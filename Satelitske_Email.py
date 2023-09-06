# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:51:56 2023

@author:Adnan Ljeskovica - Armin Korajlic
"""

import smtplib
import datetime
import serial

# Email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'ludabudala.budalaaa@gmail.com'
smtp_password = 'kdygnthsgcnkklji'
email_sender = 'ludabudala.budalaaa@gmail.com'
email_recipient = 'armin.korajlic@fet.ba'
email_subject = 'Gas Alert'
email_message = 'Senzor se aktivirao, prisustvo gasa detektovano !'

#import serial - bio je ovdje
ser = serial.Serial('COM3', 9600) #Port com3 na windows.
email_counter = 0 #Counter za brojanje koliko mailova saljemo

while email_counter < 1: #Vrti beskonacno ovu petlju dok se ne posalje mail.
    line = ser.readline().strip().decode('utf-8')
    if line == 'SendEmail':
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email_message = f'Senzor se aktivirao, prisustvo gasa detektovano !\n\nVrijeme detekcije: {time_stamp}'

        # Send
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            message = f"Subject: {email_subject}\n\n{email_message}"
            server.sendmail(email_sender, email_recipient, message)
            server.quit()
            print(f"Email je poslan uspjesno!\nVrijeme detekcije:{time_stamp}")
            email_counter += 1
        except Exception as e:
            print(f"Failed to send email: {e}")
ser.close() # close serial
#Moze se jednostavno napraviti i da vrti petlju beskonacno, sa malom izmjenom 
#koda, ali zbog jednostavnosti nastimao sam da salje samo jednom.
#Ako hocu da salje vise puta samo cu prvu petlju zavrtiti na while 0, da
#vrti beskonacno, i onda unutar samo if uslov, poslije
#if line == 'sendemail', koji ce glasiti if emailcounter < 1 i da se onda
#odradi ovo ispod try:
#Te treba line postaviti na neku trash vrijednost, da ne aktivira se opet,
#ili imati counter od 10s, te ako i dalje gori detektor da opet salje mail
#i tako sve dok ne ugasi se.