from PySide2 import QtGui, QtWidgets, QtCore


class Option(object):
    def __init__(self, ui):
        self.ui = ui

        # self.dic_resolution = {"360p": (360,640), "480p": (480,854), "720p": (720,1280), "1080p": (1080,1920)}
        self.dic_resolution = {"360p": (640,360), "480p": (854,480), "720p": (1280,720), "1080p": (1920,1080)}

    def set_directory(self, button):
        selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
        print(button.objectName())

        if button.objectName() == "opt_pushButton_urlDownDir":
            self.ui.opt_lineEdit_urlSaveDir.setText(selected_directory)
        elif button.objectName() == "opt_pushButton_saveDir":
            self.ui.opt_lineEdit_saveDir.setText(selected_directory)

    def get_urlSaveDir(self):
        return self.ui.opt_lineEdit_urlSaveDir.Text()

    def get_SaveDir(self):
        return self.ui.opt_lineEdit_saveDir.Text()

    def get_coord(self):
        return self.ui.opt_spinBox_widthValue.value(), self.ui.opt_spinBox_heightValue.value()

    def get_buffertime(self):
        return self.ui.opt_comboBox_bufTime.currentText()

    def get_downFileFmt(self):
        return self.ui.opt_comboBox_downFileFmt.currentText()

    def get_downloadFileDef(self):
        resolution = self.dic_resolution[self.ui.opt_comboBox_downFileDef.currentText()]
        return resolution

    def get_coordFileFmt(self):
        return self.ui.opt_comboBox_coordFmt.currentText()
