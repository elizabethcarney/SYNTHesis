#####################################################################
#               How to run python code on an arduino                #
#   https://www.makeuseof.com/tag/program-control-arduino-python/   #
#   1. Using command line, download pip: sudo easy_install pip      #
#   2. Use pip to install pyfirmata: pip install pyfirmata --user   #
#   3. Using Arduino IDE, open the sample program "StandardFirmata" #
#      and run it. It must be the last thing run from IDE.          #
#   4. Using command line, run this program: python blink.py        #
#      Make sure you have the correct directory.                    #
#   5. The program should run!                                      #
#####################################################################

from pyfirmata import Arduino, util
import time
board = Arduino('/dev/cu.usbmodem141221') #alter this to match arduino port on computer

patt = input('Which pattern would you like to display? (a through l): ')

loopTimes = 20
if (patt is "a"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.305)
        board.digital[8].write(0)
        time.sleep(0.305)
elif (patt is "b"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.295)
        board.digital[8].write(0)
        time.sleep(0.295)
elif (patt is "c"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.305)
        board.digital[8].write(0)
        time.sleep(0.305)
elif (patt is "d"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.20)
        board.digital[8].write(0)
        time.sleep(0.5)#
        board.digital[8].write(1)
        time.sleep(0.15)
        board.digital[8].write(0)
        time.sleep(0.2)#
        board.digital[8].write(1)
        time.sleep(0.25)
        board.digital[8].write(0)
        time.sleep(1.1)
elif (patt is "e"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.12)
        board.digital[8].write(0)
        time.sleep(0.19)#
        board.digital[8].write(1)
        time.sleep(0.12)
        board.digital[8].write(0)
        time.sleep(0.19)
elif (patt is "f"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.6)
        board.digital[8].write(0)
        time.sleep(0.6)
elif (patt is "g"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.6)
        board.digital[8].write(0)
        time.sleep(1.3)#
        board.digital[8].write(1)
        time.sleep(0.3)
        board.digital[8].write(0)
        time.sleep(0.2)
elif (patt is "h"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.1)
        board.digital[8].write(0)
        time.sleep(0.2)#
        board.digital[8].write(1)
        time.sleep(0.1)
        board.digital[8].write(0)
        time.sleep(0.2)
elif (patt is "i"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(1)
        board.digital[8].write(0)
        time.sleep(0.25)
elif (patt is "j"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(0.4)
        board.digital[8].write(0)
        time.sleep(0.5)#
        board.digital[8].write(1)
        time.sleep(.5)
        board.digital[8].write(0)
        time.sleep(0.1)#
        board.digital[8].write(1)
        time.sleep(0.3)
        board.digital[8].write(0)
        time.sleep(0.6)
elif (patt is "k"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(.3)
        board.digital[8].write(0)
        time.sleep(0.3)
elif (patt is "l"):
    for x in range(int(loopTimes)):
        board.digital[8].write(1)
        time.sleep(.3)
        board.digital[8].write(0)
        time.sleep(0.2)#
        board.digital[8].write(1)
        time.sleep(.3)
        board.digital[8].write(0)
        time.sleep(0.2)#
        board.digital[8].write(1)
        time.sleep(.3)
        board.digital[8].write(0)
        time.sleep(1)#
        
