#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test script for TechDraw module
# creates a page and 2 views
# creates a DrawClip
# adds 2 views to Clip
# removes 1 view from Clip
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

import os
path = os.path.dirname(os.path.abspath(__file__))
print ('path: ' + path)
templateFileSpec = path+'/A4_LandscapeTD.svg'

print("clip test started")
#make source feature
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere")

#make a page
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()

#make Views
view1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
FreeCAD.ActiveDocument.View.Source = App.ActiveDocument.Box
rc = page.addView(view1)
view2 = FreeCAD.activeDocument().addObject('TechDraw::DrawViewPart','View001')
FreeCAD.activeDocument().View001.Source = App.activeDocument().Sphere
rc = page.addView(view2)
FreeCAD.ActiveDocument.recompute()

#make Clip
clip = FreeCAD.activeDocument().addObject('TechDraw::DrawViewClip','Clip')
FreeCAD.activeDocument().Clip.ShowFrame = True
FreeCAD.activeDocument().Clip.Height = 30.0
FreeCAD.activeDocument().Clip.Width = 30.0
FreeCAD.activeDocument().Clip.ShowLabels = False
rc = page.addView(clip)

#add Views to Clip
clip.addView(view1)
clip.addView(view2)

#remove 1 view from Clip
clip.removeView(view1)

print("clip test ended")
