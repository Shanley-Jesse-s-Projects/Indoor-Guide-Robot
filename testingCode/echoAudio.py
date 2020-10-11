#have the robot be able to recognize specfic objects/colors
#ask the user if feature should be added to the preexisitng map
#is yes then save it
#if no then dont save it to the overall map


#~/basics/speech_recognition/speech_recognition/__main__.py
#import __main__ as main
import time
import speech_recognition as sr
import L2_log as log
import pyaudio
import os
pa = pyaudio.PyAudio()
pa.get_default_input_device_info()

m = sr.Microphone()
r = sr.Recognizer()


def echo():     #should I add
    #while 1:
    a = 1
    ans=speech2text(a)
    print(ans)

        
    
    
    


def speech2text(check):

 #   fuck = main()
    # log.uniqueFile(value, "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.txt")

    try:
        # print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        #print("Set minimum energy threshold to {}".format(r.energy_threshold))
        
        while check==1:     #checks to break or not.   1 is continue, 0 is break 
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
            
        #     log.uniqueFile(value[0], "inputList.txt")   #mine
            
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                    log.uniqueFile(value, "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.txt")
                    #return(str.value)
                    #print("Padme come closer!")
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print("You said {}".format(value))
                    #log.uniqueFile(.format(value).encode("utf-8"), "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.txt")
                    A=0
                    #print("Padme says ", value)
                    return(value)
                    
                    
                  
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                a=1
                continue
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            
    except KeyboardInterrupt:
        pass


while 1:
    
    #value=0
    echo()
    #speech2text(1)
    break
    
