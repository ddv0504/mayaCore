import os
import sys
import time
import datetime
import maya.cmds as cmds

class mayaInfo:
    
    info = {}
    version = cmds.about(v=True,q=True)

    def __init__(self):

        self.userName = os.getenv("USERNAME")
        self.minTime  = cmds.playbackOptions(min=True,q=True)
        self.maxTime  = cmds.playbackOptions(max=True,q=True)
    
    def currentDate(self):

        date     = datetime.datetime.now ().strftime("%Y/%m/%d")  # %H:%M

        return date    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def frameRate(self,rate):

        if rate == "game":

            return 15

        elif rate =="film":

            return 24

        elif rate =="pal":

            return 25

        elif rate =="ntsc":

            return 30

        elif rate =="show":

            return 48

        elif rate =="palf":
    
            return 50

        elif rate =="ntscf":

            return 60


        