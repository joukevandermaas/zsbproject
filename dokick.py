'''
Nao Goal Kick

Wessel Klijnsma - 10172432 
Marysia Winkels - 10163727 
Koen Keune - 10003527 
Jouke van der Maas - 10186883

**dokick.py**
Performs all movements needed to do a kick. Run right after standup.py. 
You will be prompted to give the robot the ball.

'''

import kickmotions
import config
tts = config.loadProxy("ALTextToSpeech")


kickmotions.liftArms()
tts.say("Ball please.")
raw_input('Druk op enter als de bal vast zit.')
kickmotions.positionLeftLeg()
kickmotions.positionRightLeg()
kickmotions.kick()
