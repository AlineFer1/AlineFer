# -*- coding: utf-8 -*-
"""
Email to SMS Gateway - send SMS
@author: aline fer
"""

import smtplib
from email.message import EmailMessage
from emailToSMSConfig import senderEmail, gatewayAddress, appKey

msg = EmailMessage()
msg.set_content('lets get a bag.')

msg['From'] = senderEmail # 'email@address.com'
msg['To'] = gatewayAddress  # '3213337133@txt.att.net'
msg['Subject'] = 'Finance Family'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, appKey)

server.send_message(msg)
server.quit()
