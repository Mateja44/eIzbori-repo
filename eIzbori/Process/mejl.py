import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import random

smtp_port = 587                 
smtp_server = "smtp.gmail.com"  
#Ispod upisujemo nasu zajednicku mejl adresu sa koje prosledjujemo linkove kandidatima.
email_from = "agandr456@gmail.com"

email_list = []
licence_list = []

#U zagrade ispod ubaciti naziv csv fajla, a u uglaste zagrade, upisati broj kolone u kojoj se nalaze mejlovi i licence
with open("data7.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        email_list.append(row[5])
        licence_list.append(row[4])

size = len(email_list)
random_list = []
for i in range(size):
    r = random.randint(100000, 999999)
    if r not in random_list:
        random_list.append(r)

modified_list = []
for number in random_list:
    number_str = str(number)
    modified_number = "!?Xx" + number_str
    modified_list.append(modified_number)


with open('data7.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Add the new column header
header = rows[0]
header.append('Passwords')

# Iterate over the rows and add the new value to each row
for i, row in enumerate(rows[1:]):
    new_value = modified_list[i]  # Get the corresponding value for the new column
    row.append(new_value)

# Write the updated data to a new CSV file
with open('data8.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

pswd = "xuqumizscvldnrgo" #Ovo je sifra koja je istekla s obzirom da je generisana samo u svrhu testiranja! Omoguci 2FA 

subject = "Elektronsko glasanje"

def send_emails(email_list):

    base_url = "http://127.0.0.1:8000/login/"

    for index, number in enumerate(licence_list):
        link = f'{base_url}{number}'
        person = email_list[index]
        random_number = modified_list[index]

        body = f'{link}\nMolim vas iskoristite ovu sifru kako biste se ulogovali na sajt.\n{random_number}'

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()

send_emails(email_list)