#********************************bibliotheque**********************************************************

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
from math import *
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
from random import randint
from scipy import ndimage
from sklearn.cluster import KMeans


#*****************************************interface****************************************************

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #*********Button**
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 480, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:blue;"
                                      "}"
                                      )
        
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.pushButton5.setObjectName("pushButton2")
        self.pushButton5.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:blue;"
                                      "}"
                                      )
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        
        self.pushButton_2.setGeometry(QtCore.QRect(400, 480, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:purple;"
                                      "}"
                                      )
        
        #****** label *****
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 110, 911, 21))
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 110, 911, 21))
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(315, 10, 2171, 51))
        font=QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(250, 55, 2171, 51))
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(25)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        
        #*******Image label***
        
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(90, 140, 351, 231))
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("label_3")
        self.ImageFinal = QtWidgets.QLabel(self.centralwidget)
        self.ImageFinal.setGeometry(QtCore.QRect(580, 140, 361, 231))
        self.ImageFinal.setText("")
        self.ImageFinal.setObjectName("label_4")
        self.ImageFinal.setStyleSheet("background-color:lightblue;")
        self.ImageOrigine.setStyleSheet("background-color:lightblue;")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 120, 351, 231))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        #*****line for sperate **
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(500, 100, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 60, 761, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        #*******Menu****
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(20,50, 90, 40))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color:lightblue;")
        self.menufichier = QtWidgets.QMenu(self.menubar)
        self.menufichier.setObjectName("menufichier")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuNegative = QtWidgets.QMenu(self.menubar)
        self.menuNegative.setObjectName("menuNegative")
        self.menuRotation = QtWidgets.QMenu(self.menubar)
        self.menuRotation.setObjectName("menuRotation")
        self.menuRedimention = QtWidgets.QMenu(self.menubar)
        self.menuRedimention.setObjectName("menuRedimention")
        self.menuFiltre = QtWidgets.QMenu(self.menubar)
        self.menuFiltre.setObjectName("menuFiltre")
        self.menuMoyenneur = QtWidgets.QMenu(self.menuFiltre)
        self.menuMoyenneur.setObjectName("menuMoyenneur")
        self.menuGaussien = QtWidgets.QMenu(self.menuFiltre)
        self.menuGaussien.setObjectName("menuGaussien")
        self.menuContours = QtWidgets.QMenu(self.menubar)
        self.menuContours.setObjectName("menuContours")
        self.menuSegementation = QtWidgets.QMenu(self.menubar)
        self.menuSegementation.setObjectName("menuSegementation")
        self.menuMorphologie = QtWidgets.QMenu(self.menubar)
        self.menuMorphologie.setObjectName("menuMorphologie")

        self.menuBinarisation = QtWidgets.QMenu(self.menubar)
        self.menuBinarisation.setObjectName("menuBinarisation")
        MainWindow.setMenuBar(self.menubar)
        
        #****sous Menu****
        
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer_sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName("actionEnregistrer_sous")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        
        self.actionNegatif = QtWidgets.QAction(MainWindow)
        self.actionNegatif.setObjectName("actionNegatif")
        self.actionRot1 = QtWidgets.QAction(MainWindow)
        self.actionRot1.setObjectName("actionRot1")
        self.actionRot2 = QtWidgets.QAction(MainWindow)
        self.actionRot2.setObjectName("actionRot2")
        self.actionRot3 = QtWidgets.QAction(MainWindow)
        self.actionRot3.setObjectName("actionRot3")
        self.actionRed1 = QtWidgets.QAction(MainWindow)
        self.actionRed1.setObjectName("actionRed1")
        self.actionRed2 = QtWidgets.QAction(MainWindow)
        self.actionRed2.setObjectName("actionRed2")
        self.actionRed3 = QtWidgets.QAction(MainWindow)
        self.actionRed3.setObjectName("actionRed3")
        self.actionSepia = QtWidgets.QAction(MainWindow)
        self.actionSepia.setObjectName("actionSepia")
        self.actionBinarisation = QtWidgets.QAction(MainWindow)
        self.actionBinarisation.setObjectName("actionBinarisation")
        self.actionGradient = QtWidgets.QAction(MainWindow)
        self.actionGradient.setObjectName("actionGradient")
        self.actionKirsh = QtWidgets.QAction(MainWindow)
        self.actionKirsh.setObjectName("actionKirsh")
        self.actionRobinson = QtWidgets.QAction(MainWindow)
        self.actionRobinson.setObjectName("actionRobinson")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionLaplacien = QtWidgets.QAction(MainWindow)
        self.actionLaplacien.setObjectName("actionLaplacien")
        self.actionCroissance_des_regions = QtWidgets.QAction(MainWindow)
        self.actionCroissance_des_regions.setObjectName("actionCroissance_des_regions")
        self.actionDilatation = QtWidgets.QAction(MainWindow)
        self.actionDilatation.setObjectName("actionDilatation")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionOuverture = QtWidgets.QAction(MainWindow)
        self.actionOuverture.setObjectName("actionOuverture")
        self.actionFermeture = QtWidgets.QAction(MainWindow)
        self.actionFermeture.setObjectName("actionFermeture")

        self.actionAvec_45_degre = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre.setObjectName("actionAvec_45_degre")
        self.actionAvec_45_degre_2 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_2.setObjectName("actionAvec_45_degre_2")
        self.actionAvec_45_degre_3 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_3.setObjectName("actionAvec_45_degre_3")
        self.actionAvec_45_degre_4 = QtWidgets.QAction(MainWindow)
        self.actionAvec_45_degre_4.setObjectName("actionAvec_45_degre_4")
        self.actionAvec_90 = QtWidgets.QAction(MainWindow)
        self.actionAvec_90.setObjectName("actionAvec_90")
        self.actionAvec_180 = QtWidgets.QAction(MainWindow)
        self.actionAvec_180.setObjectName("actionAvec_180")

        self.actionx2_2 = QtWidgets.QAction(MainWindow)
        self.actionx2_2.setObjectName("actionx2_2")
        self.actionx3 = QtWidgets.QAction(MainWindow)
        self.actionx3.setObjectName("actionx3")
        self.actionHistogramme = QtWidgets.QAction(MainWindow)
        self.actionHistogramme.setObjectName("actionHistogramme")
        self.actionEtirement = QtWidgets.QAction(MainWindow)
        self.actionEtirement.setObjectName("actionEtirement")
        self.actionEgalisation = QtWidgets.QAction(MainWindow)
        self.actionEgalisation.setObjectName("actionEgalisation")
        self.action5x5 = QtWidgets.QAction(MainWindow)
        self.action5x5.setObjectName("action5x5")
        self.action7x7 = QtWidgets.QAction(MainWindow)
        self.action7x7.setObjectName("action7x7")
        self.actions_0_2 = QtWidgets.QAction(MainWindow)
        self.actions_0_2.setObjectName("actions_0_2")
        self.actions_0_9 = QtWidgets.QAction(MainWindow)
        self.actions_0_9.setObjectName("actions_0_2")
        self.action4_4 = QtWidgets.QAction(MainWindow)
        self.action4_4.setObjectName("action4_4")
        self.action7_7 = QtWidgets.QAction(MainWindow)
        self.action7_7.setObjectName("action7_7")
        self.actionPartition_des_regions = QtWidgets.QAction(MainWindow)
        self.actionPartition_des_regions.setObjectName("actionPartition_des_regions")
        self.actionMethode_des_K_means = QtWidgets.QAction(MainWindow)
        self.actionMethode_des_K_means.setObjectName("actionMethode_des_K_means")
        self.actionSeuillage_manuelle = QtWidgets.QAction(MainWindow)
        self.actionSeuillage_manuelle.setObjectName("actionSeuillage_manuelle")
        self.actionMethode_d_OTSU = QtWidgets.QAction(MainWindow)
        self.actionMethode_d_OTSU.setObjectName("actionMethode_d_OTSU")
        
        #**integration dans menu---
        
        
        self.menufichier.addAction(self.actionOuvrir)
        self.menufichier.addAction(self.actionEnregistrer_sous)
        self.menufichier.addAction(self.actionQuitter)

        self.menuNegative.addAction(self.actionNegatif)
        
        self.menuRotation.addAction(self.actionRot1)
        self.menuRotation.addSeparator()
        self.menuRotation.addAction(self.actionRot2)
        self.menuRotation.addSeparator()
        self.menuRotation.addAction(self.actionRot3)
        self.menuRotation.addSeparator()
        self.menuRedimention.addAction(self.actionRed1)
        self.menuRedimention.addSeparator()
        self.menuRedimention.addAction(self.actionRed2)
        self.menuRedimention.addSeparator()
        self.menuRedimention.addAction(self.actionRed3)
        self.menuRedimention.addSeparator()
        
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionHistogramme)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionEtirement)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionEgalisation)
        self.menuOption.addSeparator()
        self.menuMoyenneur.addAction(self.action5x5)
        self.menuMoyenneur.addSeparator()
        self.menuMoyenneur.addAction(self.action7x7)
        self.menuMoyenneur.addSeparator()
        self.menuGaussien.addAction(self.actions_0_2)
        self.menuGaussien.addSeparator()
        self.menuGaussien.addAction(self.actions_0_9)
        self.menuGaussien.addSeparator()
        self.menuFiltre.addAction(self.menuMoyenneur.menuAction())
        self.menuFiltre.addSeparator()
        self.menuFiltre.addAction(self.menuGaussien.menuAction())
        self.menuFiltre.addSeparator()
        self.menuContours.addAction(self.actionGradient)
        self.menuContours.addSeparator()
        self.menuContours.addAction(self.actionRobinson)
        self.menuContours.addSeparator()
        self.menuContours.addAction(self.actionKirsh)
        self.menuContours.addSeparator()
        self.menuContours.addAction(self.actionSobel)
        self.menuContours.addSeparator()
        self.menuContours.addAction(self.actionLaplacien)
        self.menuContours.addSeparator()
        self.menuSegementation.addAction(self.actionCroissance_des_regions)
        self.menuSegementation.addSeparator()
        self.menuSegementation.addAction(self.actionPartition_des_regions)
        self.menuSegementation.addSeparator()
        self.menuSegementation.addAction(self.actionMethode_des_K_means)
        self.menuSegementation.addSeparator()
        self.menuMorphologie.addAction(self.actionDilatation)
        self.menuMorphologie.addSeparator()
        self.menuMorphologie.addAction(self.actionErosion)
        self.menuMorphologie.addSeparator()
        self.menuMorphologie.addAction(self.actionOuverture)
        self.menuMorphologie.addSeparator()
        self.menuMorphologie.addAction(self.actionFermeture)
        self.menuMorphologie.addSeparator()
        self.menuBinarisation.addAction(self.actionSeuillage_manuelle)
        self.menuBinarisation.addSeparator()
        self.menuBinarisation.addAction(self.actionMethode_d_OTSU)
        self.menuBinarisation.addSeparator()
        
        #***ajouter Action menu***
        
        self.menubar.addAction(self.menufichier.menuAction())
        
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuNegative.menuAction())
        
        self.menubar.addAction(self.menuRotation.menuAction())
       
        self.menubar.addAction(self.menuRedimention.menuAction())
        
        self.menubar.addAction(self.menuBinarisation.menuAction())
        
        self.menubar.addAction(self.menuFiltre.menuAction())
        
        
        self.menubar.addAction(self.menuContours.menuAction())
       
        self.menubar.addAction(self.menuSegementation.menuAction())
        self.menubar.addAction(self.menuMorphologie.menuAction())
        self.retranslateUi(MainWindow)
        self.actionQuitter.triggered.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton5.clicked.connect(self.openFile)
        self.actionOuvrir.triggered.connect(self.label.show)
        self.actionOuvrir.triggered.connect(self.label3.show)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Fermer"))        
        self.pushButton5.setText(_translate("MainWindow", "Ouvrire"))
        self.label.setText(_translate("MainWindow", "Image Originale"))
        self.label3.setText(_translate("MainWindow", "Traitement d'image"))
        self.label4.setText(_translate("MainWindow", "Quelque traitements peuvent prendre de temps à s'executer ,Veuillez Attendre un peu ,et Merci. "))
        self.label_2.setText(_translate("MainWindow", "Image aprés traitement "))
        self.pushButton_2.setText(_translate("MainWindow", "Reinitialiser"))
        
       
        self.menufichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuNegative.setTitle(_translate("MainWindow", "Negative"))
        self.menuFiltre.setTitle(_translate("MainWindow", "Filtrage"))
        self.menuMoyenneur.setTitle(_translate("MainWindow", "Moyenneur"))
        self.menuGaussien.setTitle(_translate("MainWindow", "Gaussien"))
        self.menuContours.setTitle(_translate("MainWindow", "Contours"))
        self.menuSegementation.setTitle(_translate("MainWindow", "Segementation"))
        self.menuMorphologie.setTitle(_translate("MainWindow", "Morphologie"))
   
        self.menuBinarisation.setTitle(_translate("MainWindow", "Binarisation"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation")) 
        self.menuRedimention.setTitle(_translate("MainWindow", "Redimention"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionEnregistrer_sous.setText(_translate("MainWindow", "Enregistrer sous "))
        self.actionEnregistrer_sous.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+E"))
        
        self.actionNegatif.setText(_translate("MainWindow", "Negatif"))
        self.actionRot1.setText(_translate("MainWindow", "90°"))
        self.actionRot2.setText(_translate("MainWindow", "180°"))
        self.actionRot3.setText(_translate("MainWindow", "270°"))
        self.actionRed1.setText(_translate("MainWindow", "25%"))
        self.actionRed2.setText(_translate("MainWindow", "50%"))
        self.actionRed3.setText(_translate("MainWindow", "60%"))
        self.actionSepia.setText(_translate("MainWindow", "Sepia"))
        self.actionBinarisation.setText(_translate("MainWindow", "Binarisation"))
        self.actionGradient.setText(_translate("MainWindow", "Gradient"))
        self.actionKirsh.setText(_translate("MainWindow", "Kirsh"))
        self.actionRobinson.setText(_translate("MainWindow", "Robinson"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionLaplacien.setText(_translate("MainWindow", "Laplacien"))
        self.actionCroissance_des_regions.setText(_translate("MainWindow", "Croissance des regions"))
        self.actionDilatation.setText(_translate("MainWindow", "Dilatation"))
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.actionOuverture.setText(_translate("MainWindow", "Ouverture"))
        self.actionFermeture.setText(_translate("MainWindow", "Fermeture"))

        self.actionAvec_45_degre.setText(_translate("MainWindow", "Avec 45 droite"))
        self.actionAvec_45_degre_2.setText(_translate("MainWindow", "Avec 45 gauche"))
        self.actionAvec_45_degre_3.setText(_translate("MainWindow", "Avec 90 degre"))
        self.actionAvec_45_degre_4.setText(_translate("MainWindow", "Avec 45 degre"))
        self.actionAvec_90.setText(_translate("MainWindow", "Avec 90°"))
        self.actionAvec_180.setText(_translate("MainWindow", "Avec 180°"))

        self.actionx2_2.setText(_translate("MainWindow", "x2"))
        self.actionx3.setText(_translate("MainWindow", "x3"))
        self.actionHistogramme.setText(_translate("MainWindow", "Histogramme"))
        self.actionEtirement.setText(_translate("MainWindow", "Etirement"))
        self.actionEgalisation.setText(_translate("MainWindow", "Egalisation"))
        self.action5x5.setText(_translate("MainWindow", "5x5"))
        self.action7x7.setText(_translate("MainWindow", "7x7"))
        self.actions_0_2.setText(_translate("MainWindow", " 0.2"))
        self.actions_0_9.setText(_translate("MainWindow", "0.9"))
        self.action4_4.setText(_translate("MainWindow", "4*4"))
        self.action7_7.setText(_translate("MainWindow", "7*7"))
        self.actionPartition_des_regions.setText(_translate("MainWindow", "Partition des regions"))
        self.actionMethode_des_K_means.setText(_translate("MainWindow", "Methode des K-means"))
        self.actionSeuillage_manuelle.setText(_translate("MainWindow", "Seuillage manuelle"))
        self.actionMethode_d_OTSU.setText(_translate("MainWindow", "Methode  d\'OTSU"))



        #******add fonction to actions****
        
        self.actionOuvrir.triggered.connect(self.openFile)
        self.actionNegatif.triggered.connect(self.negatif)
        self.action5x5.triggered.connect(self.Moyenneur5)
        self.action7x7.triggered.connect(self.Moyenneur7)
        self.actions_0_2.triggered.connect(self.gaussian2)
        self.actions_0_9.triggered.connect(self.gaussian9)
        
        self.actionGradient.triggered.connect(self.grad)
        self.actionKirsh.triggered.connect(self.Kirsh)
        self.actionRobinson.triggered.connect(self.Robinson)
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionLaplacien.triggered.connect(self.laplacien)
        self.actionErosion.triggered.connect(self.Erosion)
        self.actionDilatation.triggered.connect(self.dilatation)
        self.actionOuverture.triggered.connect(self.ouverture)
        self.actionFermeture.triggered.connect(self.fermeture)
        self.actionEnregistrer_sous.triggered.connect(self.save)

        self.actionSeuillage_manuelle.triggered.connect(self.binarise)
        self.actionMethode_d_OTSU.triggered.connect(self.otsu)
        self.actionRot1.triggered.connect(self.show_rotation1)
        self.actionRot2.triggered.connect(self.show_rotation2)
        self.actionRot3.triggered.connect(self.show_rotation3)
        
        self.actionRed1.triggered.connect(self.show_redimpurcentage)
        self.actionRed2.triggered.connect(self.show_redimpurcentage2)
        self.actionRed3.triggered.connect(self.show_redimpurcentage3)
        self.actionHistogramme.triggered.connect(self.histo)
        self.pushButton_2.clicked.connect(self.reset)
        self.actionCroissance_des_regions.triggered.connect(self.croissRegiontrue)
        self.actionEtirement.triggered.connect(self.etire)
        self.actionEgalisation.triggered.connect(self.histeq)
        self.actionMethode_des_K_means.triggered.connect(self.kmeanstrue)
        self.actionPartition_des_regions.triggered.connect(self.partRegiontrue)












#******************************************Les Fonctions*************************************







    def openFile(self):
        nom_fichier = QFileDialog.getOpenFileName(None, 'Open file', '', "Image files (*.BMP *.jpg *.gif *.png)")
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)

        self.ImageOrigine.setPixmap(pixmap)
        self.ImageOrigine.setScaledContents(1)

    def save(self):
        self.fileName = QFileDialog.getSaveFileName(None, 'Save file', "Image",
                                                    "Image files ( *.png *.jpg *.BMP *.gif )")

        pixmap = QtGui.QPixmap(self.ImageFinal.pixmap())
        self.fileName = self.fileName[0]

        pixmap.save(self.fileName, "png")
        return self.save

    def reset(self):
        self.ImageOrigine.clear()
        self.ImageFinal.clear()

    def show_rotation1(self):
        anglevalue = 90
        print(anglevalue)
        image = cv2.imread(self.path)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, anglevalue, 0.6)
        rotated = cv2.warpAffine(image, M, (h, w))
       
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], rotated)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
 
        self.label_2.setText("L\'image resultat : Rotation")
        self.label_2.adjustSize()
    
    def show_rotation2(self):
        anglevalue = 180
        print(anglevalue)
        image = cv2.imread(self.path)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, anglevalue, 0.6)
        rotated = cv2.warpAffine(image, M, (h, w))
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], rotated)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.label_2.setText("L\'image resultat : Rotation")
        self.label_2.adjustSize()
       
    def show_rotation3(self):
        anglevalue = 270
        print(anglevalue)
        image = cv2.imread(self.path)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, anglevalue, 0.6)
        rotated = cv2.warpAffine(image, M, (h, w))
   
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], rotated)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
      
        self.label_2.setText("L\'image resultat : Rotation")
        self.label_2.adjustSize()     

    def show_redimpurcentage(self):
        pourcentage = 25
        print(pourcentage)
        image = cv2.imread(self.path)
        scale_percent = pourcentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], resized)
        pixmap = QtGui.QPixmap(fln[0])
       
        
        self.ImageFinal.setPixmap(pixmap)
     
        self.label_2.setText("L\'image resultat : Redimentionement")
        self.label_2.adjustSize()
    def show_redimpurcentage2(self):
        pourcentage = 50
        print(pourcentage)
        image = cv2.imread(self.path)
        scale_percent = pourcentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
       
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], resized)
        pixmap = QtGui.QPixmap(fln[0])
        
        self.ImageFinal.setPixmap(pixmap)
     
        self.label_2.setText("L\'image resultat : Redimentionement")
        self.label_2.adjustSize()    
    def show_redimpurcentage3(self):
        pourcentage = 60
        print(pourcentage)
        image = cv2.imread(self.path)
        scale_percent = pourcentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], resized)
        pixmap = QtGui.QPixmap(fln[0])
        
        self.ImageFinal.setPixmap(pixmap)
     
        self.label_2.setText("L\'image resultat : Redimentionement")
        self.label_2.adjustSize()    
        



    def binarise(self):

        image_init = cv2.imread(self.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        largeur = int(gray_image.shape[0])
        print('largeur=', largeur)
        hauteur = int(gray_image.shape[1])
        print('hauteur = ', hauteur) 
        for i in range(1, largeur):
            for j in range(1, hauteur):
                if gray_image[i][j] <= 120:
                    gray_image[i][j] = 255
                else:
                    gray_image[i][j] = 0
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], gray_image)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Binarisation ")
        self.label_2.adjustSize()

    def otsu(self):
        image_init = cv2.imread(self.path)
        gray = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        pixel_number = gray.shape[0] * gray.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(gray, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)

        for t in bins[1:-1]:
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth
            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            np.seterr(divide='ignore', invalid='ignore')
            value = Wb * Wf * (mub - muf) ** 2
            if value > final_value:
                final_thresh = t
                final_value = value

        final_notreimage = gray.copy()
        final_notreimage[gray > final_thresh] = 255
        final_notreimage[gray < final_thresh] = 0
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], final_notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Binarisation OTSU")
        self.label_2.adjustSize()

    def histo(self):
        notreimage = cv2.imread(self.path, 0)
        equ = cv2.equalizeHist(notreimage)
        res = np.hstack((notreimage, equ))  
        cv2.imwrite('res.png', res)
        hist, bins = np.histogram(notreimage.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()  
        plt.plot(cdf_normalized, color='b')
        plt.hist(notreimage.flatten(), 256, [0, 256], color='r')

        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        
        plt.savefig(fln[0])
        plt.show()

        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Histogram")
        self.label_2.adjustSize()

    def hist(self):
        image_init = cv2.imread(self.path)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([image_init], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])

        plt.show()

    def histgray(self):
        image_init = cv2.imread(self.path)
        gray_image = cv2.cvtColor(image_init, cv2.COLOR_BGR2GRAY)
        Image = np.zeros(257)
        for i in range(1, gray_image.shape[0]):
            for j in range(1, gray_image.shape[1]):
                v = gray_image[i][j] + 1
                Image[v] = Image[v] + 1

        plt.plot(Image)
        plt.show()

   

    def negatif(self):
        image = cv2.imread(self.path)
        notreimage = 255 - image
        height, width, byteValue = notreimage.shape
        print(byteValue)
        if byteValue == 3:
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
            
        
            
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : negative")
        self.label_2.adjustSize()

    def Moyenneur5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        notreimage = f.Moyenneur(5)
        height, width, byteValue = notreimage.shape
        print(byteValue)
        if byteValue == 3:
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
            
       
            
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])    
        
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.moyenneur 5x5")
        self.label_2.adjustSize()

    def Moyenneur7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        notreimage = f.Moyenneur(7)
        height, width, byteValue = notreimage.shape
        print(byteValue)
        if byteValue == 3:
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
       
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.moyenneur 7x7")
        self.label_2.adjustSize()

    def gaussian2(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        notreimage = f.Gaussien(0.2)
        height, width, byteValue = notreimage.shape
        print(byteValue)
        if byteValue == 3:
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
       
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Gaussien 0.2")
        self.label_2.adjustSize()

    def gaussian9(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        notreimage = f.Gaussien(0.9)
        height, width, byteValue = notreimage.shape
        print(byteValue)
        if byteValue == 3:
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : f.Gaussien 0.9")
        self.label_2.adjustSize()

    def median4(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            notreimage = f.Median(4)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
            
        else:
            f = Filtrage(image)
            notreimage = f.Median(4)
            
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.adjustSize()
        self.label_2.setText("image avec Median 4*4")
        self.label_2.adjustSize()

    def median7(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            notreimage = f.Median(7)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            f = Filtrage(image)
            notreimage = f.Median(7)
            
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.adjustSize()
        self.label_2.setText("image avec Median 7*7")
        self.label_2.adjustSize()

    def grad(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            notreimage = c.grad(20)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            notreimage = c.grad(20)

        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : grad")
        self.label_2.adjustSize()

    def Kirsh(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            notreimage = c.Kirsh(20)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            notreimage = c.Kirsh(20)

        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Kirsh")
        self.label_2.adjustSize()

    def Robinson(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            notreimage = c.Robinson()
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            notreimage = c.Robinson()

        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Kirsh")
        self.label_2.adjustSize()    

    def Sobel(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            notreimage = c.Sobel(50)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            notreimage = c.Sobel(50)
            

        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Sobel")
        self.label_2.adjustSize()

    def laplacien(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            notreimage = c.Laplacien(20)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            c = Contours(image)
            notreimage = c.Laplacien(20)
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : laplacien")
        self.label_2.adjustSize()

    def Erosion(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            notreimage = m.Erosion(h)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            notreimage = m.Erosion(h)
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Erosion")
        self.label_2.adjustSize()

        

    def dilatation(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            notreimage = m.dilatation(h)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
            
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            notreimage = m.dilatation(h)
            
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Dilatation")
        self.label_2.adjustSize()

    def ouverture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print("ouverture")
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m1 = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            
            notreimage = m1.Ouverture(h)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            m1 = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            
            notreimage = m1.Ouverture(h)
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], imag)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Ouverture")
        self.label_2.adjustSize()

    def fermeture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m1 = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            
            notreimage = m1.Fermeture(h)
            notreimage = cv2.cvtColor(notreimage, cv2.COLOR_GRAY2RGB)
        else:
            m1 = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            
            notreimage = m1.Fermeture(h)
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], imag)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Fermeture")
        self.label_2.adjustSize()
        
        

    def rgb2gray(self, rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])

    def croissRegion(self):
        image = cv2.imread(self.path)
        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0] * gray.shape[1])
        for i in range(gray_r.shape[0]):

            if gray_r[i] > gray_r.mean():

                gray_r[i] = 255
            elif gray_r[i] > 0.5:
                gray_r[i] = 128
            elif gray_r[i] > 0.1:
                gray_r[i] = 128
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0], gray.shape[1])
       
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], gray_r)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(pixmap)
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Segmentation")
        self.label_2.adjustSize()

    def partRegion(self):
        image = cv2.imread(self.path)
        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0] * gray.shape[1])
        for i in range(gray_r.shape[0]):

            if gray_r[i] > gray_r.mean():

                gray_r[i] = 255
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0], gray.shape[1])
       
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], gray)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(pixmap)
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Segmentation")
        self.label_2.adjustSize()


   
    def kmeanstrue(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        notreimage = s.k_means()
        notreimage = cv2.cvtColor(notreimage, cv2.COLOR_BGR2RGB)
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], notreimage)
        pixmap = QtGui.QPixmap(fln[0])
        
       
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.adjustSize()
        self.label_2.setText("L\'image resultat : k_means")
        self.label_2.adjustSize()

    def partRegiontrue(self):
        image = cv2.imread(self.path)

        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
        for i in range(gray_r.shape[0]):
            
           
            
            if gray_r[i] > gray_r.mean():
                
                gray_r[i] = 255
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0],gray.shape[1])
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], gray)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(pixmap)
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : partition région")
        self.label_2.adjustSize()
    
    def croissRegiontrue(self):
        image = cv2.imread(self.path)
        gray = self.rgb2gray(image)
        gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
        for i in range(gray_r.shape[0]):
           
            if gray_r[i] > gray_r.mean():
               
                gray_r[i] = 255
            elif gray_r[i] > 0.5:
                gray_r[i] = 128
            elif gray_r[i] > 0.1:
               gray_r[i] = 128
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(gray.shape[0],gray.shape[1])
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], gray)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(pixmap)
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : croissance région")
        self.label_2.adjustSize()

    def etire(self):
        M = cv2.imread(self.path)
        MaxV = np.max(M)
        MinV = np.min(M)
        Y = np.zeros_like(M)
        m = M.shape
        for i in range(m[0]):
            for j in range(m[1]):
                Y[i, j] = (255 / (MaxV - MinV) * M[i, j] - MinV)
        
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], Y)
        pixmap = QtGui.QPixmap(fln[0])
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Etirement")
        self.label_2.adjustSize()


    def imhist(self, im):
       
        m, n = im.shape
        h = [0.0] * 256
        for i in range(m):
            for j in range(n):
                h[im[i, j]] += 1
        return np.array(h) / (m * n)

    def cumsum(self, h):
        return [sum(h[:i + 1]) for i in range(len(h))]

    def histeq(self):
        notreimage = cv2.imread(self.path)
        im = cv2.cvtColor(notreimage, cv2.COLOR_BGR2GRAY)  
        h = self.imhist(im)
        cdf = np.array(self.cumsum(h))  
        s1, s2 = im.shape
        sk = np.uint8(255 * cdf)  
        Y = np.zeros_like(im)
        for i in range(0, s1):
            for j in range(0, s2):
                Y[i, j] = sk[im[i, j]]
        fln=QFileDialog.getSaveFileName(None, 'Save file', "Image","Image files ( *.png *.jpg *.BMP *.gif )")
        cv2.imwrite(fln[0], Y)
        pixmap = QtGui.QPixmap(fln[0])
       
        self.ImageFinal.setPixmap(QtGui.QPixmap(pixmap))
        self.ImageFinal.setScaledContents(1)
        self.label_2.setText("L\'image resultat : Egalisation")
        self.label_2.adjustSize()












