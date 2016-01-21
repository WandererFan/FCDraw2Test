#!/usr/bin/env python
# -*- coding: utf-8 -*-

# basic test script for TechDraw module
# creates a page and 1 view
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

templateFileSpec = '/home/cheinz/freecad-draw2-build/data/Mod/Drawing/Templates/A4_Landscape.svg'

print("basic test started")
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()

view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)

# need another Py command here to add View to Page
FreeCAD.ActiveDocument.View.Source = App.ActiveDocument.Box
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
FreeCAD.ActiveDocument.View.X = 10.0
FreeCAD.ActiveDocument.View.Y = 10.0
FreeCAD.ActiveDocument.View.Scale = 1.0
FreeCAD.ActiveDocument.View.Rotation = 0.0
FreeCAD.ActiveDocument.recompute()

print("basic test ended")
