# SYNTHesis
# Sophia Hoenig and Elizabeth Carney

import sys
import time
# To end the program
import requests
# For the speaker
import base64
from github import Github
from github import InputGitTreeElement

from pyfirmata import Arduino, util
board = Arduino('/dev/cu.usbmodem1421')
# The library that connects to Arduino

from pydub import AudioSegment
#The library that combines sounds

it = util.Iterator(board)
it.start()
# This is for the Arduino. Not exactly sure what it means, but it's important.

sound1 = "http://elizabethcarney.github.io/sound1.wav"
sound2 = "http://elizabethcarney.github.io/sound2.wav"
sound3 = "http://elizabethcarney.github.io/sound3.wav"
sound4 = "http://elizabethcarney.github.io/sound4.wav"
sound5 = "http://elizabethcarney.github.io/sound5.wav"
sound6 = "http://elizabethcarney.github.io/sound6.wav"
sound7 = "http://elizabethcarney.github.io/sound7.wav"
sound8 = "http://elizabethcarney.github.io/sound8.wav"
sound9 = "http://elizabethcarney.github.io/sound9.wav"
sound10 = "http://elizabethcarney.github.io/sound10.wav"
sound11 = "http://elizabethcarney.github.io/sound11.wav"
sound12 = "http://elizabethcarney.github.io/sound12.wav"
# Bringing in all of the sounds

key = "tAsLon5bqbHdFNzca01BlkGeyCGGv9EX"
url = ""
service = "service"
reason = "reason"
message = "hello there"
vol = "25"
# For the speaker thing

# No buttons are pressed, we are waiting for the first layer
stop = board.get_pin('a:5:i')
# Stop the building, start over from scratch
volUp = board.get_pin('d:12:i')
# Up Volume button
volDown = board.get_pin('d:13:i')
# Down Volume button
i = 1
# This will keep track of which color is being built

layer1 = ""
layer2 = ""
layer3 = ""
layer4 = ""
layer5 = ""
#This is to keep track of which sound is played on which layer. They start out as blank

ports = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
# An array of all of the ports that have a button connected

def fileName() :
    for x in ports:
    # This will run the program to check each of the ports
        boardPort = 'd:' + str(x) + ':i'
        if board.get_pin(boardPort).read() == True:
        # Is the pin in ___ port pressed?
            pressedPort = x
            # Saves the number of the port that is pressed as the variable pressedPort
        individualSound = "sound" + str(x) + ".wav"
        # Puts together the name of the correct sound file, which is the number port that is pressed plus the file type
        return individualSound, x
        # Returns the name of the sound file and the port number

