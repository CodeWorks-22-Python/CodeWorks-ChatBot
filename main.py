#instance of chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
class ENGSN:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot('Codeworks', tagger_language = ENGSN)

#Chatterbot training
cdwrk_intro = ListTrainer(chatbot)
cdwrk_intro.train([
    'What is CodeWorks?',
    """CodeWorks is a virtual and in-person 5 week, 4 days a week, 7 hours a day workshop where managers and employees
    (Your child) choose their path and learn and make code within that path. While also following weekly ‘Sprints’ which 
    are weekly objectives that the Managers and employees show their progress throughout the week. Everyday each employee
     is put into advisory groups to have check-ins, team-building, and supplemental skills development. This program includes 
     Tools of the trade related to collaboration, remote work & specific technologies, Professional skills & career exploration, 
     Financial literacy, Socio-emotional learning. These are provided throughout the 5 week process. The final sprint in 
     week 5 every group and manager will present a major project that """,
    'When did CodeWorks first begin?',
    'CodeWorks had its first run in the summer of 2017.',
    'What year did CodeWorks start?',
    'CodeWorks had its first run in the summer of 2017.',
    'How do I sign up for CodeWorks?',
    """CodeWorks has unfortunately already concluded for this year, however we will be returning next year. To sign up, you will need to apply for YouthWorks, followed by applying for CodeWorks to be your worksite.""",
    'Is there an age requirement?',
    'You or your child must be between the ages 14 and 21.',
    'How old do I have to be?',
    'You or your child must be between the ages 14 and 21.',

])
cdwrk_intro = ListTrainer(chatbot)
cdwrk_intro.train([
    "",
    "",
    "",
])
while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

