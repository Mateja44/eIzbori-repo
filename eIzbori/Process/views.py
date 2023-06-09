from django.shortcuts import render
from Process.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
# Create your views here.

#TODO make a check for if the user is logged in, make a login page.
def voting_view(request,key):

    #following if statement only matters AFTER the ballot is filled.
    if request.method == 'POST':

        # first_filter = ballot.objects.filter(votetype = election.objects.latest('id').Phase)
        # second_filter = first_filter.filter(voter = key_of.objects.get(key = key).user )

        # this IF statement checks if the current user has voted already for the current phase, and checks if there is an active election.

        user = key_of.objects.get(key = key).user

        if  user.votestatus == election.objects.latest('id').Phase and election.objects.latest('id').Phase != 2 :
            votees = [value for key, value in request.POST.items() if key.startswith('checkbox')]
            
            for item in votees:
                usermodel = get_user_model()
                newballot = ballot()
                newballot.votes = usermodel.objects.get(id = item)
                newballot.votetype = election.objects.latest('id').Phase
                newballot.save()
            
            user.votestatus += 1
            user.save()

            # put email system here that confirms that someone successfully voted.
            response = HttpResponse("Successfully voted.")
            return response
        else:
            response = HttpResponse("You have already voted for the current step of the election.")
            return response
        #make a success html to post to after voting.

    #default method when loading the page for the first time, therefore this will usually happen when loading the page.
    if request.method == 'GET':


        if election.objects.latest('id').Phase == 0:
            #pulling info from database here v
            user = key_of.objects.get(key = key).user
            local_cent = is_within.objects.get(user = user).local_center
            voteeslist = list(is_within.objects.filter(local_center = local_cent))
            votees = []

            for object in voteeslist:
                votees.append(object.user)
            
            #storing the data in a easily accessible format for putting it into html.
            voteesdict = {}
            for object in votees:
                dict = {}
                name = f"{object.first_name} {object.last_name}"
                id = object.id
                dict['name'] = name
                dict['id'] = id
                voteesdict[f"votee_{len(voteesdict)}"] = dict


            #KEEP IN MIND: defining the entire name as "name" here, dont use first_name,last_name, at least not in html.
            currentuser = { 'local_center':local_cent.name, 'name':f"{user.first_name} {user.last_name}", 'licence' : user.licence}
            
            context = { 'currentuser': currentuser , 'key':key, 'votees' : voteesdict }
            # user > user object
            # votees > list of user dictionaries pulled from database
            # key > key that is gotten from the url.
            return render(request, 'ballot.html', context = context)
    
        if election.objects.latest('id').Phase == 1:
            user = key_of.objects.get(key = key).user
            local_cent = is_within.objects.get(user = user).local_center
            localcentlist = list(is_within.objects.filter(local_center = local_cent))
            candidates_in_localcent = []
            for item in localcentlist:
                candidates_in_localcent.append(item.user)
            #this gets all the ballots that have someone from the local center of the current user, which is a necessary step to count all the votes per candidate. 
            ballots = ballot.objects.filter(votes__in = candidates_in_localcent)

            candidate_dict = {}

            # to be later ordered in html with {% regroup %}
            for object in candidates_in_localcent:
                candidate_dict[object] = ballot.objects.filter(votes = object).count()

            currentuser = { 'local_center':local_cent.name, 'name':f"{user.first_name} {user.last_name}", 'licence' : user.licence}

            context = {'currentuser':currentuser, 'key': key, 'votees' : candidate_dict}
                #TODO ...make ballot2.
            return render(request, 'ballot2.html', context = context)
        
        if election.objects.latest('id').phase == 2:
            response = HttpResponse("There is no election going on right now.")
            return response

def Commission_view(request):
    #need to add different dictionaries, for different phases in the election.
    votes = {}
    regions = list(regional_center.objects.all())
    for region in regions:
        votes[region] = {}
        locals = list(region.local_center_set.all())
        for local in locals:
            votes[region][local] = {}
            iswithinset = list(local.is_within_set.all())
            members = []
            for item in iswithinset:
             members.append(item.user)
            for member in members:
                count = ballot.objects.filter(votes = member).count()
                votes[region][local][member] = count


    # centers = list(local_center.objects.all())
    # votes = {}
    # for center in centers:
    #      iswithinset = list(center.is_within_set.all())
    #      members = []
    #      for item in iswithinset:
    #          members.append(item.user)
    #      votes[center] = {}
    #      for member in members:
    #         count = ballot.objects.filter(votes = member).count()
    #         votes[center][member] = count
    # print(votes) 

### TODO make way (probably a button) to start a new election, and make sure it sets the "votestatus" param of the custom user to 0, and wipes the ballot table, MAKING SURE to follow guidelines in models.py for the ballot model.


    context = {'votes' : votes}
    return render(request, 'commission.html', context = context )
            #TODO make commision page.
