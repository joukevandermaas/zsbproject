import config

def factor(list, f):
    return [f*x for x in list]

motion = config.loadProxy("ALMotion")

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
times.append(factor([0.1, 1.1, 2.1, 3.1, 4.1, 5.1], f))

names.append('LKneePitch')
angles.append(
[0.9495041370391846,
 1.1719341278076172,
 1.4725980758666992,
 1.688892126083374,
 1.9051860570907593,
 2.112546443939209,
 2.112546443939209])
times.append(factor([0.1, 0.96, 1.82, 2.68, 3.54, 4.4, 5.26], f))

names.append('LAnklePitch')
angles.append(
[-0.5921659469604492,
 -0.7869839668273926,
 -0.8866939544677734,
 -0.9526557922363281,
 -0.9772000312805176,
 -1.018618106842041]
)
times.append(factor([0.1, 1.1, 2.1, 3.1, 4.1, 5.1], f))

names.append('LAnkleRoll')
angles.append(
[0.0015759468078613281,
 0.03992605209350586,
 0.04146003723144531,
 0.0813438892364502,
 0.11202406883239746,
 0.10281991958618164]
)
times.append(factor([0.1, 1.1, 2.1, 3.1, 4.1, 5.1], f))

names.append('LHipRoll')
angles.append(
[4.1961669921875e-05,
 0.1565098762512207,
 0.3037738800048828,
 0.3988819122314453,
 0.6075060367584229]
)
times.append(factor([0.1, 1.6, 3.1, 4.6], f))


motion.angleInterpolation(names, angles, times, True)

