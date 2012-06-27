import config
import motion
import almath
import sys
import time

def main(effector, stiffness):
    motionProxy = config.loadProxy("ALMotion")
    motionProxy.setStiffnesses(effector, stiffness);

effector = sys.argv[1]
stiffness = float(sys.argv[2]) if len(sys.argv) == 3 else 0.0

if __name__ == "__main__":
    main(effector, stiffness)
