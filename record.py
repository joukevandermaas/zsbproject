#**record.py**
#Records the angles of the joints of the Nao when the user presses <enter>. 
#The script requires the name of the joint or joint group to record as a command-line argument. 
#It writes a text file with the name of that joint to a folder called 'data'.
#Written by Jouke van der Maas, Koen Keune, Marysia Winkels, Wessel Klijnsma

import config
import motion
import almath
import sys
import time

def main(effector, file):
    motionProxy = config.loadProxy("ALMotion")

    output(str(motionProxy.getAngles(effector, True)), file)
    
    #motionProxy.setStiffnesses(effector, 0.0)
    while raw_input('<Enter> to record; <q> to quit. ') != 'q':
        output(str(motionProxy.getAngles(effector, True)), file)

def output(text, file):
    print text
    file.write(text + '\n')


effector = sys.argv[1]
filename = "data/" + effector + ".txt"

file = open(filename, 'w')
if __name__ == "__main__":
    main(effector, file)
