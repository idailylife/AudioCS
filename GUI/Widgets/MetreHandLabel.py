#coding:utf-8
from PyQt4 import QtGui, QtCore
import CusSettings

class MetreHandLabel(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)
        self.img = QtGui.QPixmap(CusSettings.CURRENT_PATH + 'resources/hand_of_emometre_f.png')
        #self.refresh_img()
        self.rotate_angle = 0.0

    def rotate(self, angle):
        #self.img = self.img.transformed(QtGui.QTransform().rotate(angle))
        self.rotate_angle += angle
        self.update()

    def rotate_to(self, angle):
        self.rotate_angle = angle
        self.update()

    def refresh_img(self):
        self.setPixmap(self.img)

    def get_geometry(self):
        ''' 获得旋转后的坐标位置 '''
        print '%d, %d' %(self.img.width(), self.img.height())

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(41, 41)
        painter.rotate(self.rotate_angle)
        painter.translate(-41, -41)

        painter.drawPixmap(0, 0, 82, 82, self.img)