# -*- coding: utf-8 -*-
"""
Email to SMS Gateway - send SMS
@author: adam getbags
"""

import smtplib
from email.message import EmailMessage
from emailToSMSConfig import senderEmail, gatewayAddress, appkey

msg = EmailMessage()
msg.set_content('Lets get a bag.')

msg['From'] = senderEmail # 'email@address.com'
msg['To'] = gatewayAddress # '3213338757@voicestream.net'
msg['Subject']= 'Finance Family'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, appkey)

server.send_message(msg)
server.quit()

