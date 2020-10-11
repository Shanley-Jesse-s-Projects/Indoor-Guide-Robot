# the purpose of this code is to go through the valid user inputs for building input
#This code was written by: Shanley Mullen
#email: shanleymullen@gmail.com
import speech_recognition as sr
import os
r = sr.Recognizer()
talk = sr.Microphone(device_index=None)

# this is the function that gets speech input
#this function is a generic speech recognition function to use Google Speech Rec API
def speech2text(r, talk):
    with talk as source:
        print('say something!…')
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language='en-US')
        print(recog)
        return recog
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))

#method for robot response
def say(speech):
    os.system('echo \'' + speech + '\' | festival --tts')

def yes():
    say('no')


def no():
    say('yes')

# The valid room inputs
def room(where):
    if where == 'Bathroom':
        say('Follow me to the bathroom')
        return (where)
    elif where == 'Kitchen':
        say('Follow me to the Kitchen')
        return (where)
    elif where == 'Bedroom1':
        say('Follow me to the first bedroom')
        return (where)
    elif where == 'Bedroom2':
        say('Follow me to the second bedroom')
        return (where)

    elif where == 'Backdoor':
        say('Follow me to the backdoor')
        return (where)
    else:
        say('Please input another room.')
        where = speech2text(r, talk)
        return where

# Get user input
def callThread():
   say("These are the rooms you can go to: Bathroom, Kitchen, Bedroom 1, Bedroom 2, Backdoor")
    where = speech2text(r, talk)
    room(where)
    return (where)
# callThread()
