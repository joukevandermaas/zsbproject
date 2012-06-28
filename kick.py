import config

def factor(list, f):
    return [f*x for x in list]

motion = config.loadProxy("ALMotion")

f = .1

names = list()
angles = list()
times = list()

names.append('RKneePitch')
angles.append(
[1.0769100189208984,
 0.808459997177124,
 0.5568840503692627,
 0.3467259407043457]
#0.09975194931030273,
#-0.09232791513204575]
)
times.append(factor([1,2,3,4], f))
motion.angleInterpolation(names, angles, times, True)
