import sys
import clipboard
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


#Connect QT Designer UI file
#UI file must be at same directory
form_class = uic.loadUiType("picc_app.ui")[0]

#Set Coefficient
cf_const = 19.831
cf_ccl = -0.062
cf_rhd = 0.255
cf_hvd = 0.720
cf_tcd = 0.761
cf_vbu = 1.024
cf_sex = -0.821
cf_left = 2.843
cf_manu_bd = -1.25
cf_manu_cook = 0
cf_manu_navilyst = -1.1
cf_manu_genoss = -1
result_right = 0
ecl_right = 0
result_left = 0
ecl_left = 0


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.clear_right_clicked()

        app.focusChanged.connect(self.on_focusChanged)
        self.ccl_right.textChanged.connect(self.check_and_set_value)
        self.rhd_right.textChanged.connect(self.check_and_set_value)
        self.hvd_right.textChanged.connect(self.check_and_set_value)
        self.tcd_right.textChanged.connect(self.check_and_set_value)
        self.vbu_right.textChanged.connect(self.check_and_set_value)
        self.cp_right.textChanged.connect(self.check_and_set_value)
        self.male_right.clicked.connect(self.check_and_set_value)
        self.female_right.clicked.connect(self.check_and_set_value)
        self.clear_right.clicked.connect(self.clear_right_clicked)

        self.result_right_plain.mousePressEvent = self.copy_result_right_plain
        self.result_right_bd.mousePressEvent = self.copy_result_right_bd
        self.result_right_cook.mousePressEvent = self.copy_result_right_cook
        self.result_right_navilyst.mousePressEvent = self.copy_result_right_navilyst
        self.result_right_genoss.mousePressEvent = self.copy_result_right_genoss
        self.ecl_right_plain.mousePressEvent = self.copy_ecl_right_plain
        self.ecl_right_bd.mousePressEvent = self.copy_ecl_right_bd
        self.ecl_right_cook.mousePressEvent = self.copy_ecl_right_cook
        self.ecl_right_navilyst.mousePressEvent = self.copy_ecl_right_navilyst
        self.ecl_right_genoss.mousePressEvent = self.copy_ecl_right_genoss        
    
    def on_focusChanged(self, old, new):
        if new == self.ccl_right:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_cCL.png"))
            self.input_map_right.repaint()
            
        elif new == self.rhd_right:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_2RHD.png"))
            self.input_map_right.repaint()
            
        elif new == self.hvd_right:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_HVD.png"))
            self.input_map_right.repaint()
            
        elif new == self.tcd_right:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_TCD.png"))
            self.input_map_right.repaint()
            
        elif new == self.vbu_right:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_2VBU.png"))
            self.input_map_right.repaint()
            
        else:
            self.input_map_right.setPixmap(QPixmap("./graphic/Rt_none.png"))
            self.input_map_right.repaint()
        
        self.check_and_set_value()
    


    def clear_right_clicked(self):
        self.ccl_right.clear()
        self.rhd_right.clear()
        self.hvd_right.clear()
        self.tcd_right.clear()
        self.vbu_right.clear()
        self.cp_right.clear()
        self.check_and_set_value()
        self.ccl_right.setFocus()

    def check_and_set_value(self):
        global result_right, ecl_right

        #ccl_right check and set
        if self.ccl_right.text() == ".": ccl_right_value = 0
        else: ccl_right_value = float(self.ccl_right.text())
        
        if ccl_right_value == 0: self.ccl_right_label.setStyleSheet("Color : lightgray")
        elif ccl_right_value != 0: self.ccl_right_label.setStyleSheet("Color : black")

        #rhd_right check and set
        if self.rhd_right.text() == ".": rhd_right_value = 0
        else: rhd_right_value = float(self.rhd_right.text())
        
        if rhd_right_value == 0: self.rhd_right_label.setStyleSheet("Color : lightgray")
        elif rhd_right_value != 0: self.rhd_right_label.setStyleSheet("Color : black")

        #hvd_right check and set
        if self.hvd_right.text() == ".": hvd_right_value = 0
        else: hvd_right_value = float(self.hvd_right.text())
        
        if hvd_right_value == 0: self.hvd_right_label.setStyleSheet("Color : lightgray")
        elif hvd_right_value != 0: self.hvd_right_label.setStyleSheet("Color : black")

        #tcd_right check and set
        if self.tcd_right.text() == ".": tcd_right_value = 0
        else: tcd_right_value = float(self.tcd_right.text())
        
        if tcd_right_value == 0: self.tcd_right_label.setStyleSheet("Color : lightgray")
        elif tcd_right_value != 0: self.tcd_right_label.setStyleSheet("Color : black")

        #vbu_right check and set
        if self.vbu_right.text() == ".": vbu_right_value = 0
        else: vbu_right_value = float(self.vbu_right.text())
        
        if vbu_right_value == 0: self.vbu_right_label.setStyleSheet("Color : lightgray")
        elif vbu_right_value != 0: self.vbu_right_label.setStyleSheet("Color : black")

        #cp_right check and set
        if self.cp_right.text() == ".": cp_right_value = 0
        else: cp_right_value = float(self.cp_right.text())

        #sex check
        if self.male_right.isChecked(): sex_right_value = 0
        elif self.female_right.isChecked(): sex_right_value = 1

        #CP+eCL calculation
        if ccl_right_value != 0 and rhd_right_value != 0 and hvd_right_value != 0 and tcd_right_value != 0 and vbu_right_value != 0:
            result_right = cf_const + cf_ccl * ccl_right_value + cf_rhd * rhd_right_value + cf_hvd * hvd_right_value + cf_tcd * tcd_right_value + cf_vbu * vbu_right_value + cf_sex * sex_right_value
            self.result_right_plain.setText(str(round(result_right, 1)))
            self.result_right_bd.setText(str(round(result_right + cf_manu_bd, 1)))
            self.result_right_cook.setText(str(round(result_right + cf_manu_cook, 1)))
            self.result_right_navilyst.setText(str(round(result_right + cf_manu_navilyst, 1)))
            self.result_right_genoss.setText(str(round(result_right + cf_manu_genoss, 1)))
        else:
            result_right = 0
            self.result_right_plain.setText("N/A")
            self.result_right_bd.setText("N/A")
            self.result_right_cook.setText("N/A")
            self.result_right_navilyst.setText("N/A")
            self.result_right_genoss.setText("N/A")

        if ccl_right_value != 0 and rhd_right_value != 0 and hvd_right_value != 0 and tcd_right_value != 0 and vbu_right_value != 0 and cp_right_value !=0:
            ecl_right = cf_const + cf_ccl * ccl_right_value + cf_rhd * rhd_right_value + cf_hvd * hvd_right_value + cf_tcd * tcd_right_value + cf_vbu * vbu_right_value + cf_sex * sex_right_value - cp_right_value
            self.ecl_right_plain.setText(str(round(ecl_right, 1)))
            self.ecl_right_bd.setText(str(round(ecl_right + cf_manu_bd, 1)))
            self.ecl_right_cook.setText(str(round(ecl_right + cf_manu_cook, 1)))
            self.ecl_right_navilyst.setText(str(round(ecl_right + cf_manu_navilyst, 1)))
            self.ecl_right_genoss.setText(str(round(ecl_right + cf_manu_genoss, 1)))
        else:
            ecl_right = 0
            self.ecl_right_plain.setText("N/A")
            self.ecl_right_bd.setText("N/A")
            self.ecl_right_cook.setText("N/A")
            self.ecl_right_navilyst.setText("N/A")
            self.ecl_right_genoss.setText("N/A")

    def copy_result_right_plain(self, event):
        if result_right != 0: clipboard.copy("**CP+eCL = " + str(round(result_right, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_result_right_bd(self, event):
        if result_right != 0: clipboard.copy("**CP+eCL = BD " + str(round(result_right + cf_manu_bd, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_result_right_cook(self, event):
        if result_right != 0: clipboard.copy("**CP+eCL = Cook " + str(round(result_right + cf_manu_cook, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_result_right_navilyst(self, event):
        if result_right != 0: clipboard.copy("**CP+eCL = Navilyst " + str(round(result_right + cf_manu_navilyst, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_result_right_genoss(self, event):
        if result_right != 0: clipboard.copy("**CP+eCL = Genoss " + str(round(result_right + cf_manu_genoss, 1)) + " cm (Right)\n")
        else: clipboard.copy("")

    def copy_ecl_right_plain(self, event):
        if ecl_right != 0: clipboard.copy("**eCL = " + str(round(ecl_right, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_ecl_right_bd(self, event):
        if ecl_right != 0: clipboard.copy("**eCL = BD " + str(round(ecl_right + cf_manu_bd, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_ecl_right_cook(self, event):
        if ecl_right != 0: clipboard.copy("**eCL = Cook " + str(round(ecl_right + cf_manu_cook, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_ecl_right_navilyst(self, event):
        if ecl_right != 0: clipboard.copy("**eCL = Navilyst " + str(round(ecl_right + cf_manu_navilyst, 1)) + " cm (Right)\n")
        else: clipboard.copy("")
    def copy_ecl_right_genoss(self, event):
        if ecl_right != 0: clipboard.copy("**eCL = Genoss " + str(round(ecl_right + cf_manu_genoss, 1)) + " cm (Right)\n")
        else: clipboard.copy("")



if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()