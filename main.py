import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import os

load_dotenv()
PLACEHOLDER="[NAME]"


def send_mail(name,address):
   # resume reading
   with open("./sde_mohit_soni_resume.pdf","rb") as resume_attachment:
      payload=MIMEBase("application","pdf")
      payload.set_payload(resume_attachment.read())
      encoders.encode_base64(payload)
      payload.add_header(
         "Content-Disposition",
         "attachment; filename=sde_mohit_soni_resume.pdf",
      )
   
   # reading cover letter
   with open("./sharechat_cover_letter.pdf",'rb') as cover:
      coverLetter = MIMEBase("application","pdf")
      coverLetter.set_payload(cover.read())
      encoders.encode_base64(coverLetter)
      coverLetter.add_header("Content-Disposition","attachment;filename=sharechat_cover_letter.pdf")
   
   # Creating message with template
   with open("./Template.html") as file:
      fileRead = file.read()
      letter = fileRead.replace(PLACEHOLDER,name)
      
      msg= MIMEMultipart()
      msg['Subject'] = 'Application for MERN Stack Engineer Internship'
      msg['From'] = "Mohit Soni"
      msg['To'] = address
      mainBody = MIMEText(letter,"html")
      msg.attach(mainBody)
      msg.attach(payload)
      # msg.attach(coverLetter)
      
   # send using SMTP server
   
   with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(user=os.getenv("USER"),password=os.getenv("APP_PASSWORD"))
      connection.sendmail(
         from_addr="Mohit Soni <mohitsoni9731@gmail.com>",
         to_addrs=address,
         msg = msg.as_string()
      )
      
mailList = {
   "name":"email"
}

for item in mailList:
   send_mail(item,mailList[item])