import config

motion = config.loadProxy("ALMotion")
def positionLeftLeg():
    f = 0.5

    names = list()
    angles = list()
    times = list()

    names.append('LHipPitch')
    angles.append(
    [-0.400331974029541,
    -0.5690720081329346,
    -0.7102000713348389,
    -0.9234261512756348,
    -1.1565940380096436,
    -1.2823820114135742]
    )
    times.append(factor([1, 2, 3, 4, 5, 6], f))

    names.append('LKneePitch')
    angles.append(
    [0.9495041370391846,
    1.1719341278076172,
    1.4725980758666992,
    1.688892126083374,
    1.9051860570907593,
    2.112546443939209,
    2.112546443939209])
    times.append(factor([0.85,1.71,2.57,3.42,4.28,5.14,6.00], f))

    names.append('LAnklePitch')
    angles.append(
    [-0.5921659469604492,
    -0.7869839668273926,
    -0.8866939544677734,
    -0.9526557922363281,
    -0.9772000312805176,
    -1.018618106842041]
    )
    times.append(factor([1, 2, 3, 4, 5, 6], f))

    names.append('LAnkleRoll')
    angles.append(
    [0.0015759468078613281,
    0.03992605209350586,
    0.04146003723144531,
    0.0813438892364502,
    0.11202406883239746,
    0.10281991958618164]
    )
    times.append(factor([1, 2, 3, 4, 5, 6], f))

    names.append('LHipRoll')
    angles.append(
    [4.1961669921875e-05,
    0.1565098762512207,
    0.3037738800048828,
    0.3988819122314453,
    0.5575060367584229]
    )
    times.append(factor([1.2, 2.4, 3.6, 4.8, 6.0], f))

    names.append('HeadPitch')
    angles.append(
    [-0.1304318904876709,
    -0.37126994132995605,
    -0.6719517707824707]
    )
    times.append(factor([2,4,6], f))

    motion.angleInterpolation(names, angles, times, True)

