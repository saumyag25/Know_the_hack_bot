#imported required libraries
import os
import telegram
from telegram import *                    
from telegram.ext import * 
from requests import *
from telegram import Update
from telegram.ext import Updater, CommandHandler
from telegram import Update  
from telegram.ext import CallbackContext  
from telegram.ext import MessageHandler  
from telegram.ext import Filters  

#Created various buttons for building menu

randomYes ='/Yes' 
randomNo = '/No'
randomTime= '/Time'
location='/Location ' 
elgibility='/Eligibility'
register='/Registration'
resource='/Resources'
tracks='/Tracks'
contact='/Contacts'
rule='/Rules' 
sched='/Schedule'
prizes='/Prizes'
other='/FAQ'
stop='/Stop'

def Start(update: Update, context: CallbackContext):   #start : to start the bot 
     buttons = [[KeyboardButton(randomYes)], [KeyboardButton(randomNo)]]
     context.bot.send_message(chat_id=update.effective_chat.id, text='''😁Hola Hackers,Welcome to know_the_hack bot!
Our Organization Tragic Bytes is hosting a Hackathon,Know the Hacks.
Do you want to know more about the hackathon??🚀🚀''', reply_markup=ReplyKeyboardMarkup(buttons)
        )

def Yes(update: Update, context: CallbackContext):  #yes: to continue for the updates of hackathon
    update.message.reply_text(  
        '''This hackathon is a student-led event that brings together students from different universities to work on innovative projects.
This Hackathon will be held in hybrid mode🚀🚀.
Please Type /help to know more !!''' 
        ) 
def No(update: Update, context: CallbackContext):  #no: to exit from the bot
    update.message.reply_text(  
        '''🙄Mogambo Sad Hua🙄''' 
        ) 
   
def help(update: Update, context: CallbackContext):  #Function to display the information(menu)about the hackathon 
        
       buttons = [[KeyboardButton(randomTime)], [KeyboardButton(location)],[KeyboardButton(elgibility)],[KeyboardButton(tracks)],[KeyboardButton(prizes)],[KeyboardButton(rule)],[KeyboardButton(sched)],[KeyboardButton(resource)],[KeyboardButton(register)],[KeyboardButton(contact)],[KeyboardButton(other)],[KeyboardButton(stop)]]
       context.bot.send_message(chat_id=update.effective_chat.id, text='''How may I help you??''', reply_markup=ReplyKeyboardMarkup(buttons)
        )
def Time(update: Update, context: CallbackContext):  #Function to inform date and time for the hackathon
    update.message.reply_text(  
        '''📅Date : 11th February 2023(Saturday) and 12th February 2023 (Sunday).
🕚Time : Submission window will open from 10:00 AM on Saturday and Closes at 11:59 PM on Sunday.
''' 
) 
def Location(update: Update, context: CallbackContext):  #Function to inform location for the hackathon for offline participants
    update.message.reply_text(  
        '''📍Location(For Offline Participants Only) : Indira Gandhi Delhi Technical University for Women
James Church,New Church Rd, Opp. St, Kashmere Gate, New Delhi, Delhi 110006''' 
        ) 
def Eligibility(update: Update, context: CallbackContext):  #Function to mention eligibility for the hackathon
    update.message.reply_text(  
        '''📝Eligibility : Open for all College Students''' 
        )
def Tracks(update: Update, context: CallbackContext):  #Function to display available tracks for the hackathon
    update.message.reply_text(  
        '''🚩Tracks:
🎯Education 🏫
🎯HealthCare 🏥
🎯AR/VR 👓
🎯Open innovation 💡
🎯Environment 🌴
🎯Women Empowerment 👩‍🎓
''' 
        ) 
