import random
import tkinter

# Dictionary of questions and answers
questions = {
            'You visit a learning website and there is no padlock next to the URL in the browser \nWhat does this mean?':
            ("\na. That your connection to the webserver is not encrypted and someone could possibly acccess your data\nb. That the site is not a google trusted website, as per the Google Network Trust List (GNTL)\nc. That the website has been hacked and therefore is not secure\nd. That the websites security is 2010 Web Standard Security Configuration (WSSC) or older",'d'), 
            'David from the Design team comes to you with their laptop, you see it has lots of pop ups for various products and websites. \nWhat will you advise them to do?':
            ('\na. Click the pop ups to unsubscribe through the browser\nb. Disconnect the device from the network and report it to IT\nc. Investigate their inbox for phishing emails they may have clicked\nd. Delete all files from the "Download" folder to prevent a virus spreada\n','b'), 
            'You need to set and remember a new password for your email. \nWhat is the best way to do this?':
            ('\na. use a randomly generated password stored in a password manager\nb. have a basic password that you slightly modify each time to make it easier to remember\nc. re-use an old password that you havent used for at least 6 months\nd. use the name of a pet so you never get locked out of important systems\n','a'), 
            'You find a USB marked with the label ‘HR – Important’ placed on your desk. \nWhat do you do next?':
            ('\na. Give it to a people and culture employee so they can check the files using their PC\nb. Plug the USB into your computer to see if there are any files that relate to you \nc. Contact IT regarding an unknown USB device found\nd. Copy the files onto a PC that is not connected to WiFi\n','c'), 
            'If you’re working and need to leave your desk for a moment.\nWhat should you do with your laptop?':
            ('\na. Nothing as long as it’s for less than 1 minute\nb. Turn off your laptop every time\nc. Lock your desktop/account\nd. None of the above\n','c'),
            'After lunch, you notice your colleague Luke seems very worried and when you ask him what\'s going on, he shows you his screen. Luke\'s laptop has been compromised and the attacker is asking him to pay a ransom or Luke\'s information will be erased, including the report he is due to submit this week.\nPeople at the office don\'t know what to do, some suggest to pay the ransom, while others disagree.\nWhat\'s your recommendation?':
            ('\na. Report immediately to your manager as well as the IT department to take control of the situation\nb. Ask everyone to chip in and collect the money the attacker is asking for as soon as possible\nc. Keep quiet and don\'t say anything, it\'s not your laptop so you should not interfere in other\'s people decision at work\nd. Ask everyone to turn off their laptops and run away out of the building\n','a'),
            'You have noticed that some colleagues have been victims of hackers over the past few months and the company does not have a centralised backup system to protect the information. You have very important and sensitive information on your laptop that you don’t want to lose.\nWhat should you do to protect your information?':
            ('\na. Buy a portable hard drive and backup all your information\nb. Talk to management and express your concern highlighting the importance of protecting the company’s information by having proper backing up procedures in place\nc. Work disconnected from the Internet and only connect when necessary\nd. Use USB flash drives to save the most important information and keep them on your home\n','b'),
            'Right before you head into an important meeting you receive an email that appears to be from payroll about a yearly bonus. Which is NOT a safe action to take?':
            ('\na. Hover over the hyperlink (without clicking) to see where it leads \nb. Carefully check the senders address \nc. Email the sender in a new email chain using the “Check Name” function in Outlook or Boxer to verify their identity \nd. Open the email on a Mac or iPhone as they cannot get regular computer viruses\n','d'),
            'An employee from Tech Support calls your mobile and tells you that they are having problems with the phone systems so they are using mobiles. \nThey tell you that your account is not archiving emails properly and need to access your Outlook. They require your password. They inform you your manager has already approved the process will only take 5 minutes.\nWhich of the following is NOT a safe course of action?':
            ('\na. Ask them to email the request through \nb. Give them the password and call tech support later to verify \nc. Tell them you will call them back using the internally listed number on the intranet \nd. None of the above options are safe\n','b')
            }

def get_attempt():
    while True:
        try:
            attempt = input('Hit \'a\', \'b\', \'c\' or \'d\' for your answer\n')
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if attempt.lower() not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! Only hit \'a\', \'b\' \'c\' or \'d\' for your response')
            continue
        else:
            break
    return attempt

def get_score(score):
    score_result = ""
    if score <= 2:
        score_result = "you scored " + str(score) + " YoU FuCkInG IdIoT"
    elif score <= 4:
        score_result = "you scored " + str(score) + " \nBrah WTF"
    elif score <= 6:
        score_result = "you scored " + str(score) + " \nBetter"
    elif score <= 8:
        score_result = "you scored " + str(score) + " \nNice"
    elif score <= 9:
        score_result = "you scored " + str(score) + " \nDude thats solid"
    else:
        score_result = "you scored " + str(score) + " \nFree Soc Socks for you!"
    return score_result


def ask_question(questions):
    item = random.choice(list(questions.items()))
    while item[0] in asked_questions:
        item = random.choice(list(questions.items()))
        if item[0] not in asked_questions:
            break
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = get_attempt()
    asked_questions.append(item[0])
    return (attempt, answer)

# Questions loop
asked_questions = []
score = 0
numquestion = 0
while numquestion <= 8:
    attempt, answer = ask_question(questions)
    if attempt == answer:
        print('Correct')
        score += 1
        numquestion += 1
    else:
        print('Incorrect!!!.')
        numquestion += 1
final_score = get_score(score)
print(final_score)