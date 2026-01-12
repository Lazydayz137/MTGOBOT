#This code was written by Raymond Cheung
#No one is allowed to modify this code
#if you have any questions about it, I can be emailed at Darkray16@yahoo.com
#This is a bot that with automated behavior to run independantly on Magic the Gathering: Online

#DEPENDENCIES
#used in controller to set time of transaction for recording
from datetime import datetime
import sys
import os

# Add the project root to the Python path, which is one level up from the script's directory.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Add project subdirectories to the Python path.
sys.path.append(os.path.join(project_root, "model"))
sys.path.append(os.path.join(project_root, "view"))
sys.path.append(os.path.join(project_root, "controller"))

import config
import model
import view
import controller

exec(open(os.path.join(config.BOT_ROOT, "ini.py"), "rb").read())


classified_ad = "Human BUYING     Frost Titan [s4] | Inferno Titan [s3] | Grave Titan [s9] | Devastating Summons [s1] | Mox Opal [s9] | Contested Zone [s2]  Please PM me first"
classified_ad_selling = "Human SELLING ZEN ZEN WWK ZZW [s1][s3] | Slagstorm 2x for [s3] | Kargan Dragonlord [s1][s1] | Demon of Death's Gate [s4] | Elvish Archdruid [s1]"


selling_greeting = "Entering selling mode.  When you are finished, please type the word done into the chat window"

def memorize(func):
    """
    Cache the results of the function so it doesn't need
    to be called again, if the same arguments are provided
    """
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
            
        result = func(*args)
        cache[args] = result
        return result
    return wrapper



class ErrorHandler(Exception):
    #custom Exception parent class to handle errors
    
    def __init__(self, message):
        ERRORHANDLERAPP = settings["ERRORHANDLERAPP"]
        self._errormsg = message
        ErrorHandlerApp = App(ERRORHANDLERAPP)
        if not ErrorHandlerApp.window():
            App.open(ERRORHANDLERAPP); wait(2)
        ErrorHandlerApp.focus(); wait(1)
        self.__openRecord()
        self.__writeRecord()
        ErrorHandlerApp.close()
    def __openRecord(self):
        #this will be different depending on the application
        pass
    def __writeRecord(self):
        type(self._errormsg + "\n")
        
        
class Bot(object):
    #this is at the highest level and owns all other classes
    #its a wrapper class that will encompass every other class
    __single = None
    
    def __init__(self):
        #no more than one instance is needed at a time
        if Bot.__single:
            raise ErrorHandler("Bot class cannot be instantiated more than once")
        Bot.__single = self
        
        self.primary_controller = controller.MainController()
        
    def main(self):
        #run when script starts
        self.primary_controller.startup()
        
    def do_function(self):
        self.primary_controller.trade_mode()

        

class Customer(object):

    def __init__(self, name):
        #set the name of customer upon initialization
        self.name = name
        
    def set_name(self, name):
        #Set the name of the customer, e.g. their screen name
        self.name = name
        
    def get_name(self):
        #Get the name of the customer, e.g. their screen name
        return self.name
        
    def set_mode(self, mode):
        #find whether customer wants to buy or sell
        self.mode = mode

    def get_mode(self):
        return self.mode
        
        
class RecordToFile(object):
    #this object will write the transaction to a file
    #it will take care of opening, writing, and reading transaction history
    
    def __init__(self, transaction):
        self.__record = transaction
        
    def open_record(self, filename):
        #wrapper function for open file
        pass
        
    def write_record(self):
        #write the record property to an already opened file
        pass
        
    def read_record(self, file):
        #read an already opened file
        pass
        


#run the bot
Bot_App = Bot()
Bot_App.do_function()