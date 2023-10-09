## Create the Email Report ##

import os
import datetime

import emails
import reports

# Function to get the text:

def getText(file):
    with open(file, "r") as file:
        text = file.readlines()
        name = text[0].strip("\n")
        weight = text[1].strip("\n")
        return f"{name}<br/>{weight}<br/><br/>"

## The Main Part of the Code is the Part that is gonna call all the functions:

def main():
    #List of the Paths:

    txt_directory = "<PATH WITH THE FILES>" ##supplier-data/descriptions/
    txt_files_names = os.listdir(txt_directory)
    txt_path = [txt_directory + filename for filename in txt_files_names if filename.endswith(".txt")]

    #Pdf Report Location:
    report_file = "/tmp/processed.pdf"

    #Generate Body:
    report_body = ""
    for txt in txt_path:
        report_body += getText(txt)

    #Report Title:
    today = datetime.datetime.today()
    time = today.strftime("%B")
    report_title = f"Procesed Update on {time} {today.day}, {today.year}"

    #Call the function to Generate Report:
    reports.generate_report(report_file,report_title,report_body)

    #Email Report:

    email_parameters = {
        "sender": "automation@example.com",
        "receiver": "<username>@example.com",
        "subject": "Upload Completed - Online Fruit Store",
        "body": "Fruis uploaded to the website. List attached to this email.",
        "attachment":report_file
    }

    message = emails.generate_email(**email_parameters)
    emails.send_email(message)

if __name__ == "__main__":
    main()

