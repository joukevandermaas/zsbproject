import config
import robocupmotion

mp = config.loadProxy("ALMotion")

print mp.getRobotConfig()
