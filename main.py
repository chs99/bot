import os
import telebot
from keep_alive import keep_alive
keep_alive()

bot_token = "1960679405:AAGXzS3ArwGUJzBEnVd2_Pj6VLNenRqJ7eQ"
bot = telebot.TeleBot(token=bot_token)

#start button for bot
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id,"Hello! Thank you for using TeleMeEverything!")

#test button for bot
@bot.message_handler(commands=['test'])
def test(message):
  bot.reply_to(message, "This is a test message")

#livechats button for bot
@bot.message_handler(commands=['livechats'])
def livechats(message):
  bot.reply_to(message, "Here are some resources with live chatting or counselling options:\n\n1) CPH Online Counselling - https://www.cphonlinecounselling.sg/hc/en-us \n\n2) eCounselling by eGen - https://www.ec2.sg \n\n3) Online chat service with volunteer listeners - https://www.7cups.com")

#calm button for bot
@bot.message_handler(commands=['calm'])
def calm(message):
  bot.reply_to(message, "Here are some resources for meditation and stress relief:\n\n1) https://palousemindfulness.com/index.html \n\n2) https://www.uclahealth.org/marc/mindful-meditations")

#hotlines button for bot
@bot.message_handler(commands=['hotlines'])
def hotlines(message):
  bot.reply_to(message, "Here are some hotlines to mental health services :\n\n1) National Care Hotline (8am-12am daily): 1800-202-6868\n\n2) Institute of Mental Health’s Mental Health Helpline (24 Hour): 6389-2222\n\n3) Samaritans of Singapore (24 Hour): 1800-221-4444 \n\n4) Silver Ribbon Singapore (9am-5pm): 6385-3714\n\n5) SAF Hotline For SAF Personnel(24 Hour): 1800 278 0022 \n\n6) Big Love Child Protection Specialist Centre (9am-6pm): 6445-0400\n\n7) HEART @ Fei Yue Child Protection Specialist Centre (9.30am-5.30pm): 6819-9170\n\n8) PAVE Integrated Services for Individual and Family Protection (9am-1pm,2pm-4pm): 6555-0390\n\n9) Project StART: 6476-1482\n\n10) TRANS SAFE Centre (10am-5pm): 6449-9088\n\n11) TOUCHline Counselling hotline (9am-6pm): 1800 377 2252")

#counselling button for bot
@bot.message_handler(commands=['counselling'])
def counselling(message):
  bot.reply_to(message, "Here are some counselling services :\n\n1) AWARE (Women only) 1% of your monthly income (capped at $150; minimum fee is $20 for those who are unemployed) https://www.aware.org.sg/womens-care-centre/counselling/ \n\n2) Shan You- $80 per session (individual counselling), $100 per session (couple/family counselling) 6389-2222 http://www.shanyou.org.sg/parent/en/services/clinical-counselling-services.html/4/ \n\n3) Counselling and Care Centre- $40 to $150 per hour for Singaporean/PR earning under $10,000 monthly (full rate at $180 per hour) http://www.counsel.org.sg/ \n\n4) Calvary Community Centre (C3)- $50 per session, $5 for those who need financial assistance https://calvary.sg/ \n\n5) WINGS Counselling Centre- $80 for the first session, $60 for follow-up sessions https://www.wingscounselling.org.sg/ \n\n6) Grace Counselling Centre- Fees from $130/$180 per hourly session http://www.gracecounsellors.com/ \n\n7) Singapore Counselling Centre- Fees from $181.90 for 1 session https://scc.sg/e/counselling-fees/ \n\n8) Silver Ribbon Singapore- Free basic counselling services in person. Weekdays only, from 9am to 5pm. Appointments required https://www.silverribbonsingapore.com/counselling.html \n\n9) Family Life Society- Free. Focuses on pregnancy and parenting counselling, they also support those struggling with personal and family issues. Has volunteer-counsellors who offer free counselling services at 10 Catholic churches in Singapore. https://www.familylife.sg/RestoretoFlourish\n\n10) Wesley Methodist Church- Free. Explicitly states that it offers non-religious counselling as well. https://wesleymc.org/care/counselling\n\n11) Singapore Buddhist Free Clinic- $10 registration fee. Subsequently free https://www.sbfc.org.sg/counselling-service")


bot.polling()
