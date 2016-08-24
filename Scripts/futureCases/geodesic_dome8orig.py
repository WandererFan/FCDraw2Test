# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geodesic_dialog4.ui'
#
# Created: Sat Jan 31 19:05:50 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

########################################################################
# Copyright (c)2015 Ulrich Brammer <ulrich1a[at]users.sourceforge.net> #
#                                                                      #
# This file is a supplement to the FreeCAD CAx development system.     #
#                                                                      #
# This program is free software; you can redistribute it and/or modify #
# it under the terms of the GNU Lesser General Public License (LGPL)   #
# as published by the Free Software Foundation; either version 2 of    #
# the License, or (at your option) any later version.                  #
# for detail see the LICENCE text file.                                #
#                                                                      #
# This software is distributed in the hope that it will be useful,     #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU Library General Public License for more details.                 #
#                                                                      #
# You should have received a copy of the GNU Library General Public    #
# License along with this macro; if not, write to the Free Software    #
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 #
# USA                                                                  #
#                                                                      #
########################################################################

from PySide import QtCore, QtGui
import FreeCAD, FreeCADGui, math, Part, DraftVecUtils
from FreeCAD import Base
from collections import Counter

class Ui_Dialog(object):
  def setupUi(self, Dialog):
    Dialog.setObjectName("Dialog")
    Dialog.resize(550, 367)
    self.dia = Dialog
    FCUi = FreeCADGui.UiLoader()
    self.triangles = 75
    self.nodes = 46
    self.edges = 120
    
    self.gridLayoutWidget = QtGui.QWidget(Dialog)
    self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 508, 325))
    self.gridLayoutWidget.setObjectName("gridLayoutWidget")
    self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
    self.gridLayout.setContentsMargins(0, 0, 0, 0)
    self.gridLayout.setObjectName("gridLayout")
    self.domeInfo1 = QtGui.QLabel(self.gridLayoutWidget)
    self.domeInfo1.setObjectName("domeInfo1")
    self.domeInfo1.setText(u'26 Nodes')
    
    self.gridLayout.addWidget(self.domeInfo1, 10, 0, 1, 1)
    #self.domeBandsLE = QtGui.QLineEdit(self.gridLayoutWidget)
    self.domeBandsLE = FCUi.createWidget("Gui::UIntSpinBox")
    self.domeBandsLE.setObjectName("domeBandsLE")
    spinBoxOffset = self.domeBandsLE.property('minimum')
    self.domeBandsLE.setProperty('minimum', spinBoxOffset + 1)
    self.domeBandsLE.setProperty('maximum', spinBoxOffset + 30)
    self.domeBandsLE.setProperty('value', spinBoxOffset + 4)
    self.gridLayout.addWidget(self.domeBandsLE, 2, 1, 1, 1)
    self.domeBomCB = QtGui.QCheckBox(self.gridLayoutWidget)
    self.domeBomCB.setObjectName("domeBomCB")
    self.gridLayout.addWidget(self.domeBomCB, 9, 1, 1, 1)
    self.domeShellCB = QtGui.QCheckBox(self.gridLayoutWidget)
    self.domeShellCB.setChecked(True)
    self.domeShellCB.setObjectName("domeShellCB")
    self.gridLayout.addWidget(self.domeShellCB, 4, 0, 1, 1)
    self.flatSegCB = QtGui.QCheckBox(self.gridLayoutWidget)
    self.flatSegCB.setObjectName("flatSegCB")
    self.gridLayout.addWidget(self.flatSegCB, 4, 1, 1, 1)
    #self.domeRadLE = QtGui.QLineEdit(self.gridLayoutWidget)
    self.domeRadLE = FCUi.createWidget("Gui::InputField")
    self.domeRadLE.setObjectName("domeRadLE")
    self.domeRadLE.setProperty("text", "900 mm")
    
    self.gridLayout.addWidget(self.domeRadLE, 0, 1, 1, 1)
    self.domeFrameCB = QtGui.QCheckBox(self.gridLayoutWidget)
    self.domeFrameCB.setEnabled(True)
    self.domeFrameCB.setObjectName("domeFrameCB")
    self.gridLayout.addWidget(self.domeFrameCB, 8, 0, 1, 1)
    self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget)
    self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
    self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
    self.buttonBox.setObjectName("buttonBox")
    self.gridLayout.addWidget(self.buttonBox, 11, 1, 1, 1)
    self.domeRadLab = QtGui.QLabel(self.gridLayoutWidget)
    self.domeRadLab.setObjectName("domeRadLab")
    self.gridLayout.addWidget(self.domeRadLab, 0, 0, 1, 1)
    self.domeFreqLab = QtGui.QLabel(self.gridLayoutWidget)
    self.domeFreqLab.setObjectName("domeFreqLab")
    self.gridLayout.addWidget(self.domeFreqLab, 1, 0, 1, 1)
    self.macroLab = QtGui.QLabel(self.gridLayoutWidget)
    self.macroLab.setObjectName("macroLab")
    self.gridLayout.addWidget(self.macroLab, 11, 0, 1, 1)
    self.domeBandLab = QtGui.QLabel(self.gridLayoutWidget)
    self.domeBandLab.setObjectName("domeBandLab")
    self.gridLayout.addWidget(self.domeBandLab, 2, 0, 1, 1)
    self.domeInfo2 = QtGui.QLabel(self.gridLayoutWidget)
    self.domeInfo2.setObjectName("domeInfo2")
    self.domeInfo2.setText(u'40 Triangles 65 Edges')
    self.gridLayout.addWidget(self.domeInfo2, 10, 1, 1, 1)
    #self.domeFreqLE = QtGui.QLineEdit(self.gridLayoutWidget)
    self.domeFreqLE = FCUi.createWidget("Gui::UIntSpinBox")
    self.domeFreqLE.setObjectName("domeFreqLE")
    self.domeFreqLE.setProperty('minimum', spinBoxOffset + 1)
    self.domeFreqLE.setProperty('maximum', spinBoxOffset + 10)
    self.domeFreqLE.setProperty('value', spinBoxOffset + 3)
    
    self.gridLayout.addWidget(self.domeFreqLE, 1, 1, 1, 1)
    self.strutDrawCB = QtGui.QCheckBox(self.gridLayoutWidget)
    self.strutDrawCB.setObjectName("strutDrawCB")
    self.gridLayout.addWidget(self.strutDrawCB, 9, 0, 1, 1)
    self.strutWidthLab = QtGui.QLabel(self.gridLayoutWidget)
    self.strutWidthLab.setObjectName("strutWidthLab")
    self.gridLayout.addWidget(self.strutWidthLab, 5, 0, 1, 1)
    self.strutHeightLab = QtGui.QLabel(self.gridLayoutWidget)
    self.strutHeightLab.setObjectName("strutHeightLab")
    self.gridLayout.addWidget(self.strutHeightLab, 6, 0, 1, 1)
    #self.strutWidthLE = QtGui.QLineEdit(self.gridLayoutWidget)
    self.strutWidthLE = FCUi.createWidget("Gui::InputField")
    self.strutWidthLE.setObjectName("strutWidthLE")
    self.strutWidthLE.setProperty("text", "40 mm")
    
    self.gridLayout.addWidget(self.strutWidthLE, 5, 1, 1, 1)
    self.strutHeightLE = FCUi.createWidget("Gui::InputField")
    self.strutHeightLE.setObjectName("strutHeightLE")
    self.strutHeightLE.setProperty("text", "60 mm")
    self.gridLayout.addWidget(self.strutHeightLE, 6, 1, 1, 1)
    

    self.retranslateUi(Dialog)
    QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.makeSomething)
    QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.makeNothing)
    QtCore.QObject.connect(self.domeBandsLE, QtCore.SIGNAL("valueChanged(int)"), self.updateInfo)
    QtCore.QObject.connect(self.domeFreqLE, QtCore.SIGNAL("valueChanged(int)"), self.updateInfo)
    QtCore.QMetaObject.connectSlotsByName(Dialog)


  def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Geodesic Dome Creator", None, QtGui.QApplication.UnicodeUTF8))
    #self.domeBomPathLab.setText(QtGui.QApplication.translate("Dialog", "Path for BOM-File", None, QtGui.QApplication.UnicodeUTF8))
    self.domeBomCB.setText(QtGui.QApplication.translate("Dialog", "Make Bill of Materials", None, QtGui.QApplication.UnicodeUTF8))
    self.domeShellCB.setText(QtGui.QApplication.translate("Dialog", "Show Dome Shell", None, QtGui.QApplication.UnicodeUTF8))
    self.flatSegCB.setText(QtGui.QApplication.translate("Dialog", "Show Flat Segment", None, QtGui.QApplication.UnicodeUTF8))
    self.domeFrameCB.setText(QtGui.QApplication.translate("Dialog", "Show Dome Frame", None, QtGui.QApplication.UnicodeUTF8))
    self.domeRadLab.setText(QtGui.QApplication.translate("Dialog", "Dome Radius", None, QtGui.QApplication.UnicodeUTF8))
    self.domeFreqLab.setText(QtGui.QApplication.translate("Dialog", "Frequency Parameter\n"
      "(Integer between 1 to 10)", None, QtGui.QApplication.UnicodeUTF8))
    self.macroLab.setText(QtGui.QApplication.translate("Dialog", "This Macro creates \n"
      "a geodesic dome.\n"
      "X-Y-symmetry-plane\n"
      "for even frequencies", None, QtGui.QApplication.UnicodeUTF8))
    self.domeBandLab.setText(QtGui.QApplication.translate("Dialog", "Dome Bands (3xFrequency\n"
      "Parameter makes a Globe)", None, QtGui.QApplication.UnicodeUTF8))
    self.strutDrawCB.setText(QtGui.QApplication.translate("Dialog", "Make Strut Drawing", None, QtGui.QApplication.UnicodeUTF8))
    self.strutWidthLab.setText(QtGui.QApplication.translate("Dialog", "Strut Width", None, QtGui.QApplication.UnicodeUTF8))
    self.strutHeightLab.setText(QtGui.QApplication.translate("Dialog", "Strut Height", None, QtGui.QApplication.UnicodeUTF8))



  def makeSomething(self):
    print "accepted! Dome radius: ", self.domeRadLE.property("text"), \
      " with Frequency: ", int(self.domeFreqLE.property("text"))

    #doc=App.activeDocument()

    radius = self.domeRadLE.property("text")
    frequency = int(self.domeFreqLE.property("text"))
    myBands = int(self.domeBandsLE.property("text"))
    myStrutH = self.strutHeightLE.property("text")
    myStrutW = self.strutWidthLE.property("text")

    theDome = Dome(radius, frequency, myBands, myStrutH, myStrutW)


    theDome.doShell = self.domeShellCB.isChecked()
    theDome.doFlat = self.flatSegCB.isChecked()
    theDome.doFrame = self.domeFrameCB.isChecked()
    theDome.doStrut = self.strutDrawCB.isChecked()
    theDome.doBom = self.domeBomCB.isChecked()
      
    self.dia.close()
    #self.makeDome(theDome, radius, frequency)
    theDome.makeDome()
    theDome.makeNodes()
    if self.triangles > 360:
      myAnnoScale = 2.0
    elif self.triangles > 120:
      myAnnoScale = 3.0
    else:
      myAnnoScale = 5.0
    

    if theDome.doShell: theDome.showDomeShell()
    if theDome.doFrame: theDome.showDomeFrame()
    if theDome.doFlat or theDome.doStrut: theDome.showFlatSegment()
    if theDome.doStrut:
      frameDrawing = Drawing(theDome.doc, 'Drawing_Frame_Segment')
      drawScale = frameDrawing.calcScale(theDome.flatFrame)
      theSegment = frameDrawing.addView(theDome.flatFrame, drawScale, "Strut segment")
      for strut in theDome.uFoStruts:
        frameDrawing.addAnnotation2(strut.sName, strut.annoPt, theSegment, myAnnoScale)

      strutDrawing = Drawing(theDome.doc, 'Drawing_Strut')
      strutDrawing.addStrutView (theDome)

    if theDome.doBom:
      import Spreadsheet
      if ".py" in Spreadsheet.__file__:
        if ".pyd" in Spreadsheet.__file__:
          theBom = Bom(theDome)
          theBom.fillBom()
        else:
          mw=FreeCADGui.getMainWindow()
          QtGui.QMessageBox.information(mw,"Info","FreeCAD Release version 0.15 needed for the Bill of Material")
      else:
        theBom = Bom(theDome)
        theBom.fillBom()


    theDome.doc.recompute()
    App.Gui.SendMsgToActiveView("ViewFit")
    #self.dia.destroy()
    
    
  def makeNothing(self):
    print "rejected!!"
    self.dia.close()

  def updateInfo(self):

    radius = self.domeRadLE.property("text")
    frequency = int(self.domeFreqLE.property("text"))
    myBands = int(self.domeBandsLE.property("text"))

    # calculating the parameters for makeFreqFaces / info update
    self.nodes = 1

    if myBands < frequency:
      IcutTop = myBands
      IcutMid = 0
      IcutBottom = 0
    else:
      IcutTop = frequency
      if myBands < 2*frequency:
        IcutMid = myBands - frequency
        IcutBottom = 0
      else:
        IcutMid = frequency
        if myBands < 3*frequency:
          IcutBottom = myBands - 2*frequency
        else:
          IcutBottom = frequency
          self.nodes = 2
          
    # calculating the dome info data
    self.triangles = 0
    halfProfileStruts = 0
    self.edges = 0
    for i in range(IcutTop):
      self.triangles = self.triangles + (2*i + 1) *5
      self.nodes = self.nodes + (i + 1) *5
      self.edges = self.edges + (2 + 3*i) * 5
      
    for i in range(IcutMid):
      self.triangles = self.triangles + 2*frequency * 5
      self.nodes = self.nodes + frequency *5
      self.edges = self.edges + (3*frequency) * 5
      
    for i in range(IcutBottom):
      self.triangles = self.triangles + (2*(frequency-1-i)+1) * 5
      self.nodes = self.nodes + ((frequency-1-i)) * 5
      self.edges = self.edges + (3*(frequency-1-i)+1) * 5
      
    print "dome info triangles: ", self.triangles
    print "dome info nodes: ", self.nodes
    print "dome info edges: ", self.edges
    self.domeInfo2.setText(str(self.triangles)+' Triangles '+ \
      str(self.edges) + ' Edges')
    self.domeInfo1.setText(str(self.nodes) + ' Nodes')




