import config 
import sys

def main(eff, speed, file):
    motion = config.loadProxy
    config.stiffnessOn(motion)

    f = open(file, 'r')
    d = f.readlines()

    for line in d:
        mp.setAngles(eff, eval(line), speed)

file = sys.arv[1]
effector = sys.argv[2]
speed = float(sys.argv[3])
if __name__ == "__main__":
    main(effector, speed, file)
