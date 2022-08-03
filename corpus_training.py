#instance of chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

class ENGSN:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot(
    'Codeworks',
    tagger_language = ENGSN,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

chatbot.storage.drop()
#Chatterbot training
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    './greetings.yml',
    './UBClass.yml',
    './SEL.yml',
    './equipment.yml',
    './webDev.yml',
    './general_Info.yml',
    './info_about_programming.yml',
    './COVID_Info.yml',
    './Game_Dev.yml',
    './staffInfo.yml',
    './Python.yml',
)
trainer.export_for_training('./my_export.json')

while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

