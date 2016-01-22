#!/usr/bin/env python
# -*- coding: utf-8 -*-

# annotation & symbol test script for TechDraw module
# creates a page, 1 annotation and import 1 symbol
# assumes an active empty document to start
from __future__ import print_function

import FreeCAD
import Part
import Measure
import TechDraw

templateFileSpec = '/home/cheinz/freecad-draw2-build/data/Mod/Drawing/Templates/A4_Landscape.svg'
symbolFileSpec = '/home/cheinz/Documents/CAD/DrawingModule/TestSymbol.svg'

print("Annotation and Symbol test started")

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()

#annotation
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.X = 50.0
anno.Y = 50.0
s = 'Different Text'
sl = list()
sl.append(s)
anno.Text = sl
rc = page.addView(anno)

#symbol
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)

FreeCAD.ActiveDocument.recompute()

print("Annotation and Symbol test ended")
