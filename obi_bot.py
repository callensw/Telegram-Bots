from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from requests import get
from bs4 import BeautifulSoup
import pandas as pd 
import matplotlib.pyplot as plt
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

  
def suppie(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Suppie")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
    /obi_rating - Get latest Obi Wan IMDb 
    rating
    /jedi_wisdom - Get Jedi Wisdom
    /suppie - Get a Suppie""")

def obi_rating(update: Update, context: CallbackContext):
    
    response = get('https://www.imdb.com/title/tt8466564/?ref_=ttep_ep_tt')

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all the episode containers from the season page
    ep_containers = soup.find_all('div', class_ = 'sc-7ab21ed2-2 kYEdvH')
    
    obi_wan_imdb_score = ep_containers[0].find('span', class_='sc-7ab21ed2-1 jGRxWM').text
    
    update.message.reply_text("Hey @PrideOrDie69! The current IMDb score for the Obi Wan series is: " + obi_wan_imdb_score + "!! Wow, can you believe it?")

def jedi_wisdom(update: Update, context: CallbackContext):
    quotes = ["Only a sith deals in absolutes.", "Try not. Do or do not. There is no try.", 
              "Fear is the path to the dark side…fear leads to anger…anger leads to hate…hate leads to suffering.",
              "These are not the droids you're looking for.", "The ability to speak does not make you intelligent.",
              "Your focus determines your reality.", "So this is how liberty dies…with thunderous applause.", 
              "To die for one’s people is a great sacrifice. To live for one’s people, an even greater sacrifice.",
              "You were my brother Anakin! I loved you!", 
              "You were the chosen one! It was said that you would destroy the Sith, not join them. You were to bring balance to the force, not leave it in darkness.",
              "Your eyes can decieve you... don't trust them.",
              "Don't try it, I have the high ground",
              "Chancellor Palpatine is evil!", "In my experience, there's no such thing as luck.",
              "If you define yourself by the power to take life, the desire to dominate, to possess… then you have nothing.",
              "Who is more foolish? The fool or the fool who follows him?",
              "Skill is the child of patience.", "You want to go home and rethink your life.",
              "Remember... the Force will be with you. Always.",
              "The Force is what gives a Jedi his power. It's an energy field created by all living things. It surrounds us and penetrates us. It binds the galaxy together.",
              "A great leap forward often requires taking two steps back.",
              "You can kill me, but you will never destroy me. It takes strength to resist the dark side. Only the weak embrace it.",
              "You underestimate my power."]
    random_index = random.randint(0, len(quotes)-1)
    quote = quotes[random_index]
    update.message.reply_text(quote)
    
    
def main():
    updater = Updater("API Token goes here", use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('suppie', suppie))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('obi_rating', obi_rating))
    updater.dispatcher.add_handler(CommandHandler('jedi_wisdom', jedi_wisdom))
    
    updater.start_polling()
    

if __name__ == '__main__':
    main()