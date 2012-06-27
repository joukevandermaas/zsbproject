#-*- coding: iso-8859-15 -*-

''' Cartesian control: Arm trajectory example '''
import sys
import config
import motion
import almath

def main(eff, speed):
    mp = config.loadProxy("ALMotion")
    config.stiffnessOn(mp)
#------
#------
#------
#------
    mp.setAngles(eff,
    [4.1961669921875e-05, 4.1961669921875e-05, -0.40041589736938477, 0.9526557922363281, -0.5491299629211426, 4.1961669921875e-05],
        speed)

    mp.setAngles(eff,
    [-0.0014920234680175781, -0.007627964019775391, -0.9342479705810547, 1.262524127960205, -0.19937801361083984, 0.0015759468078613281],
        speed)

    mp.setAngles(eff,
    [0.0015759468078613281, -0.007627964019775391, -1.1014537811279297, 1.245649814605713, 0.1764519214630127, 0.0015759468078613281],
        speed)

    mp.setAngles(eff,
    [-0.0014920234680175781, -0.009161949157714844, -1.0983858108520508, 0.6642639636993408, 0.08287787437438965, 0.0015759468078613281],
        speed)

    #mp.setAngles(eff,
    #[-0.4540219306945801, 0.12889790534973145, -0.6565940380096436, -0.09232791513204575, 0.09054803848266602, -0.2070479393005371],
        #speed)


effector = "Body" if len(sys.argv) == 1 else sys.argv[1]
speed = .1 if len(sys.argv) == 2 else float(sys.argv[2])
if __name__ == "__main__":
    main(effector, speed)
