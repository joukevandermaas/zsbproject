import config
import motion
import almath
import sys
import time

def main(effector):
    motionProxy = config.loadProxy("ALMotion")
    
    while raw_input('------\n') != 'q':
        print motionProxy.getAngles(effector, True)


effector = "Body" if len(sys.argv) == 1 else sys.argv[1]
if __name__ == "__main__":
    main(effector)
