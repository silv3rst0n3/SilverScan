import telebot
from telebot import types
import fileinput
import os

# set up bot with access token
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "silver scan Wellcome...")


# define function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # get user input
    user_input = message.text

    # create custom keyboard
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    
    echo="cat $HOME/targets/"
    notify="| notify -bulk -id tel3"
    user_input = user_input.replace('../', 'aaaaaaa')
    os.system(f"{echo}{user_input} {notify}")    
     
    if user_input == 'nuclei':
        button1 = types.KeyboardButton('level1')
        button2 = types.KeyboardButton('level2')
        button3 = types.KeyboardButton('Back')
        keyboard.add(button1, button2,button3)
    if user_input == 'Show':
        button1 = types.KeyboardButton('Show Targets')
        button2 = types.KeyboardButton('Show Subs')
        button3 = types.KeyboardButton('Show Screens')
        button4 = types.KeyboardButton('Back')
        keyboard.add(button1, button2,button3,button4)
    if user_input == 'Remove':
        button1 = types.KeyboardButton('Remove Targets')
        button2 = types.KeyboardButton('Remove Subs')
        button3 = types.KeyboardButton('Back')
        keyboard.add(button1, button2,button3)

    if user_input == 'Stop':
        button1 = types.KeyboardButton('Stop Nuclei')
        button2 = types.KeyboardButton('Stop Subs')
        button3 = types.KeyboardButton('Back')
        keyboard.add(button1, button2,button3)    

    elif user_input == 'Back':
        button1 = types.KeyboardButton('nuclei')
        button2 = types.KeyboardButton('sub')
        button3 = types.KeyboardButton('Show')
        button4 = types.KeyboardButton('Remove')
        button5 = types.KeyboardButton('ls')
        keyboard.add(button1, button2, button3, button4,button5)
    else:
        button2 = types.KeyboardButton('sub')
        button3 = types.KeyboardButton('nuclei')
        button4 = types.KeyboardButton('Remove')
        button5 = types.KeyboardButton('Show')
        button6 = types.KeyboardButton('Stop')
        button7 = types.KeyboardButton('ls')
        keyboard.add(button2, button3, button4,button5,button6,button7)


    # ...
    if user_input == 'ls':
        output = os.popen('ls /home/admin/targets').read()
        bot.reply_to(message, f"List of files in the home directory:\n\n{output}")
        
    # handle sub-options
    #Show buttons
    if user_input == 'Show Targets':
        os.system('cat $HOME/targets/file.txt | notify -bulk -id tel3')
    
    if user_input == 'Show Screens':
        os.system('screen -ls | notify -bulk -id tel3')

    if user_input == 'Show Subs':
        os.system('cat $HOME/targets/subs | notify -bulk -id tel3')
    
    #remove buttons   
    if user_input == 'Remove Targets':
        os.system('rm $HOME/file.txt;echo "" > $HOME/admin/file.txt')

    if user_input == 'Remove Subs':    
        os.system('rm $HOME/subs;echo "" > $HOME/admin/targets/subs;')
    
    #sub button
    if user_input == 'sub':
        os.system('screen -d -m -S sub bash -c "bash $HOME/subfinder.sh"')
    
    #nuclei button
    if user_input == 'level1':
        os.system('screen -d -m -S nuc bash -c "bash $HOME/nuc.sh"')
    
    #Stop buttons
    if user_input == 'Stop Nuclei':
        os.system('screen -XS nuc kill ')
    
    if user_input == 'Stop Subs':
        os.system('screen -XS sub kill ')

    
    # send message with keyboard
    bot.reply_to(message, "_", reply_markup=keyboard)
    
# start the bot
bot.polling()


