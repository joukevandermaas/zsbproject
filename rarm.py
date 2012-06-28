import config

motion = config.loadProxy("ALMotion")
config.stiffnessOn(motion)
motion.setAngles(["RElbowPitch", "RElbowYaw"],
                 [1.3330879211425781, 1.2655080556869507],
                 .5)
