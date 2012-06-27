import config
import motion
import almath
import sys
import time

def main(effector, file):
    motionProxy = config.loadProxy("ALMotion")

    output(str(motionProxy.getAngles(effector, True)), file)
    
    motionProxy.setStiffnesses(effector, 0.0)
    while raw_input('<Enter> to record; <q> to quit. ') != 'q':
        output(str(motionProxy.getAngles(effector, True)), file)

def output(text, file):
    print text
    file.write(text + '\n')


effector = sys.argv[1]
filename = effector + ".txt"

file = open(filename, 'w')
if __name__ == "__main__":
    main(effector, file)
