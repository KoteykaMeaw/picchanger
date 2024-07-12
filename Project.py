from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PIL import Image, ImageFilter, ImageOps

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 782)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sizeW = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.sizeW.setGeometry(QtCore.QRect(120, 600, 161, 21))
        self.sizeW.setObjectName("sizeW")
        self.sizeH = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.sizeH.setGeometry(QtCore.QRect(300, 600, 161, 21))
        self.sizeH.setObjectName("sizeH")
        self.ApplySize = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ApplySize.setGeometry(QtCore.QRect(230, 640, 101, 41))
        self.ApplySize.setObjectName("ApplySize")
        self.ApplySize.clicked.connect(self.apply_size)

        self.Rotate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Rotate.setGeometry(QtCore.QRect(110, 640, 101, 41))
        self.Rotate.setObjectName("Rotate")
        self.Rotate.clicked.connect(self.rotate_image)

        self.BAWA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BAWA.setGeometry(QtCore.QRect(350, 640, 121, 41))
        self.BAWA.setObjectName("BAWA")
        self.BAWA.clicked.connect(self.black_and_white)

        self.Image = QtWidgets.QLabel(parent=self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(20, 0, 581, 601))
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("C:\\Projects\\Samples\\pqt\\Снимок.JPG"))
        self.Image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Image.setObjectName("Image")
        self.ChangeImage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChangeImage.setGeometry(QtCore.QRect(220, 690, 121, 41))
        self.ChangeImage.setObjectName("ChangeImage")
        self.ChangeImage.clicked.connect(self.open_file)

        self.SaveImage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveImage.setGeometry(QtCore.QRect(350, 690, 121, 41))
        self.SaveImage.setObjectName("SaveImage")
        self.SaveImage.clicked.connect(self.save_image)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sizeW.setHtml(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">New Width</span></p></body></html>"))
        self.sizeW.setPlaceholderText(_translate("MainWindow", "New Width"))
        self.sizeH.setHtml(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">New Height</span></p></body></html>"))
        self.sizeH.setPlaceholderText(_translate("MainWindow", "New Width"))
        self.ApplySize.setText(_translate("MainWindow", "Apply Size"))
        self.Rotate.setText(_translate("MainWindow", "Rotate 90°"))
        self.BAWA.setText(_translate("MainWindow", "Black And White Mode"))
        self.ChangeImage.setText(_translate("MainWindow", "Change Image"))
        self.SaveImage.setText(_translate("MainWindow", "Save Image"))

    def open_file(self):
        # Open a file dialog to select an image
        file_path, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "Select an Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        # Check if a file was selected
        if file_path:
            try:
                # Load the selected image
                self.current_image = Image.open(file_path)
                pixmap = QtGui.QPixmap.fromImage(
                    QtGui.QImage(self.current_image.tobytes("raw", "RGB"), self.current_image.width,
                                 self.current_image.height, QtGui.QImage.Format.Format_RGB888))

                # Scale the image to fit the label
                pixmap = pixmap.scaled(self.Image.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)

                # Set the image to the QLabel
                self.Image.setPixmap(pixmap)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Error loading image: {e}")

    def apply_size(self):
        try:
            if hasattr(self, "current_image"):  # Ensure image is loaded
                width = int(self.sizeW.toPlainText())
                height = int(self.sizeH.toPlainText())
                self.current_image = self.current_image.resize((width, height))
                pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(self.current_image.tobytes("raw", "RGB"), self.current_image.width, self.current_image.height, QtGui.QImage.Format.Format_RGB888))
                self.Image.setPixmap(pixmap)
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Please load an image first.")
        except ValueError:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Invalid size format")

    def rotate_image(self):
        try:
            if hasattr(self, "current_image"):  # Ensure image is loaded
                self.current_image = self.current_image.rotate(90)
                pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(self.current_image.tobytes("raw", "RGB"), self.current_image.width, self.current_image.height, QtGui.QImage.Format.Format_RGB888))
                self.Image.setPixmap(pixmap)
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Please load an image first.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Error rotating image: {e}")

    def black_and_white(self):
        try:
            if hasattr(self, "current_image"):  # Ensure image is loaded
                self.current_image = ImageOps.grayscale(self.current_image)

                if self.current_image.mode == "L":
                    self.current_image = self.current_image.convert("RGB")
                else:
                    self.current_image = ImageOps.grayscale(self.current_image)
                pixmap = QtGui.QPixmap.fromImage(
                    QtGui.QImage(self.current_image.tobytes("raw", "RGB"), self.current_image.width,
                                 self.current_image.height, QtGui.QImage.Format.Format_RGB888))
                self.Image.setPixmap(pixmap)
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Please load an image first.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Error converting to black and white: {e}")

    def save_image(self):
        try:
            if hasattr(self, "current_image"):  # Ensure image is loaded
                file_path, _ = QFileDialog.getSaveFileName(
                    self.centralwidget,
                    "Save Image",
                    "",
                    "Images (*.png *.jpg *.jpeg *.bmp)"
                )

                if file_path:
                    self.current_image.save(file_path)
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Please load an image first.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Error saving image: {e}")