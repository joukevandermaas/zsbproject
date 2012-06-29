'''
Nao Goal Kick

Wessel Klijnsma - 10172432 
Marysia Winkels - 10163727 
Koen Keune - 10003527 
Jouke van der Maas - 10186883

**kickmotions.py**
Defines the different moves the Nao needs to perform the kick.

positionLeftLeg:  initial step, positions the left leg of the robot so the right leg can
                  move freely.
positionRightLeg: positions the right leg to make the kick.
liftArms:         lifts the robot's arms so he can hold the ball.
kick:             drops the ball and kicks it.

'''
import config

motion = config.loadProxy('ALMotion')

def factor(list, f):
    return [f*x for x in list]

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

def positionRightLeg():
    f = .5

    names = list()
    angles = list()
    times = list()

    names.append('RHipPitch')
    angles.append(
    [-0.40041589736938477,
    -0.4617760181427002,
    -0.4617760181427002,
    -0.6596620082855225,
    -0.8529460430145264,
    -1.055434226989746,
    -1.2002098083496094,
    -1.3177480697631836,
    -1.451902141571045]
    )
    times.append(factor([1,2,3,4,5,6,7,8,9], f))

    names.append('RKneePitch')
    angles.append(
    [0.9495878219604492,
    1.3699040412902832,
    1.6076741218566895,
    1.7748799324035645,
    1.7978901863098145,
    1.7978901863098145,
    1.7104520797729492,
    1.509498119354248,
    1.0769100189208984]
    )
    times.append(factor([1,2,3,4,5,6,7,8,9], f))

    names.append('RAnklePitch')
    angles.append(
    [-0.5475959777832031,
    -0.7638900279998779,
    -0.98785400390625,
    -0.9893879890441895,
    -0.98785400390625,
    -0.98785400390625,
    -0.98785400390625,
    -0.98785400390625,
    0.0583338737487793,
    0.28734792709350586]
    )
    times.append(factor([.9,1.8,2.7,3.6,4.5,5.4,6.3,7.2,9.0,9.3], f))

    names.append('RAnkleRoll')
    angles.append(
    [4.1961669921875e-05,
    0.38868483901023865]
    )
    times.append(factor([3.5, 9], f))

    names.append('RHipRoll')
    angles.append(
    [4.1961669921875e-05,
    0.1304318904876709,
    0.29917192459106445,
    0.357464075088501,
    0.357464075088501,
    0.357464075088501,
    0.357464075088501,
    0.357464075088501,
    0.357464075088501,
    0.3559298515319824]
    )
    times.append(factor([.9,1.8,2.7,3.6,4.5,5.4,6.3,7.2,8.1,9.0], f))

    motion.angleInterpolation(names, angles, times, True)

def liftArms():
    f = .3
    names = list()
    angles = list()
    times = list()

    names.append('LShoulderPitch')
    angles.append(
    [1.518618106842041,
    1.2348281145095825,
    0.9617760181427002,
    0.8022401332855225,
    0.570605993270874,
    0.45095396041870117,
    0.269942045211792,
    0.3420400619506836]
    )
    times.append(factor([1,2,3,4,5,6,7,8],f))

    names.append('LShoulderRoll')
    angles.append(
    [0.19324207305908203,
    0.2039799690246582,
    0.24079608917236328,
    0.24079608917236328,
    0.06438612937927246,
    -0.04606199264526367,
    -0.1764519214630127,
    -0.17184996604919434]
    )
    times.append(factor([1,2,3,4,5,6,7,8],f))

    names.append('LElbowRoll')
    angles.append(
    [-0.1748340129852295,
    -0.2868161201477051,
    -0.477031946182251,
    -0.6396360397338867,
    -0.8866100311279297,
    -1.0967681407928467,
    -1.0937001705169678,
    -0.9617760181427002,
    -0.7822980880737305]
    )
    times.append(factor([.88,1.77,2.66,3.55,4.44,5.33,6.22,7.11,8.00],f))


    names.append('RShoulderPitch')
    angles.append(
    [1.458876132965088,
    1.1520757675170898,
    0.8897619247436523,
    0.6596620082855225,
    0.48018407821655273,
    0.3298518657684326,
    0.3344540596008301,
    0.33905601501464844]
    )
    times.append(factor([1,2,3,4,5,6,7,8],f))

    names.append('RShoulderRoll')
    angles.append(
    [-0.18872404098510742,
    -0.44950389862060547,
    -0.5185339450836182,
    -0.5231359004974365,
    -0.5384759902954102,
    -0.5752918720245361]
    )
    times.append(factor([1.33,2.66,4,5.33,6.66,8],f))

    names.append('RElbowRoll')
    angles.append(
    [0.07060599327087402,
    0.3636000156402588,
    0.6443219184875488,
    0.7670419216156006,
    0.9603261947631836,
    1.1980957984924316]
    )
    times.append(factor([1.33,2.66,4,5.33,6.66,8],f))

    motion.angleInterpolation(names, angles, times, True)

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
    0.3467259407043457,
    0.556,
    0.808,
    1.076]
    )
    times.append(factor([1,2,3,4,5,6,7], f))

    names.append('RShoulderRoll')
    angles.append(
    [-0.5752918720245361,
    -1.30]
    )
    times.append(factor([1.05,3],f))

    motion.angleInterpolation(names, angles, times, True)
    config.poseInit(motion)
#    config.stiffnessOff(motion)