def lights(patt, port) :
    loopTimes = 20
    if (patt is "0"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.305)
            board.digital[port].write(0)
            time.sleep(0.305)
    elif (patt is "1"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.295)
            board.digital[port].write(0)
            time.sleep(0.295)
    elif (patt is "2"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.305)
            board.digital[port].write(0)
            time.sleep(0.305)
    elif (patt is "3"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.20)
            board.digital[port].write(0)
            time.sleep(0.5)#
            board.digital[port].write(1)
            time.sleep(0.15)
            board.digital[port].write(0)
            time.sleep(0.2)#
            board.digital[port].write(1)
            time.sleep(0.25)
            board.digital[port].write(0)
            time.sleep(1.1)
    elif (patt is "4"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.12)
            board.digital[port].write(0)
            time.sleep(0.19)#
            board.digital[port].write(1)
            time.sleep(0.12)
            board.digital[port].write(0)
            time.sleep(0.19)
    elif (patt is "5"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.6)
            board.digital[port].write(0)
            time.sleep(0.6)
    elif (patt is "6"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.6)
            board.digital[port].write(0)
            time.sleep(1.3)#
            board.digital[port].write(1)
            time.sleep(0.3)
            board.digital[port].write(0)
            time.sleep(0.2)
    elif (patt is "7"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.1)
            board.digital[port].write(0)
            time.sleep(0.2)#
            board.digital[port].write(1)
            time.sleep(0.1)
            board.digital[port].write(0)
            time.sleep(0.2)
    elif (patt is "8"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(1)
            board.digital[port].write(0)
            time.sleep(0.25)
    elif (patt is "9"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(0.4)
            board.digital[port].write(0)
            time.sleep(0.5)#
            board.digital[port].write(1)
            time.sleep(.5)
            board.digital[port].write(0)
            time.sleep(0.1)#
            board.digital[port].write(1)
            time.sleep(0.3)
            board.digital[port].write(0)
            time.sleep(0.6)
    elif (patt is "10"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(.3)
            board.digital[port].write(0)
            time.sleep(0.3)
    elif (patt is "11"):
        for x in range(int(loopTimes)):
            board.digital[port].write(1)
            time.sleep(.3)
            board.digital[port].write(0)
            time.sleep(0.2)#
            board.digital[port].write(1)
            time.sleep(.3)
            board.digital[port].write(0)
            time.sleep(0.2)#
            board.digital[port].write(1)
            time.sleep(.3)
            board.digital[port].write(0)
            time.sleep(1)#
    
def combine(file1, file2):
    sound1 = AudioSegment.from_file(file1)
    sound2 = AudioSegment.from_file(file2)
    # Finding the files to combine. file1 will be the previous layer's complete sound and file2 will be the the new, added sound
    combined = sound1.overlay(sound2)
    # Overlays sound 1, which is the previous level's complete sound, and the new sound file
    combinedName = "layer" + str(i) + ".mp3"
    # A variable that puts together the layer number to name the new sound
    combined.export(combinedName, format='mp3')
    # Naming the new combined sound for the new layer
    return combinedName
    
def toGithub(filename):
#    from github import Github
#    from github import InputGitTreeElement
    location = '/Users/sophiahoenig/HackHer/' + filename
    user = "shoenig17"
    password = "Frogbotics1!"
    g = Github(user,password)
    repo = g.get_user().get_repo('shoenig17.github.io')
    file_list = [
        location
    ]
    file_names = [
        filename
    ]
    commit_message = filename
    master_ref = repo.get_git_ref('heads/master')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)
    element_list = list()
    for i, entry in enumerate(file_list):
        with open(entry) as input_file:
            data = input_file.read()
        if entry.endswith('.mp3'):
            data = base64.b64encode(data)
        element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
        element_list.append(element)
    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)  
    # Don't touch this!!!! I do not understand that well it but it works.
    
def playSound(url):
    payload = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + vol + "</volume></play_info>"
    p = requests.post('http://192.168.1.72:8090/speaker', data=payload)
        

##################### The command part of the program starts ########################

while stop.read() == 0:
# While the stop button is not being pressed:
    
    volCommand = "<volume>" + str(vol) + "</volume>"
    r = requests.post('http://192.168.1.72:8090/volume', volCommand)
    # Send the current volume to the speaker
    
    if volUp.read() == 1:
    # If the up volume button is being pressed, volume = volume + .5
        vol = vol + 0.5
        
    if volDown.read() == 1:
    # If the down volume button is being pressed, volume = volume - .5
        vol = vol - 0.5

    if i == 1:
    # The first button is pressed. The corresponding file is played, and the bottom row of white LEDs starts to move in its set pattern.
        individualSound, x = fileName()
        # Calls the function fileName(), which generates the name of the wav file
        wav_audio = AudioSegment.from_file(individualSound, format = "wav")
        wav_audio.export("layer1.mp3", format = "mp3")
        # Just this one time it takes the .wav audio and converts it to mp3 within this function
        layer1 = "layer1.mp3"
        # Sets the variable layer1 as the entire sound being played in layer 1, which in this case is individualSound
        toGithub(layer1)
        # Sends the mp3 to Github so the file exists on the internet
        url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/" + layer1
        playSound(url)
        # Will send the correct sound file to the speaker, which in this case is layer1.mp3
        lights(x, "A0")
        #Play the correct light pattern, sending the number pattern to run and what port (and subsequent color) the pattern will run on
        i = i + 1
        # Pushes the loop forward
        
    elif i == 2:
    # The second button is pressed. The first file and the second file are combined and played. The first two rows, white and blue, are played.
        individualSound, x = fileName()
        # Calls the function fileName(), which will return individualSound, which is the sound chosen to be added and the number port being pressed
        combinedName = combine(layer1, individualSound)
        # Calls the function combinedSounds and gives it layer1, the entire sound of layer1, and individualSound, which is returned from fileName and is the second sound chosen. 
        layer2 = combinedName
        # Sets layer2 to the new name of the combined sound file
        toGithub()
        # Sends the mp3 to Github so the file exists on the internet
        url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/" + layer2
        playSound(url)
        # Sends the new, combined sound file to the speaker
        lights(x, "A1")
        #Play the correct light pattern, sending the number pattern to run and what port (and subsequent color) the pattern will run on
        i = i + 1
        # Pushes the loop forward

    elif i == 3:
    # The third button is pressed. The composite file is combined with the third file and played. The first three rows, white, blue, and green, are played.
        individualSound, x = fileName()
        # Calls the function fileName(), which will return individualSound, which is the sound chosen to be added and the number port being pressed
        combinedName = combine(layer2, individualSound)
        # Calls the function combinedSounds and gives it layer1, the entire sound of layer1, and individualSound, which is returned from fileName and is the second sound chosen. 
        layer3 = combinedName
        # Sets layer2 to the new name of the combined sound file
        toGithub()
        # Sends the mp3 to Github so the file exists on the internet
        url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/" + layer3
        playSound(url)
        # Sends the new, combined sound file to the speaker
        lights(x, "A2")
        #Play the correct light pattern, sending the number pattern to run and what port (and subsequent color) the pattern will run on
        i = i + 1
        # Pushes the loop forward

    elif i == 4:
    # The fourth button is pressed. The composite file is combined with the fourth file and played. The first four rows, white, blue, green, and yellow, are played.
        individualSound, x = fileName()
        # Calls the function fileName(), which will return individualSound, which is the sound chosen to be added and the number port being pressed
        combinedName = combine(layer3, individualSound)
        # Calls the function combinedSounds and gives it layer1, the entire sound of layer1, and individualSound, which is returned from fileName and is the second sound chosen. 
        layer4 = combinedName
        # Sets layer2 to the new name of the combined sound file
        toGithub()
        # Sends the mp3 to Github so the file exists on the internet
        url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/" + layer4
        playSound(url)
        # Sends the new, combined sound file to the speaker
        lights(x, "A3")
        #Play the correct light pattern, sending the number pattern to run and what port (and subsequent color) the pattern will run on
        i = i + 1
        # Pushes the loop forward

    elif i == 5:
    # The fifth button is pressed. The composite file is combined with the fifth file and played. All of the rows, white, blue, green, yellow, and red, are played.
        individualSound, x = fileName()
        # Calls the function fileName(), which will return individualSound, which is the sound chosen to be added and the number port being pressed
        combinedName = combine(layer4, individualSound)
        # Calls the function combinedSounds and gives it layer1, the entire sound of layer1, and individualSound, which is returned from fileName and is the second sound chosen. 
        layer5 = combinedName
        # Sets layer2 to the new name of the combined sound file
        toGithub()
        # Sends the mp3 to Github so the file exists on the internet
        url = "https://raw.githubusercontent.com/shoenig17/shoenig17.github.io/master/" + layer5
        playSound(url)
        # Sends the new, combined sound file to the speaker
        lights(x, "A4")
        #Play the correct light pattern, sending the number pattern to run and what port (and subsequent color) the pattern will run on
        i = i + 1
        # Pushes the loop forward
    else:
        print("Your track is complete")
        time.sleep(15)
        s = requests.get('http://192.168.1.72:8090/standby')
        sys.exit()
        # The program lets the music play for a while and then ends



sys.exit()
# If the stop button is being pressed, the program ends
