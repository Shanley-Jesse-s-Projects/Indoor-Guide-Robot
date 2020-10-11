#code written by Jesse Rosart-Brodnitz in March 2020
#contact: jorbaustin@gmail.com

import time
import threading # only used for threading functions
import loopDrive as chino   
import Lab6Template as l6   
import user_Input as ur
import L2_speed_control as sc  #the imported file was provided through the MXET 300 class with adapatations. 
import summaryMatrix as sumsum

def driveMethod( id ):
    l6.loop_drive()
def l5SumMatrix( id ):
    
    sumsum.portRun(location)
    #return(location)
    
def main(p):
    # Waits for the threads to finish, then stops.
    threads = []
    t = threading.Thread( target=driveMethod, args=(1,) )       #args=(1,) )
    threads.append(t)
    t.start()
    t2 = threading.Thread( target=l5SumMatrix, args=())#, args=(2,))   #args=(2,location))
    threads.append(t2)
    t2.start()
    print( "Main has spawn all the threads." )
    t.join()
    t2.join()
    print( "Done!" )

w=ur.callThread()
location = w
print(w)
main(w)
