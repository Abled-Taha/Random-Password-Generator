import sys
import os
import pyperclip
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow, QMessageBox, QWidget, QLineEdit, QPushButton, QLineEdit, QApplication, QScrollArea, QVBoxLayout, QCheckBox, QMenuBar
from PyQt5.QtGui import QIcon, QPixmap, QFont, QDesktopServices
from PyQt5.QtCore import QUrl, Qt
import Functions

class SignInApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeMainWindow()
        self.initializeUI()
        
    def initializeMainWindow(self):
        # Initializing Main Window
        self.setWindowTitle("Random Password Generator - Sign In | Log In")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) #Width, Height

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

        # Initializing Font
        self.headingFont = QFont()
        self.headingFont.setFamily("Arial Black")
        self.headingFont.setPointSize(20)
        self.headingFont.setBold(True)
        self.headingFont.setUnderline(False)
        self.headingFont.setWeight(75)

    def initializeUI(self):
        # Initializing Labels
        self.mainLabel = QLabel(self)
        self.signUpLabel = QLabel(self)

        # Initializing Text Fields
        self.emailLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)

        # Initializing Buttons
        self.signInButton = QPushButton(self)
        self.signInButton.clicked.connect(self.getData)

        self.signUpButton = QPushButton(self)
        self.signUpButton.clicked.connect(self.runSignUpApp)

        self.deleteUserButton = QPushButton(self)
        self.deleteUserButton.clicked.connect(self.runDeleteUserApp)

        # Customizing Labels
        self.mainLabel.setGeometry(20, 10, 251, 41) # x, y, width, height
        self.mainLabel.setText("Sign In | Log In")
        self.mainLabel.setFont(self.headingFont)
        self.mainLabel.show()

        self.signUpLabel.setGeometry(70, 340, 130, 21) # x, y, width, height
        self.signUpLabel.setText("Don't have an account?")
        self.signUpLabel.show()

        # Customizing Text Fields
        self.emailLineEdit.setGeometry(10, 170, 251, 23) # x, y, width, height
        self.emailLineEdit.setPlaceholderText("Email")
        self.emailLineEdit.show()

        self.passwordLineEdit.setGeometry(10, 210, 251, 23) # x, y, width, height
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLineEdit.show()

        # Customizing Buttons
        self.signInButton.setGeometry(90, 250, 91, 41) # x, y, width, height
        self.signInButton.setText("Sign In")
        self.signInButton.setCursor(Qt.PointingHandCursor)
        self.signInButton.show()

        self.signUpButton.setGeometry(210, 340, 61, 21) # x, y, width, height
        self.signUpButton.setText("Sign Up")
        self.signUpButton.setCursor(Qt.PointingHandCursor)
        self.signUpButton.show()

        self.deleteUserButton.setGeometry(180, 310, 91, 21) # x, y, width, height
        self.deleteUserButton.setText("Delete User")
        self.deleteUserButton.setCursor(Qt.PointingHandCursor)
        self.deleteUserButton.show()

    def getData(self):
        self.email = self.emailLineEdit.text()
        self.password = self.passwordLineEdit.text()
        self.isCorrect = Functions.validateSignIn(self.email, self.password)
        if self.isCorrect == True:
            self.runMainApp()
        else:
            self.incorrectInfo()

    def incorrectInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Critical)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setText("Incorrect Information!")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def runMainApp(self):
        self.close()
        global email
        email = self.email
        self.MainWindow = MainApp()
        self.MainWindow.show()

    def runSignUpApp(self):
        self.close()
        self.MainWindow = SignUpApp()
        self.MainWindow.show()

    def runDeleteUserApp(self):
        self.close()
        self.MainWindow = DeleteUserApp()
        self.MainWindow.show()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Return:
            self.getData()



class SignUpApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeMainWindow()
        self.initializeUI()
        
    def initializeMainWindow(self):
        # Initializing Main Window
        self.setWindowTitle("Random Password Generator - Sign Up")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) #Width, Height

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

        # Initializing Font
        self.headingFont = QFont()
        self.headingFont.setFamily("Arial Black")
        self.headingFont.setPointSize(19)
        self.headingFont.setBold(True)
        self.headingFont.setUnderline(False)
        self.headingFont.setWeight(75)

    def initializeUI(self):
        # Initializing Labels
        self.mainLabel = QLabel(self)
        self.signInLabel = QLabel(self)

        # Initializing Text Fields
        self.emailLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)
        self.confirmPasswordLineEdit = QLineEdit(self)

        # Initializing Buttons
        self.signUpButton = QPushButton(self)
        self.signUpButton.clicked.connect(self.getData)

        self.signInButton = QPushButton(self)
        self.signInButton.clicked.connect(self.runSignInApp)

        # Customizing Labels
        self.mainLabel.setGeometry(10, 10, 251, 41) # x, y, width, height
        self.mainLabel.setText("Sign Up | Register")
        self.mainLabel.setFont(self.headingFont)
        self.mainLabel.show()

        self.signInLabel.setGeometry(67, 340, 140, 21) # x, y, width, height
        self.signInLabel.setText("Already have an account?")
        self.signInLabel.show()

        # Customizing Buttons
        self.signUpButton.setGeometry(90, 250, 91, 41) # x, y, width, height
        self.signUpButton.setText("Sign Up")
        self.signUpButton.setCursor(Qt.PointingHandCursor)
        self.signUpButton.show()

        self.signInButton.setGeometry(210, 340, 61, 21) # x, y, width, height
        self.signInButton.setText("Sign In")
        self.signInButton.setCursor(Qt.PointingHandCursor)
        self.signInButton.show()

        # Customizing Text Fields
        self.emailLineEdit.setGeometry(10, 130, 251, 23) # x, y, width, height
        self.emailLineEdit.setPlaceholderText("Email")
        self.emailLineEdit.show()

        self.passwordLineEdit.setGeometry(10, 170, 251, 23) # x, y, width, height
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLineEdit.show()

        self.confirmPasswordLineEdit.setGeometry(10, 210, 251, 23) # x, y, width, height
        self.confirmPasswordLineEdit.setPlaceholderText("Confirm Password")
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmPasswordLineEdit.show()

    def getData(self):
        self.email = self.emailLineEdit.text()
        self.password = self.passwordLineEdit.text()
        self.confirmPassword = self.confirmPasswordLineEdit.text()
        self.isCorrect = Functions.validateSignUp(self.email, self.password, self.confirmPassword)
        if self.isCorrect == True:
            self.correctInfo()
        else:
            self.incorrectInfo()

    def correctInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Done.")
        self.msgBox.setText("Your Account has been created, please Log in.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def incorrectInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Critical)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setText("Please provide valid Information and confirm the password fields. Otherwise there is already an account with this email, try logging in.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def runSignInApp(self):
        self.close()
        self.MainWindow = SignInApp()
        self.MainWindow.show()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Return:
            self.getData()



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeWindow()
        self.initializeUI()

    def initializeWindow(self):
        # Initializing Menu Bar
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)

        # Initializing New Actions
        self.createNewPassword = QAction("Create", self)
        self.createNewPassword.setShortcut("Ctrl+N")
        self.createNewPassword.setStatusTip("Create New Password")
        self.createNewPassword.triggered.connect(self.runCreateNewApp)

        self.deletePassword = QAction("Delete", self)
        self.deletePassword.setShortcut("Ctrl+Del")
        self.deletePassword.setStatusTip("Delete an existing Password")
        self.deletePassword.triggered.connect(self.runDeleteApp)

        self.openGitHub = QAction("GitHub", self)
        self.openGitHub.setShortcut("Ctrl+H")
        self.openGitHub.setStatusTip("Open GitHub Repository")
        self.openGitHub.triggered.connect(self.openGitHubRepo)

        # Initializing New Menus
        self.passwordMenu = self.menuBar.addMenu("Password")
        self.passwordMenu.addAction(self.createNewPassword)
        self.passwordMenu.addAction(self.deletePassword)

        self.helpMenu = self.menuBar.addMenu("Help")
        self.helpMenu.addAction(self.openGitHub)

        # Initializing Main Window
        self.setWindowTitle("Random Password Generator")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) # width, height

        # Initializing Scroll Area
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

    def initializeUI(self):
        # Initializing Password Buttons
        self.keyCount, self.keyList = Functions.Details(email)
        for i in range(0, self.keyCount):
            object = QPushButton()
            object.clicked.connect(self.passwordButtonClicked)
            object.setObjectName(self.keyList[0])
            object.setText(self.keyList[0])
            self.keyList.pop(0)
            self.vbox.addWidget(object)

    def openGitHubRepo(self):
        QDesktopServices.openUrl(QUrl("https://github.com/Abled-Taha/Random-Password-Generator-GUI"))

    def copied(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Copied!")
        self.msgBox.setText("You Password has been Copied to your clipboard.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def passwordButtonClicked(self):
        object = self.sender()
        password = Functions.getPass(object.objectName(), email)
        pyperclip.copy(password)
        self.copied()

    def runCreateNewApp(self):
        self.close()
        self.MainWindow = CreateNewApp()
        self.MainWindow.show()

    def runDeleteApp(self):
        self.close()
        self.MainWindow = DeleteApp()
        self.MainWindow.show()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.close()



class CreateNewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeWindow()
        self.initializeUI()

    def initializeWindow(self):
        # Initializing Main Window
        self.setWindowTitle("Random Password Generator - Create New Password")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) # width, height

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

    def initializeUI(self):
        # Initializing Buttons
        self.generatePasswordButton = QPushButton(self)
        self.generatePasswordButton.clicked.connect(self.getData)

        self.backButton = QPushButton(self)
        self.backButton.clicked.connect(self.back)

        # Initializing Text Fields
        self.nameOfPasswordField = QLineEdit(self)
        self.numberOfCharactersField = QLineEdit(self)

        # Initializing Check Boxes
        self.capitalLettersCheckBox = QCheckBox(self)
        self.smallLettersCheckBox = QCheckBox(self)
        self.numbersCheckBox = QCheckBox(self)
        self.symbolsCheckBox = QCheckBox(self)

        # Customizing Buttons
        self.generatePasswordButton.setGeometry(80, 250, 120, 30) # x, y, width, height
        self.generatePasswordButton.setText("Generate Password")
        self.generatePasswordButton.setCursor(Qt.PointingHandCursor)
        self.generatePasswordButton.show()

        self.backButton.setGeometry(0, 340, 61, 21) # x, y, width, height
        self.backButton.setText("Go Back")
        self.backButton.setCursor(Qt.PointingHandCursor)
        self.backButton.show()

        # Customizing Text Fields
        self.nameOfPasswordField.setGeometry(10, 45, 200, 30)
        self.nameOfPasswordField.setPlaceholderText("Name the Password.") # x, y, width, height
        self.nameOfPasswordField.show()

        self.numberOfCharactersField.setGeometry(10, 80, 200, 30) # x, y, width, height
        self.numberOfCharactersField.setPlaceholderText("How many characters?")
        self.numberOfCharactersField.show()
        
        # Customizing Check Boxes
        self.capitalLettersCheckBox.setGeometry(10, 120, 200, 20) # x, y, width, height
        self.capitalLettersCheckBox.setText("Should Contain Capital Letters?")
        self.capitalLettersCheckBox.setCursor(Qt.PointingHandCursor)
        self.capitalLettersCheckBox.show()

        self.smallLettersCheckBox.setGeometry(10, 140, 200, 20) # x, y, width, height
        self.smallLettersCheckBox.setText("Should Contain Small Letters?")
        self.smallLettersCheckBox.setCursor(Qt.PointingHandCursor)
        self.smallLettersCheckBox.show()

        self.numbersCheckBox.setGeometry(10, 160, 200, 20) # x, y, width, height
        self.numbersCheckBox.setText("Should Contain Numbers?")
        self.numbersCheckBox.setCursor(Qt.PointingHandCursor)
        self.numbersCheckBox.show()

        self.symbolsCheckBox.setGeometry(10, 180, 200, 20) # x, y, width, height
        self.symbolsCheckBox.setText("Should Contain Symbols?")
        self.symbolsCheckBox.setCursor(Qt.PointingHandCursor)
        self.symbolsCheckBox.show()

    def getData(self):
        try:
            self.nameOfPasswordFieldText = str(self.nameOfPasswordField.text())
            self.numberOfCharactersFieldText = int(self.numberOfCharactersField.text())
        except:
            self.incorrectInfo()
        self.isCapitalChecked = self.capitalLettersCheckBox.isChecked()
        self.isSmallChecked = self.smallLettersCheckBox.isChecked()
        self.isNumbersChecked = self.numbersCheckBox.isChecked()
        self.isSymbolsChecked = self.symbolsCheckBox.isChecked()
        Functions.createPassword(self.nameOfPasswordFieldText, self.numberOfCharactersFieldText, self.isCapitalChecked, self.isSmallChecked, self.isNumbersChecked, self.isSymbolsChecked, email)
        self.done()

    def back(self):
        self.close()
        self.MainWindow = MainApp()
        self.MainWindow.show()

    def done(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Done!")
        self.msgBox.setText("Your New Password has been created.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def incorrectInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Critical)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setText("Please provide valid Information.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.back()
        if e.key() == Qt.Key_Return:
            self.getData()



class DeleteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeWindow()
        self.initializeUI()

    def initializeWindow(self):
        # Initializing Main Window
        self.setWindowTitle("Random Password Generator - Delete Password")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) #Width, Height

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

    def initializeUI(self):
        # Initializing Buttons
        self.deleteButton = QPushButton(self)
        self.deleteButton.clicked.connect(self.getData)

        self.backButton = QPushButton(self)
        self.backButton.clicked.connect(self.back)

        # Initializing Text Fields
        self.nameOfPasswordTextField = QLineEdit(self)

        # Customizing Buttons
        self.deleteButton.setGeometry(85, 200, 100, 30) # x, y, width, height
        self.deleteButton.setText("Delete Password")
        self.deleteButton.setCursor(Qt.PointingHandCursor)
        self.deleteButton.show()

        self.backButton.setGeometry(0, 340, 61, 21) # x, y, width, height
        self.backButton.setText("Go Back")
        self.backButton.setCursor(Qt.PointingHandCursor)
        self.backButton.show()

        # Customizing Text Fields
        self.nameOfPasswordTextField.setGeometry(35, 80, 200, 30) # x, y, width, height
        self.nameOfPasswordTextField.setPlaceholderText("Name Of Password?")
        self.nameOfPasswordTextField.show()

    def getData(self):
        self.nameOfPasswordTextFieldText = self.nameOfPasswordTextField.text()
        isDone = Functions.deletePassword(self.nameOfPasswordTextFieldText, email)
        if isDone:
            self.done()
        else:
            self.incorrectInfo()

    def back(self):
        self.close()
        self.MainWindow = MainApp()
        self.MainWindow.show()

    def done(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Done!")
        self.msgBox.setText("Your Password has been deleted.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def incorrectInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Critical)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setText("Please provide valid Information.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.back()
        if e.key() == Qt.Key_Return:
            self.getData()

class DeleteUserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeWindow()
        self.initializeUI()
    
    def initializeWindow(self):
        # Initializing Main Window
        self.setWindowTitle("Random Password Generator - Delete User")
        self.setWindowIcon(QIcon("Files/icon.png"))
        self.resize(271, 364) #Width, Height

        # Initializing Icon
        self.Icon = QIcon()
        self.Icon.addPixmap(QPixmap("Files/icon.png"), QIcon.Mode.Normal, QIcon.State.Off)

    def initializeUI(self):
        # Initializing Buttons
        self.deleteButton = QPushButton(self)
        self.deleteButton.clicked.connect(self.getData)

        self.backButton = QPushButton(self)
        self.backButton.clicked.connect(self.back)

        # Initializing Text Fields
        self.nameOfUserTextField = QLineEdit(self)
        self.passwordTextField = QLineEdit(self)

        # Customizing Buttons
        self.deleteButton.setGeometry(85, 200, 100, 30) # x, y, width, height
        self.deleteButton.setText("Delete User")
        self.deleteButton.setCursor(Qt.PointingHandCursor)
        self.deleteButton.show()

        self.backButton.setGeometry(0, 340, 61, 21) # x, y, width, height
        self.backButton.setText("Go Back")
        self.backButton.setCursor(Qt.PointingHandCursor)
        self.backButton.show()

        # Customizing Text Fields
        self.nameOfUserTextField.setGeometry(35, 80, 200, 30) # x, y, width, height
        self.nameOfUserTextField.setPlaceholderText("Name Of User?")
        self.nameOfUserTextField.show()

        self.passwordTextField.setGeometry(35, 115, 200, 30) # x, y, width, height
        self.passwordTextField.setPlaceholderText("Password?")
        self.passwordTextField.show()

    def done(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Done!")
        self.msgBox.setText("The User has been deleted.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def incorrectInfo(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setIcon(QMessageBox.Icon.Critical)
        self.msgBox.resize(50, 50) # width, height
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setText("Please provide valid Information.")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def getData(self):
        self.nameOfUserTextFieldText = self.nameOfUserTextField.text()
        self.passwordTextFieldText = self.passwordTextField.text()
        isDone = Functions.deleteUser(self.nameOfUserTextFieldText, self.passwordTextFieldText)
        if isDone:
            self.done()
        else:
            self.incorrectInfo()

    def back(self):
        self.close()
        self.MainWindow = SignInApp()
        self.MainWindow.show()

    def keyPressEvent(self, e):     
        if e.key() == Qt.Key_Escape:
            self.back()
        if e.key() == Qt.Key_Return:
            self.getData()




# Defining Application
app = QApplication(sys.argv)
app.setStyleSheet(open("Files/style.css").read())

if os.path.isdir("Files/Accounts") == True:
    # Defining Main Window
    MainWindow = SignInApp()
else:
    MainWindow = SignUpApp()

# Running Main Window
MainWindow.show()

# Defining Exit
sys.exit(app.exec())