class Bom(object):
  ''' Bom is a class to provide a spreadsheet-object for storing
  the bill of material for a geodesic dome made of struts. 
  '''
  def __init__(self, myDome):
    
    #self.doc = myDome.doc
    self.dome = myDome
    self.sheet = self.dome.doc.addObject('Spreadsheet::Sheet','Bill_of_Material')
 
    self.actRow = 2
    self.sheet.set('A'+ str(self.actRow), myDome.domeRadQuant)
    self.sheet.set('B'+ str(self.actRow), 'Radius of the Dome')

    self.actRow += 1
    self.sheet.set('A'+ str(self.actRow), myDome.strutHQuant)
    self.sheet.set('B'+ str(self.actRow), 'H Height of Strutprofile')
    
    self.actRow += 1
    self.sheet.set('A'+ str(self.actRow), '=('+ myDome.strutWQuant+ ')/2')
    self.sheet.set('B'+ str(self.actRow), 'W/2 Half-Width of Strutprofile')

    self.actRow += 2
    self.sheet.set('A'+ str(self.actRow), 'Type of Strut')    
    self.sheet.set('B'+ str(self.actRow), 'Amount Half-Width Profiles')    
    self.sheet.set('C'+ str(self.actRow), 'Strut Length')    
    self.sheet.set('D'+ str(self.actRow), 'Angle Gamma0')    
    self.sheet.set('E'+ str(self.actRow), 'Angle Gamma1')    
    self.sheet.set('F'+ str(self.actRow), 'Angle Beta')    
    self.dome.doc.recompute()

  def addRow(self, strutType, number, strutLen, gam0, gam1):
    self.actRow += 1
    self.sheet.set('A'+ str(self.actRow), str(strutType))    
    self.sheet.set('B'+ str(self.actRow), str(number))    
    self.sheet.set('C'+ str(self.actRow), str(strutLen) + 'mm')    
    self.sheet.set('D'+ str(self.actRow), str(math.degrees(gam0)) + 'deg')    
    self.sheet.set('E'+ str(self.actRow), str(math.degrees(gam1)) + 'deg')    
    self.sheet.set('F'+ str(self.actRow), '=acos(C'+ str(self.actRow) +' /2/A2)')

  def fillBom(self):
    print "fillBom"
    myCounts = dict(self.dome.bomCounts)
    #for myKey in self.dome.strutNames:
    for myKey in myCounts:
      print 'addKey: ', myKey
      self.addRow(self.dome.strutNames[myKey], myCounts[myKey], \
        myKey[0], myKey[1], myKey[2])

class Drawing_node(object):
  ''' Drawing_node is a class to store triangle Face data, needed for
  an unfold process to create a flat representation of those triangles.
  '''
  def __init__(self, tFace = None, normAxis = None):
    self.triFace = tFace  #
    self.strutList = []
    self.children = []
    self.foldEdge = None
    self.parent = None
    self.axis = normAxis



