#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test script for TechDraw module
# creates a Box and a Sphere and makes a Fusions from them
# creates a page
# creates a Projection Group
# adds Front,Left,Top projections to the group
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

templateFileSpec = '/home/cheinz/freecad-draw2-build/data/Mod/Drawing/Templates/A4_Landscape.svg'

print("projection group test started")
#make Fusion feature
box = FreeCAD.ActiveDocument.addObject("Part::Box","Box")
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere")
fusion = FreeCAD.ActiveDocument.addObject("Part::MultiFuse","Fusion")
FreeCAD.ActiveDocument.Fusion.Shapes = [box,sphere]

#make a page
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()

#make projection group
group = FreeCAD.ActiveDocument.addObject('TechDraw::DrawProjGroup','cView')
group.Source = fusion
anchorView = group.addProjection("Front")
group.Anchor = anchorView
page.addView(group)
leftView = group.addProjection("Left")
rightView = group.addProjection("Top")

#remove a view from projection group
iv = group.removeProjection("Left")

#test getItemByLabel method
label = "Top"
item = group.getItemByLabel(label)
print("Item Label: " + label + " Item Name: " + item.Name)

##need to run something here to get views to claim children.
group.X = group.X + 10
FreeCAD.ActiveDocument.recompute()

print("projection group test ended")
