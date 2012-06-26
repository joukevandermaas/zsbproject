import config
import motion
import almath
import sys
import time

def main(effector):
    motionProxy = config.loadProxy("ALMotion")
    config.stiffnessOff(motionProxy)
    
    while True:
        print motionProxy.getPosition(effector, 2, False)
        time.sleep(0.5)


effector = "LLeg" if len(sys.argv) == 1 else sys.argv[1]
if __name__ == "__main__":
    main(effector)
