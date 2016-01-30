#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test script for TechDraw module
# creates a page and 1 section view
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

templateFileSpec = '/home/cheinz/freecad-draw2-build/data/Mod/Drawing/Templates/A4_Landscape.svg'

print("section test started")
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()

view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSection','Section')
rc = page.addView(view)

view.Source = box
view.Direction = (0.0,0.0,1.0)
view.X = 10.0
view.Y = 10.0
view.Scale = 1.0
view.Rotation = 0.0
view.SectionOrigin = (0.0,0.0,1.0)

FreeCAD.ActiveDocument.recompute()

print("section test ended")