class Drawing(object):
  ''' Class to store the objects for a A3-drawing page'''
  def __init__(self, myDoc, dTitle):
    self.doc = myDoc
    self.Page = self.doc.addObject('Drawing::FeaturePage', dTitle)
    self.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'
    self.usableX = 0
    self.usableY = 0
    self.annoCounter = 1

  def calcScale(self, myObject):
    
    myShape = myObject.Shape
    # Scale calculation
    self.usableX = 380
    self.usableY = 240
    
    rawXScale = self.usableX / myShape.BoundBox.XLength
    rawYScale = self.usableY / myShape.BoundBox.YLength
    if rawXScale < rawYScale:
      rawScale = rawXScale
    else:
      rawScale = rawYScale
    magnitude = math.floor(math.log10(rawScale))
    fineFactor = rawScale/(10**magnitude)
    #print "fineFactor: ", fineFactorY, " YLength: ", myShape.BoundBox.YLength
    if (fineFactor < 1.5):
      fineFactor = 1.0
    else:
      if (fineFactor < 2.5):
        fineFactor = 1.5
      else:
        if (fineFactor < 5.0):
          fineFactor = 2.5
        else:
          if (fineFactor < 7.5):
            fineFactor = 5.0
          else:
            fineFactor = 7.5
    return fineFactor*10**magnitude
    
  def addView(self, myObject, Scale, label):
    myView = self.doc.addObject('Drawing::FeatureViewPart', label)
    myView.Source = myObject
    myView.Direction = (0.0, 0.0, 1.0)
    myView.Scale = Scale
    myShape = myObject.Shape
    myView.X = 20 + self.usableX - (self.usableX - myView.Scale * myShape.BoundBox.XLength) / 2.0
    myView.Y = 5 +  (self.usableY - myView.Scale * myShape.BoundBox.YLength) / 2.0
    self.Page.addObject(myView)
    return myView

  def addStrutView(self, aDome):
    ''' The first Strut of the dome is shown here'''
    
    myView = self.doc.addObject('Drawing::FeatureViewPart', 'Strut_A_top')
    myView.Source = aDome.doc.Strut_A_
    myView.Direction = aDome.nodeDict[(0,0)].strutList[0].proDir
    myShape = aDome.doc.Strut_A_.Shape
    viewAngle = myView.Direction.getAngle(Base.Vector(0,0,1.0))

    # Scale calculation
    self.usableX = 380
    self.usableY = 200
    
    rawXScale = self.usableX / (myShape.BoundBox.XLength / math.cos(viewAngle))
    rawYScale = self.usableY / myShape.BoundBox.YLength
    if rawXScale < rawYScale:
      rawScale = rawXScale
    else:
      rawScale = rawYScale
    magnitude = math.floor(math.log10(rawScale))
    fineFactor = rawScale/(10**magnitude)
    #print "fineFactor: ", fineFactorY, " YLength: ", myShape.BoundBox.YLength
    if (fineFactor < 2.0):
      fineFactor = 1.0
    else:
      if (fineFactor < 5.0):
        fineFactor = 2.0
      else:
        fineFactor = 5.0
    myView.Scale = fineFactor*10**magnitude
    
    angleOffSet = (math.sin(viewAngle)*aDome.domeRad) * myView.Scale
    cosOffSet = ((1.0-math.cos(viewAngle))*aDome.domeRad) * myView.Scale
    print "sinOff: ", angleOffSet, ' cosOff: ', cosOffSet
    
    myView.X = 20 + self.usableX -angleOffSet - \
      (self.usableX - myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle)) / 2.0
    myView.Y = 15 + 150 #+  (self.usableY - myView.Scale * myShape.BoundBox.YLength) / 2.0
    myView.LineWidth = 0.75
    self.Page.addObject(myView)
    
    # Dimension Profile Half-Width
    vec1 = aDome.doc.Strut_A_.Shape.Edge8.Vertex2.Point - \
      aDome.doc.Strut_A_.Shape.Edge8.Vertex1.Point
    vec2 = aDome.doc.Strut_A_.Shape.Vertex1.Point - \
      aDome.doc.Strut_A_.Shape.Edge8.Vertex1.Point
    angleGam1 = vec1.getAngle(vec2)
    dimX1 = myView.X - myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY1 = myView.Y
    dimX2 = myView.X + aDome.strutW / 2.0 / math.tan(angleGam1) * myView.Scale
    dimY2 = myView.Y + aDome.strutW / 2.0 * myView.Scale
    self.addDim(dimX1, dimY1, dimX2, dimY2, -1.0, 0.0, 'W/2')
    
    # Dimension Gamma1
    r = 70.0
    self.addArcDim(dimX1, dimY1, angleGam1, r, '1', 'Gamma1')

    # Dimension Gamma0
    vec1 = aDome.doc.Strut_A_.Shape.Edge8.Vertex1.Point - \
      aDome.doc.Strut_A_.Shape.Edge8.Vertex2.Point
    vec2 = aDome.doc.Strut_A_.Shape.Vertex2.Point - \
      aDome.doc.Strut_A_.Shape.Edge8.Vertex2.Point
    r = 70.0
    dimX1 = myView.X + myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY1 = myView.Y
    angleGam0 = vec1.getAngle(vec2)
    self.addArcDim(dimX1, dimY1, angleGam0, r, '0', 'Gamma0')


    myView2 = self.doc.addObject('Drawing::FeatureViewPart', 'Strut_A_side')
    myView2.Source = aDome.doc.Strut_A_
    myView2.Direction = Base.Vector(0.0, -1.0, 0.0)
    myView2.Rotation = math.degrees(viewAngle)+90.0
    myView2.Scale = myView.Scale
    myView2.LineWidth = 0.75
    #myView2.X = 20 + self.usableX - \
    #  (self.usableX - myView.Scale * myShape.BoundBox.XLength) / 2.0
    myView2.X = myView.X
      
    heightOffSet = aDome.domeRad * myView.Scale
    myView2.Y = 15 + 50 + heightOffSet - cosOffSet
    self.Page.addObject(myView2)

    
    annoTop = self.doc.addObject('Drawing::FeatureView','Anno_Top')
    aX = myView.X
    aY = myView.Y - 5
    tPos = 'center'
    annoTop.ViewResult = self.addSVGText(aX, aY, 'Top-View', tPos)
    self.Page.addObject(annoTop)






    
    annoSide = self.doc.addObject('Drawing::FeatureView','Anno_Side')
    #annoBeta.Text = [unicode('Side-View', 'utf-8')]
    #annoBeta.Scale = 5
    aX = myView.X #- myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    aY = 15 + 50 - 20
    annoSide.ViewResult = self.addSVGText(aX, aY, 'Side-View', tPos)
    self.Page.addObject(annoSide)
    
    # Dimension Profile height
    angleBeta = (math.pi - aDome.doc.Strut_A_.Shape.Edge8.Vertex1.Point.getAngle( \
      aDome.doc.Strut_A_.Shape.Edge8.Vertex2.Point)) / 2.0
    dimX1 = myView.X - myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY1 = 15 + 50
    dimX2 = dimX1 +  aDome.strutH / math.tan(angleBeta) * myView.Scale
    dimY2 = dimY1 + aDome.strutH * myView.Scale
    
    self.addDim(dimX1, dimY1, dimX2, dimY2, -1.0, 0.0, 'H')

    # Dimension Profile Length
    dimX1 = myView.X - myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY1 = 15 + 50
    dimX2 = myView.X + myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY2 = 15 + 50
    self.addDim(dimX1, dimY1, dimX2, dimY2, 0.0, -1.0, 'Length')


    # Dimension Beta
    r = 70.0
    # r = aDome.strutH * myView.Scale * 1.05
    dimX1 = myView.X - myView.Scale * myShape.BoundBox.XLength / math.cos(viewAngle) / 2.0
    dimY1 = 15 + 50
    self.addArcDim(dimX1, dimY1, angleBeta, r, '1', 'Beta')
    




  def addAnnotation(self, theText, anPt, theView, scale = 5.0):
    #print "annoPoint: ", anPt.X, ' ', anPt.Y,' ', anPt.Z, ' View.X: ', theView.X, ' View.Y: ', theView.Y, 'Scale: ', theView.Scale
    
    myAnno = self.doc.addObject('Drawing::FeatureViewAnnotation','Annotation')
    myAnno.Text = [unicode(theText, 'utf-8')]
    myAnno.Scale = scale
    myAnno.X = theView.X + anPt.X * theView.Scale - myAnno.Scale/2.0
    myAnno.Y = theView.Y - anPt.Y * theView.Scale + myAnno.Scale/2.0
    self.Page.addObject(myAnno)


  def addAnnotation2(self, theText, anPt, theView, scale = 5.0):
    #print "annoPoint: ", anPt.X, ' ', anPt.Y,' ', anPt.Z, ' View.X: ', theView.X, ' View.Y: ', theView.Y, 'Scale: ', theView.Scale
    obName = 'Annota' + str(self.annoCounter)
    self.annoCounter += 1
    myAnno = self.doc.addObject('Drawing::FeatureView', obName)
    # myAnno.Text = [unicode(theText, 'utf-8')]
    # myAnno.Scale = scale
    # aX = theView.X + anPt.X * theView.Scale - myAnno.Scale/2.0
    # aY = theView.Y - anPt.Y * theView.Scale + myAnno.Scale/2.0
    aX = theView.X + anPt.X * theView.Scale
    aY = theView.Y - anPt.Y * theView.Scale + myAnno.Scale*1.25
    tPos = 'center'
    myAnno.ViewResult = self.addSVGText(aX, aY, theText, tPos, scale)
    self.Page.addObject(myAnno)



  def addSVGLine(self, x1, y1, x2, y2, arrow = False):
    strokeDef = '" style="stroke:#000000;stroke-width:0.30" />'
    lineSVG = ''    
    lineSVG += '<line x1="' + str(x1) + '" y1="' + str(y1)
    lineSVG += '" x2="' + str(x2) + '" y2="' + str(y2)
    lineSVG += strokeDef
    if arrow:
      # calculate arrow-points sX1, sY1, eX1, eY1, sX2, sY2, eX2, eY2
      lLen = math.sqrt((x2-x1)**2 + (y2-y1)**2)
      lDirX = (x2-x1)/lLen
      lDirY = (y2-y1)/lLen
      aOffX = -lDirY
      aOffY = lDirX
      lDirX *= 3.0
      lDirY *= 3.0

      lineSVG += '<line x1="' + str(x1+lDirX+aOffX) + '" y1="' + str(y1+lDirY+aOffY)
      lineSVG += '" x2="' + str(x1) + '" y2="' + str(y1)
      lineSVG += strokeDef
      lineSVG += '<line x1="' + str(x1+lDirX-aOffX) + '" y1="' + str(y1+lDirY-aOffY)
      lineSVG += '" x2="' + str(x1) + '" y2="' + str(y1)
      lineSVG += strokeDef

      lineSVG += '<line x1="' + str(x2-lDirX+aOffX) + '" y1="' + str(y2-lDirY+aOffY)
      lineSVG += '" x2="' + str(x2) + '" y2="' + str(y2)
      lineSVG += strokeDef
      lineSVG += '<line x1="' + str(x2-lDirX-aOffX) + '" y1="' + str(y2-lDirY-aOffY)
      lineSVG += '" x2="' + str(x2) + '" y2="' + str(y2)
      lineSVG += strokeDef
    return lineSVG


  def addDim(self, x1, y1, x2, y2, dirX, dirY, dimText):
    if dirX < -0.99:
      dx1 = x1 - 5.0
      dx2 = x1 - 5.0
      dy2 = y2
      dy1 = y1
      # projection lines
      p1x1 = x1
      p1y1 = y1
      p1x2 = x1 - 7.0
      p1y2 = y1
      p2x1 = x2
      p2y1 = y2
      p2x2 = x1 - 7.0
      p2y2 = y2
      # text position
      tx1 = x1 - 7
      ty1 = (y1 + y2)/2.0 + 5.0 / 2.0
      tPos = 'end'
    else:
      dx1 = x1
      dx2 = x2
      dy2 = y2 - 5.0
      dy1 = y1 - 5.0
      # projection lines
      p1x1 = x1 
      p1y1 = y1
      p1x2 = x1
      p1y2 = y1 - 7.0
      p2x1 = x2
      p2y1 = y2
      p2x2 = x2
      p2y2 = y2 - 7.0
      # text position
      tx1 = (x1 + x2) / 2.0
      ty1 = y1 - 7.0 
      tPos = 'center'
      
      
    viewDim = self.doc.addObject('Drawing::FeatureView','Dim_'+ dimText)
    viewDim.ViewResult = '<g  >\n'
    viewDim.ViewResult += self.addSVGLine(p1x1, p1y1, p1x2, p1y2, False)
    viewDim.ViewResult += self.addSVGLine(dx1, dy1, dx2, dy2, True)
    viewDim.ViewResult += self.addSVGLine(p2x1, p2y1, p2x2, p2y2, False)
    viewDim.ViewResult += '\n</g>\n'
    viewDim.ViewResult += self.addSVGText(tx1, ty1, dimText, tPos)
    
    self.Page.addObject(viewDim)

 
  def addSVGText(self, x1, y1, theText, theAlign, fSize=None):
    if fSize == None:
      fSize = 5
    if theAlign == 'end':
      tAnchor = 'end'
    elif theAlign == 'center':
      tAnchor = 'middle'
    else:
      tAnchor = 'start'
    textSVG = ''
    textSVG += '<g transform="translate('
    textSVG += str(x1) +',' + str(y1)
    textSVG += ') rotate(0)">\n'
    textSVG += '<text id="' + theText + '"\n'
    textSVG += ' font-family="Sans"\n font-size="'
    textSVG += str(fSize) + '"\n fill="#000000"\n'
    textSVG += ' text-align="' + theAlign
    textSVG += '"\n text-anchor="' + tAnchor + '">'
    # textSVG += '<tspan x="0" dy="1em">'+ theText + '</tspan>\n'
    textSVG += theText + '\n'
    textSVG += '</text>\n</g>\n'
    return textSVG
    
  def addSVGArc(self, x1, y1, x2, y2, r, sweep):
    # x1 and y1 should spezify the coordinates at the horizontal line
    strokeDef = '" style="stroke:#000000;stroke-width:0.30" />'

    arcSVG = ''
    arcSVG += '<path d = "M ' + str(x1) + ' ' + str(y1) + 'A '
    arcSVG += str(r) + ' ' + str(r) + ' 0 0 ' + sweep + ' '
    arcSVG += str(x2) + ' ' + str(y2)
    arcSVG += '" style="stroke:#000000;stroke-width:0.30;fill:none" />'

    arcSVG += '<line x1="' + str(x1-1.0) + '" y1="' + str(y1+3.0)
    arcSVG += '" x2="' + str(x1) + '" y2="' + str(y1)
    arcSVG += strokeDef
    arcSVG += '<line x1="' + str(x1+1.0) + '" y1="' + str(y1+3.0)
    arcSVG += '" x2="' + str(x1) + '" y2="' + str(y1)
    arcSVG += strokeDef
    
    if sweep == '1':
      cx = x1 - r
      cy = y1
      lLen = math.sqrt((x2-cx)**2 + (y2-cy)**2)
      aOffX = (x2-cx)/lLen
      aOffY = (y2-cy)/lLen
      lDirX = -aOffY * 3.0
      lDirY = aOffX * 3.0
    else:
      cx = x1 + r
      cy = y1
      lLen = math.sqrt((x2-cx)**2 + (y2-cy)**2)
      aOffX = (x2-cx)/lLen
      aOffY = (y2-cy)/lLen
      lDirX = aOffY * 3.0
      lDirY = -aOffX * 3.0

    arcSVG += '<line x1="' + str(x2-lDirX+aOffX) + '" y1="' + str(y2-lDirY+aOffY)
    arcSVG += '" x2="' + str(x2) + '" y2="' + str(y2)
    arcSVG += strokeDef
    arcSVG += '<line x1="' + str(x2-lDirX-aOffX) + '" y1="' + str(y2-lDirY-aOffY)
    arcSVG += '" x2="' + str(x2) + '" y2="' + str(y2)
    arcSVG += strokeDef
    return arcSVG
 
  def addArcDim(self, cx, cy, ang, r, sweep, dimText):
    # sweep is SVG-sweep-flag '0' or '1'
    if sweep == '1':
      x1 = cx + r
      x2 = cx + r*math.cos(ang)
      y2 = cy + r*math.sin(ang)
      px2 = cx + (r+2.0)*math.cos(ang)
      py2 = cy + (r+2.0)*math.sin(ang)
      tx1 = cx + (r+4.0)*math.cos(ang * 0.95)
      ty1 = cy + (r+4.0)*math.sin(ang * 0.95)
      tPos = 'start'
    else:
      x1 = cx - r
      x2 = cx - r*math.cos(ang)
      y2 = cy + r*math.sin(ang)
      px2 = cx - (r+2.0)*math.cos(ang)
      py2 = cy + (r+2.0)*math.sin(ang)
      tx1 = cx - (r+4.0)*math.cos(ang * 0.95)
      ty1 = cy + (r+4.0)*math.sin(ang * 0.95)
      tPos = 'end'
      
    viewDim = self.doc.addObject('Drawing::FeatureView','Dim_'+ dimText)
    viewDim.ViewResult = '<g  >\n'
    viewDim.ViewResult += self.addSVGArc(x1, cy, x2, y2, r, sweep)
    viewDim.ViewResult += self.addSVGLine(cx, cy, px2, py2, False)
    viewDim.ViewResult += '\n</g>\n'
    viewDim.ViewResult += self.addSVGText(tx1, ty1, dimText, tPos)
    self.Page.addObject(viewDim)

    
    
    
    