def Prizes(update: Update, context: CallbackContext):  #Function for listing prizes for the hackathon winners
    update.message.reply_text(  
        '''🏆Prizes:
🥇Winner: Winner Medal along with a Certificate, for each member of the team.
🥈1st Runner Track:1st Runner Up Medal along with a Certificate, for each member of the team.
🥉2nd Runner Track:2nd Runner Up Medal along with a Certificate, for each member of the team.
👧All Girls Team:All Girls Team Medal along with a Certificate, for each member of the team.
📦All the above Mentioned Winners will get some amazing swags too.
''' 
)
def Rules(update: Update, context: CallbackContext): #Function for listing rules for the hackathon 
    update.message.reply_text(  
        '''🎯Rules
✔ You must treat all team members, competitors, judges, coaches, volunteers, etc, with respect and courtesy.
✔ Hackathon teams will be a maximum of 5 people
✔ All prizes are to be shared between all team members
✔ Teams should be made up exclusively of students or EMCRs who are not organizers, volunteers, judges, sponsors, or in any other privileged position at the event.
✔ All team members should be present at the event. Leaving the venue for some time to hack elsewhere is fine.
✔ Teams can of course gain advice and support from organizers, volunteers, sponsors, and others.
✔ All work on a project should be done during the hackathon.
✔ Teams can use an idea they had before the event.
✔ Teams can work on ideas that have already been done. Hacks do not have to be “innovative”. If somebody wants to work on a common idea they should be allowed to do so and should be judged on the quality of their hack.
✔ Teams can use libraries, frameworks, or open-source code in their projects. Working on a project before the event and open-sourcing it for the sole purpose of using the code during the event is against the spirit of the rules and is not allowed.
✔ Teams must stop hacking once the time is up. However, teams are allowed to debug and make small fixes to their programs after time is up. e.g. If during demoing your hack you find a bug that breaks your application and the fix is only a few lines of code, it’s okay to fix that. Making large changes or adding new features is not allowed.
✔ Teams can be disqualified from the competition at the organizers’ discretion.
''' 
        )  
def Schedule(update: Update, context: CallbackContext):  #Function to notify the schedule for the hackathon
    update.message.reply_text(  
        '''⏳Schedule:
🚀Inauguration of hackathon: 09:00 Am-10:00 am at 11th February,2023.
🚀Hackathon Starts at 10.00am on 11th February,2023.
🚀Submission will close at 12am on 12th February,2023.
🚀Closing Ceremony at 8.00 am on 13th February,2023.
🚀There will be some Fun Events and sessions  in between.
''' 
        )     
def Resources(update: Update, context: CallbackContext):  #Function for listing resources for the users to prepare for the hackathon 
    update.message.reply_text(  
        '''📒Resources:
💻Web Development:
https://youtube.com/playlist?list=PL0Zuz27SZ-6M1Uopt6_VL3gf3cpMnwavm

📱Android Development:
https://youtu.be/mXjZQX3UzOs
https://youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ

🚀AI/ML:
https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe
https://youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME

👓AR/VR:
https://youtu.be/WzfDo2Wpxks
''' 
        )
def Registration(update: Update, context: CallbackContext):  #Function for details of Registration process
    update.message.reply_text(  
        '''✨✨We highly Encourage you to Register for this Hackathon.You can Register For this Hackathon in very few steps.There are some advantages for the first 100 registrations.
Click on the link below👇,enter your details and get yourself registered for this amazing hackathon and Happy Developing✨✨
https://forms.gle/43wzfYb38WhyQN4H6
Deadline to Register:8th February,2023 
''' 
        )     

def Contacts(update: Update, context: CallbackContext):  #Function to give contact details
    update.message.reply_text(  
        '''📧Contact: If you have any queries, kindly contact us at knowthehack@gmail.com''' 
        ) 
