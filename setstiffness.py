'''
Nao Goal Kick

Wessel Klijnsma - 10172432 
Marysia Winkels - 10163727 
Koen Keune - 10003527 
Jouke van der Maas - 10186883

**setstiffness.py**
Sets the stiffness of a joint or joint group. Useful when testing or recording using record.py, 
to move certain limbs around. It requires two command line arguments: the joint or joint group 
to set and the stiffness (from 0.0 to 1.0) to give it.

'''

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
