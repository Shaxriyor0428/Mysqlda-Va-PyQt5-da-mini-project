from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QMessageBox,QCompleter
from index import Repsitory
from userMainWindow import UserMainwindow
from bookCreate import BookCreate
from createBook_category import CreateBookCategory

class GetInfo():
    def __init__(self):
        self.info = Repsitory().userRepsitory().getByName()
    
    def GetNameInfo(self):
        names = []
        for item in self.info:
            names.append(item[3])
        result = [i.lower() for i in names]
        return result

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,400)
        obj = GetInfo()
        self.names = QCompleter(obj.GetNameInfo())
    
        self.liniUser = QLineEdit(self)
        self.liniUser.move(150,20)
        self.liniUser.setCompleter(self.names)
        self.liniUser.textChanged.connect(self.LoginOnoff)
        self.liniPass = QLineEdit(self)
        self.liniPass.move(150,50)
        self.liniPass.textChanged.connect(self.LoginOnoff)

        self.lblUser = QLabel("Username",self)
        self.lblUser.move(50,25)
        self.lblPass = QLabel("Password",self)
        self.lblPass.move(50,55)
        self.btnLogin = QPushButton("Login",self)
        self.btnRegister = QPushButton("User Register",self)

        


        self.btnRegister.move(130,210)
        self.btnLogin.move(150,270)
        self.liniUser.setStyleSheet("font-size:20px;")
        self.liniPass.setStyleSheet("font-size:20px;")
        self.btnLogin.setStyleSheet("font-size:20px;")
        self.btnRegister.setStyleSheet("font-size:20px;")
        self.lblPass.setStyleSheet("font-size:20px;")
        self.lblUser.setStyleSheet("font-size:20px;")
        self.liniPass.setPlaceholderText("Password..")
        self.liniUser.setPlaceholderText("Username..")

        self.chBox = QCheckBox(self)
        self.chBox.move(360,60)
        self.chBox.clicked.connect(self.showPassword)
        self.btnLogin.clicked.connect(self.checkInfo)
        self.liniPass.setEchoMode(QLineEdit.Password)
        self.btnRegister.clicked.connect(self.registratsiya)
        self.btnBack = QPushButton("Back",self)
        self.btnBack.setStyleSheet("font-size:20px;color:red")
        self.btnBack.move(150,330)
        self.btnBack.clicked.connect(self.backClose)

        self.btnBookCreate = QPushButton("Book Create",self)
        self.btnBookCreate.move(140,150)
        self.btnBookCreate.setStyleSheet("font-size:20px")
        self.btnBookCreate.clicked.connect(self.bookWindow)

        self.btnBookCreateCategory = QPushButton("Book Create Category",self)
        self.btnBookCreateCategory.move(100,100)
        self.btnBookCreateCategory.setStyleSheet("font-size:20px")
        self.btnBookCreateCategory.clicked.connect(self.categoryWindow)


    def bookWindow(self):

        self.bookwin = BookCreate()
        self.bookwin.show()

    def categoryWindow(self):
        self.categoryWin = CreateBookCategory()
        self.categoryWin.show()

    def showPassword(self):
        if self.chBox.isChecked():
            self.liniPass.setEchoMode(QLineEdit.Normal)
        else:
            self.liniPass.setEchoMode(QLineEdit.Password)

    def LoginOnoff(self):
        if len(self.liniUser.text()) > 0 and len(self.liniPass.text()) > 0:
            self.btnLogin.setEnabled(True)
        
        else:
            self.btnLogin.setEnabled(False)


    def checkInfo(self):
        try:
            userRepoObj = Repsitory()
            user = userRepoObj.userRepsitory().getByUserName(self.liniUser.text())
            if user:
                if user.password == self.liniPass.text():
                    self.userMainWin = UserMainwindow(user.id)
                    self.userMainWin.show()
                    self.close()
                else:
                    raise Exception("Password xato")
            else:
                raise Exception("Username topilmadi")

        except Exception as error:
            self.messagBox(str(error))

            self.liniPass.clear()
            self.liniUser.clear()

    def registratsiya(self):
        from registrLogin import Register
        self.obj = Register()
        self.obj.show()
  


    def messagBox(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()

    def backClose(self):
        self.close()

app = QApplication([])
window = Mainwindow()
window.show()
app.exec()
