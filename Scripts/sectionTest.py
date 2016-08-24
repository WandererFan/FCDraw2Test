#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test script for TechDraw module
# creates a page, 1 view and 1 section view
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

import os
path = os.path.dirname(os.path.abspath(__file__))
templateFileSpec = path+'/A4_LandscapeTD.svg'

print("section test started")
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()


view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)
view.Scale = 1.0
view.Rotation = 0.0

section = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)


FreeCAD.ActiveDocument.recompute()

print("section test ended")
