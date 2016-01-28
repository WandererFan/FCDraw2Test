#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test script for TechDraw module
# creates a page and 1 views
# adds a hatch area to view1
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

templateFileSpec = '/home/cheinz/freecad-draw2-build/data/Mod/Drawing/Templates/A4_Landscape.svg'
hatchFileSpec = ''

print("hatch test started")
#make source feature
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")

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
FreeCAD.ActiveDocument.recompute()

#make hatch
print("making hatch")
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.PartView = view1
objs = list()
objs.append((view1,"Edge0"))
objs.append((view1,"Edge1"))
objs.append((view1,"Edge2"))
objs.append((view1,"Edge3"))
hatch.Edges = objs
#hatch.HatchPattern = hatchFileSpec          #comment out to use default from preferences
print("adding hatch to page")
rc = page.addView(hatch)
print("finished hatch")

##need to run something here to get views to claim children.
view1.X = view1.X + 10
FreeCAD.ActiveDocument.recompute()

print("hatch test ended")