class Strut(object):
  ''' This defines a strut class with a shape, a name and an annotation vertex'''   
  def __init__(self, strutShape, strutName, aPt, pDir):
    self.Shape = strutShape
    self.sName = strutName
    self.annoPt = aPt  # here we can add an annotation to a strut
    self.proDir = pDir # projection Direction for strut Drawing






class Dome(object):
  def __init__(self, domeRad_str, ny, tBands, strH, strW):
    self.domeRad = FreeCAD.Units.parseQuantity(domeRad_str).Value
    self.domeRadQuant = domeRad_str
    print " Dome Radius: ", self.domeRad, " String: ", domeRad_str
    self.ny = ny
    if self.ny == 0:
      self.ny = 1
    self.totalBands = tBands  # Number of rings of triangles making up the dome
    if self.totalBands == 0:
      self.totalBands = 3
    # totalBands >= 3*ny makes a geodesic globe
    self.strutH = FreeCAD.Units.parseQuantity(strH).Value
    self.strutW = FreeCAD.Units.parseQuantity(strW).Value
    self.strutHQuant = strH
    self.strutWQuant = strW
    
    
    # icoAngle: angle of vertices of icosahedron points not a north or south pole
    icoAngle = math.atan(0.5)
    icoLat = self.domeRad * math.sin(icoAngle)
    latRad = self.domeRad * math.cos(icoAngle)
    ang36 = math.radians(36.0)


    # Calculation all points of the icosahedron
    self.icoPts = []
    self.icoPts.append(Base.Vector(0.0, 0.0, self.domeRad))
    
    for i in range(10):
      icoCos = latRad * math.cos(i*ang36 - math.pi / 2.0)
      icoSin = latRad * math.sin(i*ang36 - math.pi / 2.0) 
      if i%2 == 0:
        self.icoPts.append(Base.Vector(icoSin, icoCos, icoLat))
      else:
        self.icoPts.append(Base.Vector(icoSin, icoCos, -icoLat))
    
    self.icoPts.append(Base.Vector(0.0, 0.0, -self.domeRad))
    
    self.domeFaces = []
    self.domeStruts = []
    
    self.nodeDict = {} # Dictionary for the nodes to be unfolded
    # Key = (band, triangle number in band) band starts with 0
      
    
    # calculating the parameter for makeFreqFaces 
    if self.totalBands < self.ny:
      self.cutTop = self.totalBands
      self.cutMid = 0
      self.cutBottom = 0
    else:
      self.cutTop = self.ny
      if self.totalBands < 2*self.ny:
        self.cutMid = self.totalBands - self.ny
        self.cutBottom = 0
      else:
        self.cutMid = self.ny
        if self.totalBands < 3*self.ny:
          self.cutBottom = self.totalBands - 2*self.ny
        else:
          self.cutBottom = self.ny
  
    # setting the special values for ny=3 (David Kruschke partioning)
    # makes a flat bottom for 4 and 5 bands with ny==3
    if self.ny == 3:
      # Calculate the central point for icosahedron triangle 9, 10, 1
      # See ASCI-sketch below
      # is identical to center of incircle of triangle
      firstEdge = self.icoPts[9]-self.icoPts[10]
      secEdge = self.icoPts[10]-self.icoPts[1]
      thirdEdge = self.icoPts[1]-self.icoPts[9]
      sumOfLength = firstEdge.Length + secEdge.Length +  thirdEdge.Length
      cIdSecPt = Base.Vector(self.icoPts[1].x, self.icoPts[1].y, self.icoPts[1].z)
      cIdThirdPt = Base.Vector(self.icoPts[9].x, self.icoPts[9].y, self.icoPts[9].z)
      cIdFirstPt = Base.Vector(self.icoPts[10].x, self.icoPts[10].y, self.icoPts[10].z)
      centerIncircle = cIdSecPt.multiply(firstEdge.Length / sumOfLength) \
        + cIdThirdPt.multiply(secEdge.Length / sumOfLength) \
        + cIdFirstPt.multiply(thirdEdge.Length / sumOfLength)
            
      centerKruschke = centerIncircle.normalize().multiply(self.domeRad)
      angleKruschke = math.sin(centerKruschke.z/self.domeRad)
      partRatio = centerKruschke.z/self.domeRad
  
        
      lamb=(partRatio*math.sqrt(((-self.icoPts[9].y**2-self.icoPts[9].x**2)* \
        self.icoPts[10].z**2+(2*self.icoPts[9].y*self.icoPts[9].z*self.icoPts[10].y+ \
        2*self.icoPts[9].x*self.icoPts[9].z*self.icoPts[10].x)*self.icoPts[10].z+\
        (-self.icoPts[9].z**2-self.icoPts[9].x**2)*self.icoPts[10].y**2+\
        2*self.icoPts[9].x*self.icoPts[9].y*self.icoPts[10].x*self.icoPts[10].y+\
        (-self.icoPts[9].z**2-self.icoPts[9].y**2)*self.icoPts[10].x**2)*partRatio**2+\
        (self.icoPts[9].y**2+self.icoPts[9].x**2)*self.icoPts[10].z**2+\
        (-2*self.icoPts[9].y*self.icoPts[9].z*self.icoPts[10].y-2*self.icoPts[9].x*\
        self.icoPts[9].z*self.icoPts[10].x)*self.icoPts[10].z+self.icoPts[9].z**2*\
        self.icoPts[10].y**2+self.icoPts[9].z**2*self.icoPts[10].x**2)+\
        (-self.icoPts[9].z*self.icoPts[10].z-self.icoPts[9].y*self.icoPts[10].y-\
        self.icoPts[9].x*self.icoPts[10].x+self.icoPts[9].z**2+self.icoPts[9].y**2+\
        self.icoPts[9].x**2)*partRatio**2+self.icoPts[9].z*self.icoPts[10].z-self.icoPts[9].z**2)/\
        ((self.icoPts[10].z**2-2*self.icoPts[9].z*self.icoPts[10].z+self.icoPts[10].y**2-\
        2*self.icoPts[9].y*self.icoPts[10].y+self.icoPts[10].x**2-2*self.icoPts[9].x*\
        self.icoPts[10].x+self.icoPts[9].z**2+self.icoPts[9].y**2+self.icoPts[9].x**2)*\
        partRatio**2-self.icoPts[10].z**2+2*self.icoPts[9].z*self.icoPts[10].z-self.icoPts[9].z**2)  
      # print "lambda: ", lamb
      testPartition = self.icoPts[9] +(self.icoPts[10] - self.icoPts[9]).multiply(lamb)
      testPt = testPartition.normalize().multiply(self.domeRad)
      #print "centerKruschke.z: ", centerKruschke.z, " testPt.z: ", testPt.z
      
      # see formula Kruschke_partition for further developing
      # lambda=(ptz-p1z)/(p2z-p1z)
      lamb2 = (centerIncircle.z - self.icoPts[10].z) \
               /(self.icoPts[9].z - self.icoPts[10].z)
      #print "lambda2: ", lamb2

      self.freq3Dict = {} # Dictionary for the frequency 3 partitioning
      # Key = (growVecIdx, crossVecIdx) used in makeFreqFaces with
      # indices k and l
      # Contains the partition-values for growVec and crossVec
      self.freq3Dict[(0,0)] = (0.0,0.0) # Point 10
      self.freq3Dict[(1,0)] = (lamb,0.0) # Point e
      self.freq3Dict[(1,1)] = (lamb,lamb) # Point f
      self.freq3Dict[(2,0)] = (1.0-lamb,0.0) # Point c
      self.freq3Dict[(2,1)] = (2.0/3.0,1.0/3.0) # Point C
      self.freq3Dict[(2,2)] = (1.0-lamb,1.0-lamb) # Point d
      self.freq3Dict[(3,0)] = (1.0,0.0) # Point 9
      self.freq3Dict[(3,1)] = (1.0,lamb) # Point a
      self.freq3Dict[(3,2)] = (1.0,1.0-lamb) # Point b
      self.freq3Dict[(3,3)] = (1.0,1.0) # Point 1


      # lambda is the partitioning ratio for the points: a, b, c, d, e, f
      # 1, 9, 10 are the indices of the icoPts
      # C is the center-point of the icosahedron-triangle
      #     10 
      #     /\
      #    e-f
      #   /\ /\
      #   c-C -d
      #  / \/\ /\
      # 9--a--b--1
    



    self.doc = App.newDocument("Geodesic_Dome")
    #App.setActiveDocument(self.doc)   
  
    #self.doc=App.activeDocument()
    
    self.doShell = True
    self.doFlat = False
    self.doFrame = False
    self.doStrut = False
    self.doBom = False
    self.uFoStruts = [] # contains the unfolded struts
    self.unFoldedFaces = []
    self.dFlatObject = None # contains later the flattened shell segment
    self.flatFrame = None # doc object of Compound of flattened struts
    self.bomCounts = Counter() # counts the struts of the different types
    self.strutNames = dict()
    self.nameIdx = 1 # counts the types of struts for naming the struts
    self.strutDir = None # Direction of strut projection in strut drawing
    



  def updateBomCounts(self, a, b, c):
    ''' calls the counter for each strut of the dome'''
    myTup = self.makeStrutKey(a, b, c)
    #print "myTup: ", myTup
    self.bomCounts[myTup] += 1
    
    if not (myTup in self.strutNames):
      firstIdx = 0
      secIdx = 0
      if self.nameIdx > 26:
        firstIdx = int(self.nameIdx / 26)
        secIdx = self.nameIdx -  firstIdx*26
        if secIdx == 0:
          secIdx = 26
        sName = chr(firstIdx + 64) + chr(secIdx + 64)
      else:
        sName = chr(self.nameIdx + 64)
      self.strutNames[myTup] = sName
      self.nameIdx += 1
      print "add Name: ", sName, ' secIdx: ', secIdx, ' firstIdx: ', firstIdx

  def makeStrutKey(self, a, b, c):
    myKey = (round(a,6), round(b,6), round(c,6))
    return myKey



  def makeDome(self):
    
    thirdPt = self.icoPts[9]
    for i in range(5):
    #for i in range(1):
      j = i*2+1
      self.makeFreqFaces(self.icoPts[0], thirdPt, self.icoPts[j], self.cutTop)
      thirdPt = self.icoPts[j]
      
    thirdPt = self.icoPts[9]
    secPt = self.icoPts[10]
    for i in range(10):
      j = i+1
      if i%2 == 0:
        self.makeFreqFaces(secPt, self.icoPts[j], thirdPt, -self.cutMid)
      else:  
        self.makeFreqFaces(secPt, thirdPt, self.icoPts[j], self.cutMid)
      thirdPt = secPt  
      secPt = self.icoPts[j]  
    
    thirdPt = self.icoPts[10]
    for i in range(5):
      j = i*2+2
      self.makeFreqFaces(self.icoPts[11], self.icoPts[j], thirdPt, -self.cutBottom)
      thirdPt = self.icoPts[j]

    # Shell of the geodesic dome
    #domeShell = Part.Shell(self.domeFaces)
    # Part.show(domeShell)
      
      
  def showDomeShell(self):
    label = "GeodesicDomeShell"
    self.dObject = self.doc.addObject("Part::Feature",label)
    self.dObject.Shape = Part.Shell(self.domeFaces)
    # self.doc.recompute()
    print "dome real data triangles: ", len(self.domeFaces)
    print "dome real data vertexes: ", len(self.dObject.Shape.Vertexes)
    print "dome real data edges: ", len(self.dObject.Shape.Edges)
    
  def showDomeFrame(self):
    frameGroup = self.doc.addObject("App::DocumentObjectGroup","DomeFrame")
    strutGroups = dict()
    for strut in self.domeStruts:
      if not (strut.sName in strutGroups):
        strutGroups[strut.sName] = self.doc.addObject \
          ("App::DocumentObjectGroup", strut.sName)
        frameGroup.addObject(strutGroups[strut.sName])
      
      strutI = App.ActiveDocument.addObject("Part::Feature","Strut_"+strut.sName+"_")
      strutI.Shape = strut.Shape
      strutGroups[strut.sName].addObject(strutI)
    print "dome real data struts: ", len(self.domeStruts)
                
  def showFlatSegment(self):
    print "Flat called!" 
    fAx = self.icoPts[9] - self.icoPts[1]
    fAn = DraftVecUtils.angle(Base.Vector(0.0, 0.0, 1.0), self.nodeDict[(0,0)].axis, fAx)
    
    if self.doShell:
      print "Flat shell now"
      for rFace in self.unFoldedFaces:
        rFace.rotate(Base.Vector(0.0, 0.0, self.domeRad),fAx,math.degrees(-fAn))
        #Part.show(rFace)
      label = "FlatDomeShell"
      self.dFlatObject = self.doc.addObject("Part::Feature",label)
      self.dFlatObject.Shape = Part.Shell(self.unFoldedFaces)
      
    if self.doFrame:
      print "Flat Frame now"
      #flatGroup = self.doc.addObject("App::DocumentObjectGroup","FlatDomeFrame")
      for rStrut in self.uFoStruts:
        rStrut.Shape.rotate(Base.Vector(0.0, 0.0, self.domeRad),fAx,math.degrees(-fAn))
        rStrut.annoPt.rotate(Base.Vector(0.0, 0.0, self.domeRad),fAx,math.degrees(-fAn))
        #strutI = self.doc.addObject("Part::Feature","FlatStrut")
        #strutI.Shape = rStrut.Shape
        #flatGroup.addObject(strutI)

        #Part.show(rStrut)
        #Part.show(rStrut.annoPt)
      strutShapes = []
      for i in self.uFoStruts:
        strutShapes.append(i.Shape)
      uFoStrutComp = Part.makeCompound(strutShapes)
      self.flatFrame = self.doc.addObject("Part::Feature","FlatFrame")
      self.flatFrame.Shape = uFoStrutComp
    
    #newShell = Part.Shell(unFoldedFaces)
    #Part.show(newShell)



  def makeFreqFaces(self, fPt, sPt, thPt, cutIdx = None, band = None):
    # band <> None: The nodeDict will be filled, in order to unfold
    # the structure later.
    # definition of direction vectors
    # growVec goes from Vertex3 to Vertex2 with index k
    growVec = (sPt - fPt)
    # crossVec goes from Vertex2 to Vertex1 with index l
    crossVec = (thPt - sPt)
    if self.ny <> 3:
      growVec.multiply(1.0/self.ny)
      crossVec.multiply(1.0/self.ny)
  
    # Indexing of triangle vertexes in the loop
    #  4--3
    #  \  | \
    #   \ |  \
    #     2--1
    #
    # The Vertex4 is not used at index l==0
    # firstEdge 1_3
    # secEdge   2_1
    # thirdEdge 2_3
    # fourthEdge 3_4
    # fifthEdge 4_2
    
    if cutIdx == None:
      cutIdx = self.ny
    startK = 0
    endK = cutIdx
    if band <> None:
      bandForm = band # The band formula-value for calc purposes
      kForm = 1
    if cutIdx < 0:
      startK = self.ny + cutIdx
      endK = self.ny
      if band <> None:
        bandForm = band + self.ny -1
        kForm = -1
  
    for k in range(startK, endK):
      if self.ny <> 3:
        kThirdPt = fPt + growVec * (k+0.0)
        kSecPt = fPt + growVec * (k+1.0)
      else:
        kThirdPt = fPt + growVec * self.freq3Dict[(k,0)][0]
        kSecPt = fPt + growVec * self.freq3Dict[(k+1,0)][0]
  
      for l in range(k+1):
        if band <> None:
          numberForm = 0
          if band == self.ny:
            numberForm = (2*self.ny) - (2*k +1)
          lForm = 2
          lOff = -1
          if cutIdx < 0:
            numberForm = 2*k
            lForm = -2
            lOff = 1
            
        if self.ny <> 3:  
          firstPt = kSecPt + crossVec *(l+1.0)
          secPt = kSecPt + crossVec *(l+0.0)
          thirdPt = kThirdPt + crossVec *(l+0.0)
        else:
          firstPt = fPt + growVec * self.freq3Dict[(k+1,l+1)][0] + crossVec * self.freq3Dict[(k+1,l+1)][1]
          secPt = fPt + growVec * self.freq3Dict[(k+1,l)][0] + crossVec *self.freq3Dict[(k+1,l)][1]
          thirdPt = fPt + growVec * self.freq3Dict[(k,l)][0] + crossVec *self.freq3Dict[(k,l)][1]

        dSecPt =secPt.normalize().multiply(self.domeRad)
        dFirstPt = firstPt.normalize().multiply(self.domeRad)
        dThirdPt = thirdPt.normalize().multiply(self.domeRad)
        thirdEdge = Part.makeLine(dSecPt, dThirdPt)
        # Part.show(thirdEdge)
  
        if l > 0:
          fourthEdge = Part.makeLine(dThirdPt,dFourthPt)
          triWire = Part.Wire([thirdEdge, fourthEdge, fifthEdge])
          # Part.show(triWire)
          triFace = Part.Face(triWire)
          self.domeFaces.append(triFace)
          #Part.show(triFace)
          triNorm = (dSecPt - dThirdPt).cross(dFourthPt - dThirdPt)
          triNorm.normalize().multiply(self.domeRad/2.0)
          #Normtest = Part.makeLine(dThirdPt, dThirdPt + triNorm)
          #Part.show(Normtest)
          
          # angles of the triangle face
          fourthGamma = self.getPtsAngle(dThirdPt, dFourthPt, dSecPt) / 2.0
          secGamma = self.getPtsAngle(dFourthPt, dSecPt, dThirdPt) / 2.0  
          thirdGamma = self.getPtsAngle(dSecPt, dThirdPt, dFourthPt) / 2.0
          #print "Sum of angles: ", math.degrees(fourthGamma + secGamma + thirdGamma)
          
          # center of incircle
          sumOfLength = thirdEdge.Length + fourthEdge.Length +  fifthEdge.Length
          cIdSecPt = Base.Vector(dSecPt.x, dSecPt.y, dSecPt.z)
          cIdThirdPt = Base.Vector(dThirdPt.x, dThirdPt.y, dThirdPt.z)
          cIdFourthPt = Base.Vector(dFourthPt.x, dFourthPt.y, dFourthPt.z)
          centerIncircle = cIdSecPt.multiply(fourthEdge.Length / sumOfLength) \
            + cIdThirdPt.multiply(fifthEdge.Length / sumOfLength) \
            + cIdFourthPt.multiply(thirdEdge.Length / sumOfLength)
          
          
          if band<>None:
            nodeBand = bandForm + k * kForm
            nodeNumber = numberForm + lForm*l + lOff
            self.nodeDict[(nodeBand, nodeNumber)] = Drawing_node(triFace.copy(), triNorm)
            #Part.show(triFace)
            #print "i,j: ",nodeBand, " ", nodeNumber
            dMode = True # make struts for the drawing
  
            strut1 = self.makePriStrut(fifthEdge, \
              triNorm, fourthGamma, secGamma, False, dMode, centerIncircle)
            strut2 = self.makePriStrut(fourthEdge, \
              triNorm, thirdGamma, fourthGamma, True, dMode, centerIncircle)
            strut3 = self.makePriStrut(thirdEdge, \
              triNorm, secGamma, thirdGamma, True, dMode, centerIncircle)
            self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut1)
            self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut2)
            self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut3)
          else:
            dMode = False # make struts for the 3D-frame
            self.updateBomCounts(fifthEdge.Length, fourthGamma, secGamma)
            strut1 = self.makePriStrut(fifthEdge, \
              triNorm, fourthGamma, secGamma, False, dMode, centerIncircle)
            self.updateBomCounts(fourthEdge.Length, thirdGamma, fourthGamma)
            strut2 = self.makePriStrut(fourthEdge, \
              triNorm, thirdGamma, fourthGamma, True, dMode, centerIncircle)
            self.updateBomCounts(thirdEdge.Length, secGamma, thirdGamma)
            strut3 = self.makePriStrut(thirdEdge, \
              triNorm, secGamma, thirdGamma, True, dMode, centerIncircle)
            self.domeStruts.append(strut1)
            self.domeStruts.append(strut2)
            self.domeStruts.append(strut3)
            #Part.show(strut1)
            #Part.show(strut2)
            #Part.show(strut3)
  
          
        dFourthPt = dThirdPt
        doFirstPt = dFirstPt
        firstEdge = Part.makeLine(dFirstPt, dThirdPt)
        fifthEdge = firstEdge
        secEdge = Part.makeLine(dSecPt, dFirstPt)
        triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
        triFace = Part.Face(triWire)
        self.domeFaces.append(triFace)
        #Part.show(triFace)
  
        triNorm = (dSecPt - dFirstPt).cross(dThirdPt - dFirstPt)
        triNorm.normalize().multiply(self.domeRad/3.0)
        #Normtest = Part.makeLine(dFirstPt, dFirstPt + triNorm)
        #Part.show(Normtest)
        
        # angles of the triangle face
        firstGamma = self.getPtsAngle(dThirdPt, dFirstPt, dSecPt) / 2.0
        #print "FirstGamma: ", math.degrees(firstGamma)
        secGamma = self.getPtsAngle(dFirstPt, dSecPt, dThirdPt) / 2.0  
        thirdGamma = self.getPtsAngle(dSecPt, dThirdPt, dFirstPt) / 2.0

        # center of incircle
        sumOfLength = firstEdge.Length + secEdge.Length +  thirdEdge.Length
        cIdSecPt = Base.Vector(dSecPt.x, dSecPt.y, dSecPt.z)
        cIdThirdPt = Base.Vector(dThirdPt.x, dThirdPt.y, dThirdPt.z)
        cIdFirstPt = Base.Vector(dFirstPt.x, dFirstPt.y, dFirstPt.z)
        centerIncircle = cIdSecPt.multiply(firstEdge.Length / sumOfLength) \
          + cIdThirdPt.multiply(secEdge.Length / sumOfLength) \
          + cIdFirstPt.multiply(thirdEdge.Length / sumOfLength)
        #print 'centerIC: ', centerIncircle, ' sumL: ', sumOfLength
        
        if band<>None:
          #Part.show(Part.Vertex(centerIncircle.x, centerIncircle.y, centerIncircle.z))
          nodeBand = bandForm + k * kForm
          #nodeNumber = 2*l
          nodeNumber = numberForm + lForm*l
          self.nodeDict[(nodeBand, nodeNumber)] = Drawing_node(triFace.copy(), triNorm)
          #Part.show(triFace)
          #print "i,j: ",nodeBand, " ", nodeNumber
          dMode = True # make struts for the drawing
          strut1 = self.makePriStrut(firstEdge, \
            triNorm, firstGamma, thirdGamma, True, dMode, centerIncircle)
          strut2 = self.makePriStrut(secEdge, \
            triNorm, secGamma, firstGamma, True, dMode, centerIncircle)
          strut3 = self.makePriStrut(thirdEdge, \
            triNorm, thirdGamma, secGamma, False, dMode, centerIncircle)
          self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut1)
          self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut2)
          self.nodeDict[(nodeBand, nodeNumber)].strutList.append(strut3)
        else:
          dMode = False # make struts for the 3D-frame
          self.updateBomCounts(firstEdge.Length, firstGamma, thirdGamma)
          strut1 = self.makePriStrut(firstEdge, \
            triNorm, firstGamma, thirdGamma, True, dMode, centerIncircle)
          self.updateBomCounts(secEdge.Length, secGamma, firstGamma)
          strut2 = self.makePriStrut(secEdge, \
            triNorm, secGamma, firstGamma, True, dMode, centerIncircle)
          self.updateBomCounts(thirdEdge.Length, thirdGamma, secGamma)
          strut3 = self.makePriStrut(thirdEdge, \
            triNorm, thirdGamma, secGamma, False, dMode, centerIncircle)
          self.domeStruts.append(strut1)
          self.domeStruts.append(strut2)
          self.domeStruts.append(strut3)
          #Part.show(strut1)
          #Part.show(strut2)
          #Part.show(strut3)
    
  
  def makePriStrut(self, theEdge, Norm, Gam0, Gam1, NormDir, \
    dMod=False, cIC = None):
    ''' This function generates a strut for the dome frame.
    - dMod stands for drawing mode = generating a flat segment
    - Norm is the face normal of the corresponding dome triangle
    - Normdir is the direction of the Edge, needed to make the strut 
      faces at the inner side of the dome triangle
    - cIC is the center of the inner circle of the triangle
      where this strut belongs to. It is used to calculate a point
      to add an annotation in a drawing
    '''
    
    h = self.strutH
    w = self.strutW
    eLength = theEdge.Length
    # Normalvectors of struts outer plane
    theNorm = theEdge.valueAt(eLength/2.0)
    theNorm.normalize().multiply(h)
  
    # angles between strut normal and face normal
    alpha = theNorm.getAngle(Norm)
    # print "alpha: ", math.degrees(alpha)
    
    # crossing point of the strut edges
    # distance in triangle plane normal to theEdge 
    W1 = w / 2.0 * math.cos(alpha)
    #print "firstW1: ", W1
    if W1 < 0.0: 
      W1 = -W1
    
    if NormDir:
      theStart = theEdge.valueAt(0.0)
      theEnd = theEdge.valueAt(eLength)
      startVal = 0.0
      endVal = theEdge.Length  
    else:
      theStart = theEdge.valueAt(eLength)
      theEnd = theEdge.valueAt(0.0)
      startVal = eLength
      endVal = 0.0
    theVec0 = theEnd - theStart
    theVec1 = theEnd - theStart
    vec2 = theEnd - theStart # needed for annotation point
    theCross = theNorm.cross(theVec0)
    theCross.normalize().multiply(w/2.0)
    
    beta = (math.pi - theEnd.getAngle(theStart)) / 2.0
    sinBeta = math.sin(beta)
    # variables with big S at the end are the values for the
    # Smaller inner points of the dome frame
    domeRadS = self.domeRad - h / sinBeta
    theStartS = Base.Vector(theStart.x, theStart.y, theStart.z)
    theStartS = theStartS.normalize().multiply(domeRadS)
    theEndS = Base.Vector(theEnd.x, theEnd.y, theEnd.z)
    theEndS = theEndS.normalize().multiply(domeRadS)
        
    off0 = W1 / math.tan(Gam0) 
    theVec0.normalize().multiply(off0)
    off1 = W1 / math.tan(Gam1)
    theVec1.normalize().multiply(off1)
  
    # Printing BOM-data to the console  
    #print eLength, ",", math.degrees(beta), ",", \
    #  math.degrees(Gam0), ",", math.degrees(Gam1)
  
  
    # Testpoints
    #tLine = Part.makeLine(theEdge.valueAt(off0), theEdge.valueAt(off0) - theCross)
    #Part.show(tLine)
    theStrutFaces = []
    
    pt0 = theStart + theVec0 - theCross
    pt1 = theEnd - theVec1 - theCross
    pt0S = theStartS + theVec0 - theCross
    pt1S = theEndS - theVec1 - theCross
    
    inEd1 = Part.makeLine(pt0, pt1)
    inEd2 = Part.makeLine(pt1, pt1S)
    inEd3 = Part.makeLine(pt1S, pt0S)
    inEd4 = Part.makeLine(pt0S, pt0)
    inEd4rev = Part.makeLine(pt0, pt0S)
    
    strW1 = Part.Wire([inEd1, inEd2, inEd3, inEd4])
    strF1 = Part.Face(strW1)
    # Part.show(strF1)
    theStrutFaces.append(strF1)
    
    outEd1 = Part.makeLine(theStart, theEnd)
    outEd2 = Part.makeLine(theEnd, theEndS)
    outEd3 = Part.makeLine(theEndS, theStartS)
    outEd4 = Part.makeLine(theStartS, theStart)
    
    strW2 = Part.Wire([outEd1, outEd2, outEd3, outEd4])
    strF2 = Part.Face(strW2)
    # Part.show(strF2)
    theStrutFaces.append(strF2)
    
    c0Ed1 = Part.makeLine(theStart, pt0)
    c0Ed2 = Part.makeLine(pt0S, theStartS)
    c1Ed1 = Part.makeLine(theEnd, pt1)
    c1Ed2 = Part.makeLine(pt1S, theEndS)
    
    strW3 = Part.Wire([c0Ed1, inEd4rev, c0Ed2, outEd4])
    #strW3.fixWire()
    #strW3.isClosed()
    #print "Wire3: ", strW3.isClosed()
    #Part.show(strW3)
    strF3 = Part.Face(strW3)
    #Part.show(strF3)
    theStrutFaces.append(strF3)
  
    strW4 = Part.Wire([c1Ed1, inEd2, c1Ed2, outEd2])
    #Part.show(strW4)
    strF4 = Part.Face(strW4)
    # Part.show(strF4)
    theStrutFaces.append(strF4)
    
    strW5 = Part.Wire([outEd1, c1Ed1, inEd1, c0Ed1])
    #Part.show(strW5)
    strF5 = Part.Face(strW5)
    # Part.show(strF5)
    theStrutFaces.append(strF5)
  
    strW6 = Part.Wire([outEd3, c1Ed2, inEd3, c0Ed2])
    strF6 = Part.Face(strW6)
    # Part.show(strF6)
    theStrutFaces.append(strF6)
    
    strShell = Part.makeShell(theStrutFaces)
    
    strutName = self.strutNames[self.makeStrutKey(eLength, Gam0, Gam1)]
    
    # calculation of the annotation point
    #vec2 = theEnd - theStart
      
    lam = (vec2.z*cIC.z+vec2.y*cIC.y+vec2.x*cIC.x-theStart.z*vec2.z \
      -theStart.y*vec2.y-theStart.x*vec2.x)/(vec2.z**2+vec2.y**2+vec2.x**2)
    
    # tPt touch-point at strut length
    tPt = theStart + vec2.multiply(lam)
    annoDistFact = (w/2.0 + ((cIC - tPt).Length-w/2.0)/3.0) / (cIC - tPt).Length
    
    annoPt = tPt + (cIC - tPt).multiply(annoDistFact)
    annoVert = Part.Vertex(annoPt.x, annoPt.y, annoPt.z)
    
    strut = Strut(Part.makeSolid(strShell), strutName, annoVert, \
      theNorm.normalize())
    if dMod:
      #rFace.rotate(fPt,fAx,math.degrees(-fAn))
      strut.Shape.rotate(theStart, theVec0, math.degrees(alpha))
      #testline = Part.makeLine(cIC, annoPt)
      #Part.show(testline)
    # Part.show(strut)
    return strut
  

  def getPtsAngle(self, pt1, pt2, pt3):
    #return the angle at pt2
    vec1 = pt1 - pt2
    vec2 = pt3 - pt2
    return vec1.getAngle(vec2)


  def equalEdge(self, ed1, ed2, p=6):
    # compares two edges
    e1v1 = ed1.Vertex1
    e1v2 = ed1.Vertex2
    e2v1 = ed2.Vertex1
    e2v2 = ed2.Vertex2
    
    comp1 =  (round(e1v1.X - e2v1.X,p)==0 and \
      round(e1v1.Y - e2v1.Y,p)==0 and round(e1v1.Z - e2v1.Z,p)==0)
    comp2 =  (round(e1v1.X - e2v2.X,p)==0 and \
      round(e1v1.Y - e2v2.Y,p)==0 and round(e1v1.Z - e2v2.Z,p)==0)
    comp3 =  (round(e1v2.X - e2v1.X,p)==0 and \
      round(e1v2.Y - e2v1.Y,p)==0 and round(e1v2.Z - e2v1.Z,p)==0)
    comp4 =  (round(e1v2.X - e2v2.X,p)==0 and \
      round(e1v2.Y - e2v2.Y,p)==0 and round(e1v2.Z - e2v2.Z,p)==0)
    
    return ((comp1 or comp2) and (comp3 or comp4))

  def searchFoldData(self, pFace, cFace):
    rEdge = None
    for pEdge in pFace.Edges:
      # print 'P: ', pEdge.Vertexes[0].Point, ' ', pEdge.Vertexes[1].Point 
      for cEdge in cFace.Edges:
        # print 'C: ', cEdge.Vertexes[0].Point, ' ', cEdge.Vertexes[1].Point
        #if cEdge.isSame(pEdge): # Does not work for what ever reason!?
        if self.equalEdge(cEdge, pEdge):
          rEdge = cEdge
          break
    if rEdge == None:
      print "Error: no common Edge found!"
      #Part.show(pFace)
      #Part.show(cFace)
    #else:
    #  Part.show(cFace)
    fAxis = rEdge.Vertexes[1].Point - rEdge.Vertexes[0].Point
    return fAxis, rEdge.Vertexes[0].Point


  def unfold_tree(self, node):
    # This function traverses the tree and unfolds the faces 
    # beginning at the outermost nodes.
    # print "unfold_tree face", node.idx + 1
    theShell = []
    theStruts = []
    for nodeKey in node.children:
      moreFaces, moreStruts = self.unfold_tree(self.nodeDict[nodeKey])
      theShell = theShell + moreFaces
      theStruts = theStruts + moreStruts
    # nodeShell = [node.triFace]  # self.generateBendShell(node)
    theShell.append(node.triFace)
    theStruts = theStruts + node.strutList
    
    if node.parent <> None:
      fAx, fPt = self.searchFoldData(self.nodeDict[node.parent].triFace, node.triFace)
      fAn = DraftVecUtils.angle(self.nodeDict[node.parent].axis, node.axis, fAx)
      #fAn = nodeDict[node.parent].axis.getAngle(node.axis)
      #print "FoldData Angle: ", math.degrees(fAn)
    
      for rFace in theShell:
        rFace.rotate(fPt,fAx,math.degrees(-fAn))
      for rStrut in theStruts:
        rStrut.Shape.rotate(fPt,fAx,math.degrees(-fAn))
        rStrut.annoPt.rotate(fPt,fAx,math.degrees(-fAn))
    
    #return (theShell + nodeShell)
    return theShell, theStruts

  def makeNodes(self):
    # make a segment for a drawing
    thirdPt = self.icoPts[9]
    for i in range(1):
      j = i*2+1
      self.makeFreqFaces(self.icoPts[0], thirdPt, self.icoPts[j], self.cutTop, 0)
      thirdPt = self.icoPts[j]
      
    thirdPt = self.icoPts[9]
    secPt = self.icoPts[10]
    
    for i in range(2):
      j = i+1
      if i%2 == 0:
        self.makeFreqFaces(secPt, self.icoPts[j], thirdPt, -self.cutMid, self.ny)
      else:  
        self.makeFreqFaces(secPt, thirdPt, self.icoPts[j], self.cutMid, self.ny)
    
      thirdPt = secPt  
      secPt = self.icoPts[j]  
    
    thirdPt = self.icoPts[10]
    for i in range(1):
      j = i*2+2
      self.makeFreqFaces(self.icoPts[11], self.icoPts[j], thirdPt, -self.cutBottom, 2*self.ny)
      thirdPt = self.icoPts[j]
    
    
    # Shell of the geodesic segment
    #domeShell = Part.Shell(domeFaces)
    #Part.show(domeShell)
    
    # make the parent-child relation
    if self.ny > 1:
      self.nodeDict[(0,0)].children = [(1,1)]
      self.nodeDict[(1,1)].parent = (0,0)
    else:
      if self.totalBands > 1:
        self.nodeDict[(0,0)].children = [(1,0)]
        self.nodeDict[(1,0)].parent = (0,0)
    
    
    for i in range(1,self.cutTop):
      #print "Adoption 1 start: ", i
      if i==(self.ny-1):
        child = 0
      else:
        child = 1
      if (i< self.totalBands-1):
        self.nodeDict[(i,0)].children.append((i+1,child))
        self.nodeDict[(i+1,child)].parent = (i,0)
        #Part.show(self.nodeDict[(i,j)].triFace)
      if i>0:
        self.nodeDict[(i,1)].children.append((i,0))
        self.nodeDict[(i,0)].parent = (i,1)  
      for j in range(1,2*i):
        #print "Adoption 1 i: ",i ," j: ",j
        self.nodeDict[(i,j)].children.append((i,j+1))
        self.nodeDict[(i,j+1)].parent = (i,j)
        #Part.show(self.nodeDict[(i,j)].triFace)
    
    for i in range(self.ny, self.ny + self.cutMid):
      for j in range(2*self.ny):
        #print "Adoption 2 i: ",i ," j: ",j
        if (j == 1) and (i< self.totalBands-1):
          self.nodeDict[(i,j)].children.append((i+1,0))
          self.nodeDict[(i+1,0)].parent = (i,j)
        if (j<(2*self.ny-1)):
          self.nodeDict[(i,j)].children.append((i,j+1))
          self.nodeDict[(i,j+1)].parent = (i,j)
          #Part.show(self.nodeDict[(i,j)].triFace)
    
    jMax = 2*self.ny -2
    for i in range(2*self.ny, 2*self.ny + self.cutBottom ):
      for j in range(jMax):
        #print "Adoption 3 i: ",i ," j: ",j
        if (j == 1) and (i< self.totalBands-1):
          self.nodeDict[(i,j)].children.append((i+1,0))
          self.nodeDict[(i+1,0)].parent = (i,j)
        self.nodeDict[(i,j)].children.append((i,j+1))
        self.nodeDict[(i,j+1)].parent = (i,j)
        #Part.show(self.nodeDict[(i,j)].triFace)
      jMax = jMax - 2
  
    self.unFoldedFaces, self.uFoStruts = self.unfold_tree(self.nodeDict[(0,0)])




d = QtGui.QWidget()
d.ui = Ui_Dialog()
d.ui.setupUi(d)
d.ui.updateInfo()

d.show()
