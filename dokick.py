# **dokick.py**
#Performs all movements needed to do a kick. Run right after standup.py. 
#You will be prompted to give the robot the ball.
#Written by Jouke van der Maas, Koen Keune, Marysia Winkels, Wessel Klijnsma

import kickmotions
import config
tts = config.loadProxy("ALTextToSpeech")


kickmotions.liftArms()
tts.say("Ball please.")
raw_input('Druk op enter als de bal vast zit.')
kickmotions.positionLeftLeg()
kickmotions.positionRightLeg()
kickmotions.kick()