#******************************************Les Classes seulement pour organiser notre fichier*************










class Operation:
    def __init__(self, image):
        self.image = image

    def rotate_image(self, angle):
        
        image_size = (self.image.shape[1], self.image.shape[0])
        image_center = tuple(np.array(image_size) / 2)

      
        rot_mat = np.vstack(
            [cv2.getRotationMatrix2D(image_center, angle, 1.0), [0, 0, 1]]
        )

        rot_mat_notranslate = np.matrix(rot_mat[0:2, 0:2])

      
        image_w2 = image_size[0] * 0.5
        image_h2 = image_size[1] * 0.5
        rotated_coords = [
            (np.array([-image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([-image_w2, -image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, -image_h2]) * rot_mat_notranslate).A[0]
        ]

        x_coords = [pt[0] for pt in rotated_coords]
        x_pos = [x for x in x_coords if x > 0]
        x_neg = [x for x in x_coords if x < 0]

        y_coords = [pt[1] for pt in rotated_coords]
        y_pos = [y for y in y_coords if y > 0]
        y_neg = [y for y in y_coords if y < 0]

        right_bound = max(x_pos)
        left_bound = min(x_neg)
        top_bound = max(y_pos)
        bot_bound = min(y_neg)

        new_w = int(abs(right_bound - left_bound))
        new_h = int(abs(top_bound - bot_bound))

        trans_mat = np.matrix([
            [1, 0, int(new_w * 0.5 - image_w2)],
            [0, 1, int(new_h * 0.5 - image_h2)],
            [0, 0, 1]
        ])

        affine_mat = (np.matrix(trans_mat) * np.matrix(rot_mat))[0:2, :]

        result = cv2.warpAffine(
            self.image,
            affine_mat,
            (new_w, new_h),
            flags=cv2.INTER_LINEAR
        )
        notreimage = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        return result


class Morphologie:

    def __init__(self, image):
        self.image = image

    def dilatation(self, H):
        imagecopy = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 0):
                    imagecopy[i][j] = 0
                else:
                    imagecopy[i][j] = 255
        return imagecopy

    def Erosion(self, H):
        imagecopy = self.image.copy()

        for i in range(0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if (self.image[i][j] > 128):
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = 0

        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 2295):
                    imagecopy[i][j] = 255
                else:
                    imagecopy[i][j] = 0
        return imagecopy

    def Ouverture(self, H):
        notreimage = self.Erosion(H)
        notreimage=Morphologie(notreimage)
        imageO = notreimage.dilatation(H)
        return imageO

    def Fermeture(self, H):
        notreimage = self.dilatation(H)
        notreimage=Morphologie(notreimage)
        imageF = notreimage.Erosion(H)
        return imageF


class Filtrage:
    def __init__(self, image):
        self.image = image

    def Moyenneur(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s = 0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += self.image[i + n, j + m] / (taille * taille)
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage

    def Median(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                liste = []
                if imagefiltrage[i, j] == 0 or imagefiltrage[i, j] == 255:
                    for n in range(-x, x):
                        for m in range(-x, x):
                            liste.append(imagefiltrage[i + n, j + m])
                    liste.sort()
                    imagefiltrage[i, j] = liste[x + 1]
                    while len(liste) > 0: liste.pop()
        return imagefiltrage

    def h(self,x,y,v):
        x =(1/(2*math.pi*math.pow(v,2)))*(math.exp(-(math.pow(x,2)
            +math.pow(y,2))/(2*math.pow(v,2))))
        return x

    def Gaussien(self, v):
        imagefiltrage = self.image.copy()
        x = 1
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s = 0
                for a in range(-x, x):
                    for b in range(-x, x):
                        s = s + self.h(a, b, v) * self.image[i + a, j + b]
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage


class Contours:

    def __init__(self, image):
        self.image = image

    def grad(self, seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j + 1] - self.image[i, j]
                imageY[i, j] = self.image[i + 1, j] - self.image[i, j]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Kirsh(self, seuil):
        image =self.image.copy()
        imagefel = self.image.copy()
        
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imagefel[i, j] = 5/15 * image[i-1, j-1] + 5/15 * image[i-1,j] + 5/15 * image[i-1,j+1] - 3/15 * image[i+1,j-1] - 3/15 * image[i+1,j] - 3/15 * image[i+1,j+1] - 3/15 * image[i,j-1] - 3/15 * image[i,j] - 3/15 * image[i,j+1]
                if imagefel[i,j]<seuil:
                    imagefel[i,j]=0
                else:
                    imagefel[i,j]=255
        
        return imagefel
    
    def Robinson(self, seuil=128):
        image =self.image.copy()
        imagefel = self.image.copy()
        
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imagefel[i, j] = 1/3 * image[i-1, j-1] + 1/3 * image[i-1,j] + 1/3 * image[i-1,j+1] - 1/3 * image[i+1,j-1] - 1/3 * image[i+1,j] - 1/3 * image[i+1,j+1]
                if imagefel[i,j]<seuil:
                    imagefel[i,j]=0
                else:
                    imagefel[i,j]=255
        
        return imagefel

    def Sobel(self, seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageY[i, j] = -self.image[i - 1, j - 1] - 2 * self.image[i, j - 1] - self.image[i + 1, j - 1] \
                               + self.image[i - 1, j + 1] + 2 * self.image[i, j + 1] + self.image[i + 1, j + 1]
                imageX[i, j] = self.image[i - 1, j - 1] + 2 * self.image[i - 1, j] + self.image[i - 1, j + 1] \
                               - self.image[i + 1, j - 1] - 2 * self.image[i + 1, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Laplacien(self, seuil):
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = -4 * self.image[i, j] + self.image[i - 1, j] + self.image[i + 1, j] \
                                + self.image[i, j - 1] + self.image[i, j + 1]
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def blur(image):
        F = image.copy()
        N, M = image.shape
        h = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        for i in range(2, N - 2):
            for j in range(2, M - 2):
                s = 0
                for n in range(-1, 1):
                    for m in range(-1, 1):
                        s += h[n + 1][m + 1] * image[i + n][j + m]

                F[i][j] = s

        return F

    def Moyenneur(image, taille):
        imagefiltrage = image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, image.shape[0] - x):
            for j in range(x, image.shape[1] - x):
                s = 0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += image[i + n, j + m] / (taille * taille)
                imagefiltrage[i, j] = s
                s = 0
        return imagefiltrage


class Segmentation:

    def __init__(self, image):
        self.image = image

    def k_means(self):
        

        pixel_values = self.image.reshape((-1, 3))
        
        pixel_values = np.float32(pixel_values)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        k = 3
        
        ret, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)

        segmented_image = centers[labels.flatten()]

        segmented_image = segmented_image.reshape(self.image.shape)

        return segmented_image

    def partition_regions(self):
        gray_r = self.image.reshape(self.image.shape[0] * self.image.shape[1])
        for i in range(gray_r.shape[0]):
            if gray_r[i] > gray_r.mean():
                gray_r[i] = 3
            elif gray_r[i] > 0.5:
                gray_r[i] = 2
            elif gray_r[i] > 0.25:
                gray_r[i] = 1
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(self.image.shape[0], self.image.shape[1])
        plt.imshow(gray, cmap='gray')
        return gray









#**************************************main*************************************************************













if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

