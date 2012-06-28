import config

def factor(list, f):
    return [f*x for x in list]

motion = config.loadProxy("ALMotion")

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


#names.append('LHipYawPitch')
#angles.append(
#[0.10454400062561035]
#)
#times.append(factor([5.4], f))

motion.angleInterpolation(names, angles, times, True)

