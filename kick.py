import config

motion = config.loadProxy("ALMotion")
config.stiffnessOn(motion)
def kick():
    f = .07

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

    names.append('RShoulderRoll')
    angles.append(
    [-0.5752918720245361,
    -1.30]
    )
    times.append(factor([1.05,3],f))

    motion.angleInterpolation(names, angles, times, True)
    config.stiffnessOff(motion)
