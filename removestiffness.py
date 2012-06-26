import config
import motion
import almath
import sys
import time

def main(effector):
    motionProxy = config.loadProxy("ALMotion")
    motionProxy.setStiffnesses(effector, 0.0);

effector = "LLeg" if len(sys.argv) == 1 else sys.argv[1]
if __name__ == "__main__":
    main(effector)
