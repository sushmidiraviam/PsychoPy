#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.00), Wed Apr 16 18:05:54 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'Cultural_blockSEAT'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
#github test 
# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb')

# Initialize components for Routine "Intro_picturetask"
Intro_picturetaskClock = core.Clock()
Intro1 = visual.TextStim(win=win, ori=0, name='Intro1',
    text='Welcome to the face/place task. \r\n\r\n\tYou will see a task cue \r\n\t followed by a picture. \r\n\r\n    Press any key to continue\r\n',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Intro2"
Intro2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='All the pictures will be a face \r\n  superimposed on a place.',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Intro3"
Intro3Clock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='For an "Indoor/Outdoor?" task cue, your task is to focus\r\n on the place in the superimposed picture and determine\r\n\t\t\t\t\t\twhether it is \r\n\t\t\t\tan indoor or outdoor scene.\r\n\r\n\t\t\tPress the "2" key for an indoor scene\r\n\t\t\tand the "3" key for an outdoor scene.\r\n\r\n\r\n\r\n\t\t\t\tpress any key to continue\t',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Intro4"
Intro4Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='For a "Male/Female?" task cue, your task is to focus on\r\n    the face in the superimposed picture and determine\r\n\t\t\t\t\t   whether it is\r\n\t\t\t\t       male or female.\r\n\r\n\t\t\tPress the "2" key for a male face\r\n\t\t\tand the "3" key for a female face. \r\n\r\n\r\n\t\t\t\tpress any key to continue\t',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Intro5"
Intro5Clock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='For a "Like/Dislike?" task cue, your task is to focus on \r\n     the face in the superimposed picture and determine\r\n\t\t\t\t\t\twhether you\r\n\t\t\t\t      like it or dislike it.\r\n\r\n\t\t     Press the "2" key if you like it\r\n\t\t     and the "3" key if you dislike it. \r\n\r\n\r\n\r\n\t\t\t   press any key to continue\r\n\r\n',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "intro6"
intro6Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='You can answer anytime during or soon after the picture\r\n\t\t\t\t\t\tdisplay. \r\n\r\n\r\n\t\t\t     Please answer as quickly\r\n\t\t\t     and accurately as possible.\r\n\r\n\r\n\r\n\t\t\t     press any key to continue',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "intro6_1"
intro6_1Clock = core.Clock()
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text='There will be a practice block before the actual task begins. \r\n\r\n\r\n\r\n             Press any key to begin the practice block',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=2.0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "intro6_9"
intro6_9Clock = core.Clock()
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='The practice block is now over\r\n\r\n\r\n\r\n    Press any key to continue',    font='Courier New Bold',
    pos=[0, 0], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press "x" to start the task',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press "x" to start the task',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press "x" to start the task',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "L_D"
L_DClock = core.Clock()
LikeDislike_cue = visual.TextStim(win=win, ori=0, name='LikeDislike_cue',
    text='Like(2)/Dislike(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "I_O"
I_OClock = core.Clock()
InOut_cue = visual.TextStim(win=win, ori=0, name='InOut_cue',
    text='Indoor(2)/Outdoor(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "M_F"
M_FClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Male(2)/Female(3)?',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1, 1.34],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
Imagetaskcue = visual.TextStim(win=win, ori=0, name='Imagetaskcue',
    text='nonsense',    font='Courier New Bold',
    pos=[0, -.8], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='+',    font='Courier New Bold',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='The task is over. ',    font='Courier New Bold',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Intro_picturetask"-------
t = 0
Intro_picturetaskClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
Intro_picturetaskComponents = []
Intro_picturetaskComponents.append(Intro1)
Intro_picturetaskComponents.append(key_resp_3)
for thisComponent in Intro_picturetaskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro_picturetask"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intro_picturetaskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro1* updates
    if t >= 0.0 and Intro1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro1.tStart = t  # underestimates by a little under one frame
        Intro1.frameNStart = frameN  # exact frame index
        Intro1.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_picturetaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro_picturetask"-------
for thisComponent in Intro_picturetaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Intro2"-------
t = 0
Intro2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
Intro2Components = []
Intro2Components.append(text)
Intro2Components.append(key_resp_5)
for thisComponent in Intro2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intro2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro2"-------
for thisComponent in Intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Intro3"-------
t = 0
Intro3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
Intro3Components = []
Intro3Components.append(text_5)
Intro3Components.append(key_resp_7)
for thisComponent in Intro3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intro3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro3"-------
for thisComponent in Intro3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Intro4"-------
t = 0
Intro4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_8.status = NOT_STARTED
# keep track of which components have finished
Intro4Components = []
Intro4Components.append(text_6)
Intro4Components.append(key_resp_8)
for thisComponent in Intro4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intro4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # underestimates by a little under one frame
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        key_resp_8.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro4"-------
for thisComponent in Intro4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Intro5"-------
t = 0
Intro5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
# keep track of which components have finished
Intro5Components = []
Intro5Components.append(text_7)
Intro5Components.append(key_resp_9)
for thisComponent in Intro5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Intro5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        key_resp_9.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro5"-------
for thisComponent in Intro5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "intro6"-------
t = 0
intro6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
intro6Components = []
intro6Components.append(text_8)
intro6Components.append(key_resp_10)
for thisComponent in intro6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = intro6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        key_resp_10.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro6"-------
for thisComponent in intro6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "intro6_1"-------
t = 0
intro6_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
intro6_1Components = []
intro6_1Components.append(text_12)
intro6_1Components.append(key_resp_13)
for thisComponent in intro6_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro6_1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = intro6_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        key_resp_13.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro6_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro6_1"-------
for thisComponent in intro6_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\practice.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "intro6_9"-------
t = 0
intro6_9Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_14.status = NOT_STARTED
# keep track of which components have finished
intro6_9Components = []
intro6_9Components.append(text_13)
intro6_9Components.append(key_resp_14)
for thisComponent in intro6_9Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro6_9"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = intro6_9Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # underestimates by a little under one frame
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t  # underestimates by a little under one frame
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        key_resp_14.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_14.keys = theseKeys[-1]  # just the last key pressed
            key_resp_14.rt = key_resp_14.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro6_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro6_9"-------
for thisComponent in intro6_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
readyComponents = []
readyComponents.append(text_10)
readyComponents.append(key_resp_4)
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ready"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['x'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys.extend(theseKeys)  # storing all keys
            key_resp_4.rt.append(key_resp_4.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_AF2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_AsiFear_2.csv'),
    seed=None, name='IO_AF2')
thisExp.addLoop(IO_AF2)  # add the loop to the experiment
thisIO_AF2 = IO_AF2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_AF2.rgb)
if thisIO_AF2 != None:
    for paramName in thisIO_AF2.keys():
        exec(paramName + '= thisIO_AF2.' + paramName)

for thisIO_AF2 in IO_AF2:
    currentLoop = IO_AF2
    # abbreviate parameter names if possible (e.g. rgb = thisIO_AF2.rgb)
    if thisIO_AF2 != None:
        for paramName in thisIO_AF2.keys():
            exec(paramName + '= thisIO_AF2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_AF2 (TrialHandler)
    IO_AF2.addData('response.keys',response.keys)
    IO_AF2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_AF2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_AF2'

# get names of stimulus parameters
if IO_AF2.trialList in ([], [None], None):  params = []
else:  params = IO_AF2.trialList[0].keys()
# save data for this loop
IO_AF2.saveAsExcel(filename + '.xlsx', sheetName='IO_AF2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_AF2.saveAsText(filename + 'IO_AF2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_AN2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_AsiNeu_2.csv'),
    seed=None, name='LD_AN2')
thisExp.addLoop(LD_AN2)  # add the loop to the experiment
thisLD_AN2 = LD_AN2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_AN2.rgb)
if thisLD_AN2 != None:
    for paramName in thisLD_AN2.keys():
        exec(paramName + '= thisLD_AN2.' + paramName)

for thisLD_AN2 in LD_AN2:
    currentLoop = LD_AN2
    # abbreviate parameter names if possible (e.g. rgb = thisLD_AN2.rgb)
    if thisLD_AN2 != None:
        for paramName in thisLD_AN2.keys():
            exec(paramName + '= thisLD_AN2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_AN2 (TrialHandler)
    LD_AN2.addData('response.keys',response.keys)
    LD_AN2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_AN2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_AN2'

# get names of stimulus parameters
if LD_AN2.trialList in ([], [None], None):  params = []
else:  params = LD_AN2.trialList[0].keys()
# save data for this loop
LD_AN2.saveAsExcel(filename + '.xlsx', sheetName='LD_AN2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_AN2.saveAsText(filename + 'LD_AN2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_CN3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_CauNeu_3.csv'),
    seed=None, name='IO_CN3')
thisExp.addLoop(IO_CN3)  # add the loop to the experiment
thisIO_CN3 = IO_CN3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_CN3.rgb)
if thisIO_CN3 != None:
    for paramName in thisIO_CN3.keys():
        exec(paramName + '= thisIO_CN3.' + paramName)

for thisIO_CN3 in IO_CN3:
    currentLoop = IO_CN3
    # abbreviate parameter names if possible (e.g. rgb = thisIO_CN3.rgb)
    if thisIO_CN3 != None:
        for paramName in thisIO_CN3.keys():
            exec(paramName + '= thisIO_CN3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_CN3 (TrialHandler)
    IO_CN3.addData('response.keys',response.keys)
    IO_CN3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_CN3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_CN3'

# get names of stimulus parameters
if IO_CN3.trialList in ([], [None], None):  params = []
else:  params = IO_CN3.trialList[0].keys()
# save data for this loop
IO_CN3.saveAsExcel(filename + '.xlsx', sheetName='IO_CN3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_CN3.saveAsText(filename + 'IO_CN3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_CF1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_CauFear_1.csv'),
    seed=None, name='MF_CF1')
thisExp.addLoop(MF_CF1)  # add the loop to the experiment
thisMF_CF1 = MF_CF1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_CF1.rgb)
if thisMF_CF1 != None:
    for paramName in thisMF_CF1.keys():
        exec(paramName + '= thisMF_CF1.' + paramName)

for thisMF_CF1 in MF_CF1:
    currentLoop = MF_CF1
    # abbreviate parameter names if possible (e.g. rgb = thisMF_CF1.rgb)
    if thisMF_CF1 != None:
        for paramName in thisMF_CF1.keys():
            exec(paramName + '= thisMF_CF1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_CF1 (TrialHandler)
    MF_CF1.addData('response.keys',response.keys)
    MF_CF1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_CF1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_CF1'

# get names of stimulus parameters
if MF_CF1.trialList in ([], [None], None):  params = []
else:  params = MF_CF1.trialList[0].keys()
# save data for this loop
MF_CF1.saveAsExcel(filename + '.xlsx', sheetName='MF_CF1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_CF1.saveAsText(filename + 'MF_CF1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_AF3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_AsiFear_3.csv'),
    seed=None, name='LD_AF3')
thisExp.addLoop(LD_AF3)  # add the loop to the experiment
thisLD_AF3 = LD_AF3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_AF3.rgb)
if thisLD_AF3 != None:
    for paramName in thisLD_AF3.keys():
        exec(paramName + '= thisLD_AF3.' + paramName)

for thisLD_AF3 in LD_AF3:
    currentLoop = LD_AF3
    # abbreviate parameter names if possible (e.g. rgb = thisLD_AF3.rgb)
    if thisLD_AF3 != None:
        for paramName in thisLD_AF3.keys():
            exec(paramName + '= thisLD_AF3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_AF3 (TrialHandler)
    LD_AF3.addData('response.keys',response.keys)
    LD_AF3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_AF3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_AF3'

# get names of stimulus parameters
if LD_AF3.trialList in ([], [None], None):  params = []
else:  params = LD_AF3.trialList[0].keys()
# save data for this loop
LD_AF3.saveAsExcel(filename + '.xlsx', sheetName='LD_AF3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_AF3.saveAsText(filename + 'LD_AF3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_CN1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_CauNeu_1.csv'),
    seed=None, name='MF_CN1')
thisExp.addLoop(MF_CN1)  # add the loop to the experiment
thisMF_CN1 = MF_CN1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_CN1.rgb)
if thisMF_CN1 != None:
    for paramName in thisMF_CN1.keys():
        exec(paramName + '= thisMF_CN1.' + paramName)

for thisMF_CN1 in MF_CN1:
    currentLoop = MF_CN1
    # abbreviate parameter names if possible (e.g. rgb = thisMF_CN1.rgb)
    if thisMF_CN1 != None:
        for paramName in thisMF_CN1.keys():
            exec(paramName + '= thisMF_CN1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_CN1 (TrialHandler)
    MF_CN1.addData('response.keys',response.keys)
    MF_CN1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_CN1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_CN1'

# get names of stimulus parameters
if MF_CN1.trialList in ([], [None], None):  params = []
else:  params = MF_CN1.trialList[0].keys()
# save data for this loop
MF_CN1.saveAsExcel(filename + '.xlsx', sheetName='MF_CN1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_CN1.saveAsText(filename + 'MF_CN1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_CN3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_CauNeu_3.csv'),
    seed=None, name='LD_CN3')
thisExp.addLoop(LD_CN3)  # add the loop to the experiment
thisLD_CN3 = LD_CN3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_CN3.rgb)
if thisLD_CN3 != None:
    for paramName in thisLD_CN3.keys():
        exec(paramName + '= thisLD_CN3.' + paramName)

for thisLD_CN3 in LD_CN3:
    currentLoop = LD_CN3
    # abbreviate parameter names if possible (e.g. rgb = thisLD_CN3.rgb)
    if thisLD_CN3 != None:
        for paramName in thisLD_CN3.keys():
            exec(paramName + '= thisLD_CN3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_CN3 (TrialHandler)
    LD_CN3.addData('response.keys',response.keys)
    LD_CN3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_CN3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_CN3'

# get names of stimulus parameters
if LD_CN3.trialList in ([], [None], None):  params = []
else:  params = LD_CN3.trialList[0].keys()
# save data for this loop
LD_CN3.saveAsExcel(filename + '.xlsx', sheetName='LD_CN3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_CN3.saveAsText(filename + 'LD_CN3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_AN1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_AsiNeu_1.csv'),
    seed=None, name='MF_AN1')
thisExp.addLoop(MF_AN1)  # add the loop to the experiment
thisMF_AN1 = MF_AN1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_AN1.rgb)
if thisMF_AN1 != None:
    for paramName in thisMF_AN1.keys():
        exec(paramName + '= thisMF_AN1.' + paramName)

for thisMF_AN1 in MF_AN1:
    currentLoop = MF_AN1
    # abbreviate parameter names if possible (e.g. rgb = thisMF_AN1.rgb)
    if thisMF_AN1 != None:
        for paramName in thisMF_AN1.keys():
            exec(paramName + '= thisMF_AN1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_AN1 (TrialHandler)
    MF_AN1.addData('response.keys',response.keys)
    MF_AN1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_AN1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_AN1'

# get names of stimulus parameters
if MF_AN1.trialList in ([], [None], None):  params = []
else:  params = MF_AN1.trialList[0].keys()
# save data for this loop
MF_AN1.saveAsExcel(filename + '.xlsx', sheetName='MF_AN1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_AN1.saveAsText(filename + 'MF_AN1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
readyComponents = []
readyComponents.append(text_10)
readyComponents.append(key_resp_4)
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ready"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['x'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys.extend(theseKeys)  # storing all keys
            key_resp_4.rt.append(key_resp_4.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_CF3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_CauFear_3.csv'),
    seed=None, name='IO_CF3')
thisExp.addLoop(IO_CF3)  # add the loop to the experiment
thisIO_CF3 = IO_CF3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_CF3.rgb)
if thisIO_CF3 != None:
    for paramName in thisIO_CF3.keys():
        exec(paramName + '= thisIO_CF3.' + paramName)

for thisIO_CF3 in IO_CF3:
    currentLoop = IO_CF3
    # abbreviate parameter names if possible (e.g. rgb = thisIO_CF3.rgb)
    if thisIO_CF3 != None:
        for paramName in thisIO_CF3.keys():
            exec(paramName + '= thisIO_CF3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_CF3 (TrialHandler)
    IO_CF3.addData('response.keys',response.keys)
    IO_CF3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_CF3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_CF3'

# get names of stimulus parameters
if IO_CF3.trialList in ([], [None], None):  params = []
else:  params = IO_CF3.trialList[0].keys()
# save data for this loop
IO_CF3.saveAsExcel(filename + '.xlsx', sheetName='IO_CF3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_CF3.saveAsText(filename + 'IO_CF3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_CN2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_CauNeu_2.csv'),
    seed=None, name='MF_CN2')
thisExp.addLoop(MF_CN2)  # add the loop to the experiment
thisMF_CN2 = MF_CN2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_CN2.rgb)
if thisMF_CN2 != None:
    for paramName in thisMF_CN2.keys():
        exec(paramName + '= thisMF_CN2.' + paramName)

for thisMF_CN2 in MF_CN2:
    currentLoop = MF_CN2
    # abbreviate parameter names if possible (e.g. rgb = thisMF_CN2.rgb)
    if thisMF_CN2 != None:
        for paramName in thisMF_CN2.keys():
            exec(paramName + '= thisMF_CN2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_CN2 (TrialHandler)
    MF_CN2.addData('response.keys',response.keys)
    MF_CN2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_CN2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_CN2'

# get names of stimulus parameters
if MF_CN2.trialList in ([], [None], None):  params = []
else:  params = MF_CN2.trialList[0].keys()
# save data for this loop
MF_CN2.saveAsExcel(filename + '.xlsx', sheetName='MF_CN2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_CN2.saveAsText(filename + 'MF_CN2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_AN3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_AsiNeu_3.csv'),
    seed=None, name='IO_AN3')
thisExp.addLoop(IO_AN3)  # add the loop to the experiment
thisIO_AN3 = IO_AN3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_AN3.rgb)
if thisIO_AN3 != None:
    for paramName in thisIO_AN3.keys():
        exec(paramName + '= thisIO_AN3.' + paramName)

for thisIO_AN3 in IO_AN3:
    currentLoop = IO_AN3
    # abbreviate parameter names if possible (e.g. rgb = thisIO_AN3.rgb)
    if thisIO_AN3 != None:
        for paramName in thisIO_AN3.keys():
            exec(paramName + '= thisIO_AN3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_AN3 (TrialHandler)
    IO_AN3.addData('response.keys',response.keys)
    IO_AN3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_AN3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_AN3'

# get names of stimulus parameters
if IO_AN3.trialList in ([], [None], None):  params = []
else:  params = IO_AN3.trialList[0].keys()
# save data for this loop
IO_AN3.saveAsExcel(filename + '.xlsx', sheetName='IO_AN3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_AN3.saveAsText(filename + 'IO_AN3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_AF2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_AsiFear_2.csv'),
    seed=None, name='MF_AF2')
thisExp.addLoop(MF_AF2)  # add the loop to the experiment
thisMF_AF2 = MF_AF2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_AF2.rgb)
if thisMF_AF2 != None:
    for paramName in thisMF_AF2.keys():
        exec(paramName + '= thisMF_AF2.' + paramName)

for thisMF_AF2 in MF_AF2:
    currentLoop = MF_AF2
    # abbreviate parameter names if possible (e.g. rgb = thisMF_AF2.rgb)
    if thisMF_AF2 != None:
        for paramName in thisMF_AF2.keys():
            exec(paramName + '= thisMF_AF2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_AF2 (TrialHandler)
    MF_AF2.addData('response.keys',response.keys)
    MF_AF2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_AF2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_AF2'

# get names of stimulus parameters
if MF_AF2.trialList in ([], [None], None):  params = []
else:  params = MF_AF2.trialList[0].keys()
# save data for this loop
MF_AF2.saveAsExcel(filename + '.xlsx', sheetName='MF_AF2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_AF2.saveAsText(filename + 'MF_AF2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_AN1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_AsiNeu_1.csv'),
    seed=None, name='LD_AN1')
thisExp.addLoop(LD_AN1)  # add the loop to the experiment
thisLD_AN1 = LD_AN1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_AN1.rgb)
if thisLD_AN1 != None:
    for paramName in thisLD_AN1.keys():
        exec(paramName + '= thisLD_AN1.' + paramName)

for thisLD_AN1 in LD_AN1:
    currentLoop = LD_AN1
    # abbreviate parameter names if possible (e.g. rgb = thisLD_AN1.rgb)
    if thisLD_AN1 != None:
        for paramName in thisLD_AN1.keys():
            exec(paramName + '= thisLD_AN1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_AN1 (TrialHandler)
    LD_AN1.addData('response.keys',response.keys)
    LD_AN1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_AN1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_AN1'

# get names of stimulus parameters
if LD_AN1.trialList in ([], [None], None):  params = []
else:  params = LD_AN1.trialList[0].keys()
# save data for this loop
LD_AN1.saveAsExcel(filename + '.xlsx', sheetName='LD_AN1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_AN1.saveAsText(filename + 'LD_AN1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_CF2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_CauFear_2.csv'),
    seed=None, name='MF_CF2')
thisExp.addLoop(MF_CF2)  # add the loop to the experiment
thisMF_CF2 = MF_CF2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_CF2.rgb)
if thisMF_CF2 != None:
    for paramName in thisMF_CF2.keys():
        exec(paramName + '= thisMF_CF2.' + paramName)

for thisMF_CF2 in MF_CF2:
    currentLoop = MF_CF2
    # abbreviate parameter names if possible (e.g. rgb = thisMF_CF2.rgb)
    if thisMF_CF2 != None:
        for paramName in thisMF_CF2.keys():
            exec(paramName + '= thisMF_CF2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_CF2 (TrialHandler)
    MF_CF2.addData('response.keys',response.keys)
    MF_CF2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_CF2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_CF2'

# get names of stimulus parameters
if MF_CF2.trialList in ([], [None], None):  params = []
else:  params = MF_CF2.trialList[0].keys()
# save data for this loop
MF_CF2.saveAsExcel(filename + '.xlsx', sheetName='MF_CF2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_CF2.saveAsText(filename + 'MF_CF2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_AF1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_AsiFear_1.csv'),
    seed=None, name='IO_AF1')
thisExp.addLoop(IO_AF1)  # add the loop to the experiment
thisIO_AF1 = IO_AF1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_AF1.rgb)
if thisIO_AF1 != None:
    for paramName in thisIO_AF1.keys():
        exec(paramName + '= thisIO_AF1.' + paramName)

for thisIO_AF1 in IO_AF1:
    currentLoop = IO_AF1
    # abbreviate parameter names if possible (e.g. rgb = thisIO_AF1.rgb)
    if thisIO_AF1 != None:
        for paramName in thisIO_AF1.keys():
            exec(paramName + '= thisIO_AF1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_AF1 (TrialHandler)
    IO_AF1.addData('response.keys',response.keys)
    IO_AF1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_AF1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_AF1'

# get names of stimulus parameters
if IO_AF1.trialList in ([], [None], None):  params = []
else:  params = IO_AF1.trialList[0].keys()
# save data for this loop
IO_AF1.saveAsExcel(filename + '.xlsx', sheetName='IO_AF1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_AF1.saveAsText(filename + 'IO_AF1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_CN2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_CauNeu_2.csv'),
    seed=None, name='LD_CN2')
thisExp.addLoop(LD_CN2)  # add the loop to the experiment
thisLD_CN2 = LD_CN2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_CN2.rgb)
if thisLD_CN2 != None:
    for paramName in thisLD_CN2.keys():
        exec(paramName + '= thisLD_CN2.' + paramName)

for thisLD_CN2 in LD_CN2:
    currentLoop = LD_CN2
    # abbreviate parameter names if possible (e.g. rgb = thisLD_CN2.rgb)
    if thisLD_CN2 != None:
        for paramName in thisLD_CN2.keys():
            exec(paramName + '= thisLD_CN2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_CN2 (TrialHandler)
    LD_CN2.addData('response.keys',response.keys)
    LD_CN2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_CN2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_CN2'

# get names of stimulus parameters
if LD_CN2.trialList in ([], [None], None):  params = []
else:  params = LD_CN2.trialList[0].keys()
# save data for this loop
LD_CN2.saveAsExcel(filename + '.xlsx', sheetName='LD_CN2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_CN2.saveAsText(filename + 'LD_CN2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
readyComponents = []
readyComponents.append(text_10)
readyComponents.append(key_resp_4)
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ready"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['x'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys.extend(theseKeys)  # storing all keys
            key_resp_4.rt.append(key_resp_4.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_CN1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_CauNeu_1.csv'),
    seed=None, name='IO_CN1')
thisExp.addLoop(IO_CN1)  # add the loop to the experiment
thisIO_CN1 = IO_CN1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_CN1.rgb)
if thisIO_CN1 != None:
    for paramName in thisIO_CN1.keys():
        exec(paramName + '= thisIO_CN1.' + paramName)

for thisIO_CN1 in IO_CN1:
    currentLoop = IO_CN1
    # abbreviate parameter names if possible (e.g. rgb = thisIO_CN1.rgb)
    if thisIO_CN1 != None:
        for paramName in thisIO_CN1.keys():
            exec(paramName + '= thisIO_CN1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_CN1 (TrialHandler)
    IO_CN1.addData('response.keys',response.keys)
    IO_CN1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_CN1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_CN1'

# get names of stimulus parameters
if IO_CN1.trialList in ([], [None], None):  params = []
else:  params = IO_CN1.trialList[0].keys()
# save data for this loop
IO_CN1.saveAsExcel(filename + '.xlsx', sheetName='IO_CN1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_CN1.saveAsText(filename + 'IO_CN1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_CF1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_CauFear_1.csv'),
    seed=None, name='LD_CF1')
thisExp.addLoop(LD_CF1)  # add the loop to the experiment
thisLD_CF1 = LD_CF1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_CF1.rgb)
if thisLD_CF1 != None:
    for paramName in thisLD_CF1.keys():
        exec(paramName + '= thisLD_CF1.' + paramName)

for thisLD_CF1 in LD_CF1:
    currentLoop = LD_CF1
    # abbreviate parameter names if possible (e.g. rgb = thisLD_CF1.rgb)
    if thisLD_CF1 != None:
        for paramName in thisLD_CF1.keys():
            exec(paramName + '= thisLD_CF1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_CF1 (TrialHandler)
    LD_CF1.addData('response.keys',response.keys)
    LD_CF1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_CF1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_CF1'

# get names of stimulus parameters
if LD_CF1.trialList in ([], [None], None):  params = []
else:  params = LD_CF1.trialList[0].keys()
# save data for this loop
LD_CF1.saveAsExcel(filename + '.xlsx', sheetName='LD_CF1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_CF1.saveAsText(filename + 'LD_CF1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_AF3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_AsiFear_3.csv'),
    seed=None, name='MF_AF3')
thisExp.addLoop(MF_AF3)  # add the loop to the experiment
thisMF_AF3 = MF_AF3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_AF3.rgb)
if thisMF_AF3 != None:
    for paramName in thisMF_AF3.keys():
        exec(paramName + '= thisMF_AF3.' + paramName)

for thisMF_AF3 in MF_AF3:
    currentLoop = MF_AF3
    # abbreviate parameter names if possible (e.g. rgb = thisMF_AF3.rgb)
    if thisMF_AF3 != None:
        for paramName in thisMF_AF3.keys():
            exec(paramName + '= thisMF_AF3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_AF3 (TrialHandler)
    MF_AF3.addData('response.keys',response.keys)
    MF_AF3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_AF3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_AF3'

# get names of stimulus parameters
if MF_AF3.trialList in ([], [None], None):  params = []
else:  params = MF_AF3.trialList[0].keys()
# save data for this loop
MF_AF3.saveAsExcel(filename + '.xlsx', sheetName='MF_AF3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_AF3.saveAsText(filename + 'MF_AF3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_CF2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_CauFear_2.csv'),
    seed=None, name='IO_CF2')
thisExp.addLoop(IO_CF2)  # add the loop to the experiment
thisIO_CF2 = IO_CF2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_CF2.rgb)
if thisIO_CF2 != None:
    for paramName in thisIO_CF2.keys():
        exec(paramName + '= thisIO_CF2.' + paramName)

for thisIO_CF2 in IO_CF2:
    currentLoop = IO_CF2
    # abbreviate parameter names if possible (e.g. rgb = thisIO_CF2.rgb)
    if thisIO_CF2 != None:
        for paramName in thisIO_CF2.keys():
            exec(paramName + '= thisIO_CF2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_CF2 (TrialHandler)
    IO_CF2.addData('response.keys',response.keys)
    IO_CF2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_CF2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_CF2'

# get names of stimulus parameters
if IO_CF2.trialList in ([], [None], None):  params = []
else:  params = IO_CF2.trialList[0].keys()
# save data for this loop
IO_CF2.saveAsExcel(filename + '.xlsx', sheetName='IO_CF2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_CF2.saveAsText(filename + 'IO_CF2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_AN3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_AsiNeu_3.csv'),
    seed=None, name='MF_AN3')
thisExp.addLoop(MF_AN3)  # add the loop to the experiment
thisMF_AN3 = MF_AN3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_AN3.rgb)
if thisMF_AN3 != None:
    for paramName in thisMF_AN3.keys():
        exec(paramName + '= thisMF_AN3.' + paramName)

for thisMF_AN3 in MF_AN3:
    currentLoop = MF_AN3
    # abbreviate parameter names if possible (e.g. rgb = thisMF_AN3.rgb)
    if thisMF_AN3 != None:
        for paramName in thisMF_AN3.keys():
            exec(paramName + '= thisMF_AN3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_AN3 (TrialHandler)
    MF_AN3.addData('response.keys',response.keys)
    MF_AN3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_AN3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_AN3'

# get names of stimulus parameters
if MF_AN3.trialList in ([], [None], None):  params = []
else:  params = MF_AN3.trialList[0].keys()
# save data for this loop
MF_AN3.saveAsExcel(filename + '.xlsx', sheetName='MF_AN3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_AN3.saveAsText(filename + 'MF_AN3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "L_D"-------
t = 0
L_DClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
L_DComponents = []
L_DComponents.append(LikeDislike_cue)
for thisComponent in L_DComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "L_D"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = L_DClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LikeDislike_cue* updates
    if t >= 0.0 and LikeDislike_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        LikeDislike_cue.tStart = t  # underestimates by a little under one frame
        LikeDislike_cue.frameNStart = frameN  # exact frame index
        LikeDislike_cue.setAutoDraw(True)
    elif LikeDislike_cue.status == STARTED and t >= (0.0 + 2.0):
        LikeDislike_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in L_DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "L_D"-------
for thisComponent in L_DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
LD_AF1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\LD_AsiFear_1.csv'),
    seed=None, name='LD_AF1')
thisExp.addLoop(LD_AF1)  # add the loop to the experiment
thisLD_AF1 = LD_AF1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLD_AF1.rgb)
if thisLD_AF1 != None:
    for paramName in thisLD_AF1.keys():
        exec(paramName + '= thisLD_AF1.' + paramName)

for thisLD_AF1 in LD_AF1:
    currentLoop = LD_AF1
    # abbreviate parameter names if possible (e.g. rgb = thisLD_AF1.rgb)
    if thisLD_AF1 != None:
        for paramName in thisLD_AF1.keys():
            exec(paramName + '= thisLD_AF1.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for LD_AF1 (TrialHandler)
    LD_AF1.addData('response.keys',response.keys)
    LD_AF1.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        LD_AF1.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LD_AF1'

# get names of stimulus parameters
if LD_AF1.trialList in ([], [None], None):  params = []
else:  params = LD_AF1.trialList[0].keys()
# save data for this loop
LD_AF1.saveAsExcel(filename + '.xlsx', sheetName='LD_AF1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
LD_AF1.saveAsText(filename + 'LD_AF1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "I_O"-------
t = 0
I_OClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
I_OComponents = []
I_OComponents.append(InOut_cue)
for thisComponent in I_OComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "I_O"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = I_OClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InOut_cue* updates
    if t >= 0.0 and InOut_cue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InOut_cue.tStart = t  # underestimates by a little under one frame
        InOut_cue.frameNStart = frameN  # exact frame index
        InOut_cue.setAutoDraw(True)
    elif InOut_cue.status == STARTED and t >= (0.0 + 2.0):
        InOut_cue.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in I_OComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "I_O"-------
for thisComponent in I_OComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
IO_AN2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\IO_AsiNeu_2.csv'),
    seed=None, name='IO_AN2')
thisExp.addLoop(IO_AN2)  # add the loop to the experiment
thisIO_AN2 = IO_AN2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIO_AN2.rgb)
if thisIO_AN2 != None:
    for paramName in thisIO_AN2.keys():
        exec(paramName + '= thisIO_AN2.' + paramName)

for thisIO_AN2 in IO_AN2:
    currentLoop = IO_AN2
    # abbreviate parameter names if possible (e.g. rgb = thisIO_AN2.rgb)
    if thisIO_AN2 != None:
        for paramName in thisIO_AN2.keys():
            exec(paramName + '= thisIO_AN2.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for IO_AN2 (TrialHandler)
    IO_AN2.addData('response.keys',response.keys)
    IO_AN2.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        IO_AN2.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'IO_AN2'

# get names of stimulus parameters
if IO_AN2.trialList in ([], [None], None):  params = []
else:  params = IO_AN2.trialList[0].keys()
# save data for this loop
IO_AN2.saveAsExcel(filename + '.xlsx', sheetName='IO_AN2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
IO_AN2.saveAsText(filename + 'IO_AN2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "M_F"-------
t = 0
M_FClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
M_FComponents = []
M_FComponents.append(text_2)
for thisComponent in M_FComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "M_F"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = M_FClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 2.0):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in M_FComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "M_F"-------
for thisComponent in M_FComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
MF_CF3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('..\\Conditions\\MF_CauFear_3.csv'),
    seed=None, name='MF_CF3')
thisExp.addLoop(MF_CF3)  # add the loop to the experiment
thisMF_CF3 = MF_CF3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMF_CF3.rgb)
if thisMF_CF3 != None:
    for paramName in thisMF_CF3.keys():
        exec(paramName + '= thisMF_CF3.' + paramName)

for thisMF_CF3 in MF_CF3:
    currentLoop = MF_CF3
    # abbreviate parameter names if possible (e.g. rgb = thisMF_CF3.rgb)
    if thisMF_CF3 != None:
        for paramName in thisMF_CF3.keys():
            exec(paramName + '= thisMF_CF3.' + paramName)
    
    #------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image.setImage(Image)
    Imagetaskcue.setText(TaskCue)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    blockComponents = []
    blockComponents.append(fix)
    blockComponents.append(image)
    blockComponents.append(Imagetaskcue)
    blockComponents.append(response)
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        elif fix.status == STARTED and t >= (0.0 + 0.5):
            fix.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0.5 + 1.5):
            image.setAutoDraw(False)
        
        # *Imagetaskcue* updates
        if t >= 0.5 and Imagetaskcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Imagetaskcue.tStart = t  # underestimates by a little under one frame
            Imagetaskcue.frameNStart = frameN  # exact frame index
            Imagetaskcue.setAutoDraw(True)
        elif Imagetaskcue.status == STARTED and t >= (0.5 + 1.5):
            Imagetaskcue.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        elif response.status == STARTED and t >= (0.5 + 2.0):
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['down', 'pagedown'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(CorrectRes)): response.corr = 1
                    else: response.corr=0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(response.keys) == 0:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(CorrectRes).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for MF_CF3 (TrialHandler)
    MF_CF3.addData('response.keys',response.keys)
    MF_CF3.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        MF_CF3.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'MF_CF3'

# get names of stimulus parameters
if MF_CF3.trialList in ([], [None], None):  params = []
else:  params = MF_CF3.trialList[0].keys()
# save data for this loop
MF_CF3.saveAsExcel(filename + '.xlsx', sheetName='MF_CF3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
MF_CF3.saveAsText(filename + 'MF_CF3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_3)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 5.0):
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_9)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    elif text_9.status == STARTED and t >= (0.0 + 1.0):
        text_9.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