def FAQ(update: Update, context: CallbackContext):  #Function For Listing Frequently aasked questions for clearing all the doubts of user
    update.message.reply_text(  
        '''❓Frequently Asked Questions❓
♦ What is a Hackathon? 💻
A hackathon is a programming competition in which competitors use technology to build innovative projects within 36 hours. There will be opportunities to win cool prizes, learn from our key-note speakers,and network with our sponsors.

♦ How much does it cost? 💵
Know The Hack is absolutely free to attend! You can participate for free.

♦ How many members in a team? 👩‍👩‍👦
The team may consist of 2-4 members. You can also take part solo in this hackathon

♦ Are there any rules? 🎯
Attendees must abide by the Tragic Bytes Code of Conduct. We want to respect each other and keep Know The Hack a safe environment for all participants

♦ Where will it be hosted? 🏫
Know the Hack will be hosted in February, 2023, in both offline and online mode. For offline the venue is IGDTUW and for online the hackathon will take place at Devfolio.

♦ How to register? 🖱
You can type /Registration register or you can directly visit our website for registration!

♦ What information is required for registration? 📝 
Your name,phone number, email address,your college name etc. and team members information if participating in a team.

♦ Will accommodation and food be provided? 🍕
Yes the accommodation and food will be provided for offline participants on both days.

♦ Is my data safe..? 🤗
Data privacy is of highest priority to us. Your data will not be used for any commercial purpose.

♦ I'm a beginner. Can I still participate? 😃
We encourage you to participate in this hackathon, regardless of your experience level. Learn as you make it!.

If you have any other queries, kindly contact us at knowthehack@gmail.com     
''' 
)  
def Stop(update: Update, context: CallbackContext):  #Function To stop the bot
    update.message.reply_text(  
        '''🙏Thank you for Contacting us.Please type /Start if you want to contact us again🙏''' 
        ) 
def unknownCommand(update: Update, context: CallbackContext):    #Function to recognize any unknown command
    update.message.reply_text(  
        "Sorry '%s' is an invalid command" % update.message.text  
        )  
  
def unknownText(update: Update, context: CallbackContext):  #Function to recognize any unknown text
    update.message.reply_text(                                                           
        "Unfortunately, the system cannot recognize you, you said '%s'" % update.message.text  
        )  
 
updater = Updater('5856182538:AAHc5u-KuVfQ7wEzK3KwUE4vR-LY5gEf9X8',use_context=True)  #To store Api Token
dispatcher = updater.dispatcher

#Various Handlers to Run the commands

Start_handler = CommandHandler('Start', Start)
dispatcher.add_handler(Start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

Yes_handler = CommandHandler('Yes', Yes)
dispatcher.add_handler(Yes_handler)

No_handler = CommandHandler('No', No)
dispatcher.add_handler(No_handler)

Time_handler = CommandHandler('Time', Time)
dispatcher.add_handler(Time_handler)

Location_handler = CommandHandler('Location', Location)
dispatcher.add_handler(Location_handler)

Eligibilty_handler = CommandHandler('Eligibility', Eligibility)
dispatcher.add_handler(Eligibilty_handler)

Tracks_handler = CommandHandler('Tracks', Tracks)
dispatcher.add_handler(Tracks_handler)

Prizes_handler = CommandHandler('Prizes', Prizes)
dispatcher.add_handler(Prizes_handler)

Rules_handler = CommandHandler('Rules', Rules)
dispatcher.add_handler(Rules_handler)

Schedule_handler = CommandHandler('Schedule', Schedule)
dispatcher.add_handler(Schedule_handler)

Resources_handler = CommandHandler('Resources', Resources)
dispatcher.add_handler(Resources_handler)

Registration_handler = CommandHandler('Registration',Registration )
dispatcher.add_handler(Registration_handler)

Contacts_handler = CommandHandler('Contacts', Contacts)
dispatcher.add_handler(Contacts_handler)

FAQ_handler = CommandHandler('FAQ', FAQ)
dispatcher.add_handler(FAQ_handler)

Stop_handler = CommandHandler('Stop', Stop)
dispatcher.add_handler(Stop_handler)

unknownCommand_handler=MessageHandler(Filters.command,unknownCommand)
dispatcher.add_handler(unknownCommand_handler)

unknownText_handler=MessageHandler(Filters.text,unknownText)
dispatcher.add_handler(unknownText_handler)

updater.start_polling()  #To start the Bot