from PyQt6 import QtWidgets 
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic
import sys
import sqlite3
import requests
import datetime
# http://openweathermap.org/img/w/04d.png
class Register(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)
        self.name = ""
        self.btnRegister.clicked.connect(self.register)
        self.btnRegister_2.clicked.connect(self.showLoginPage)

    def register(self):
        self.name = self.txtName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not self.name:
            err_box.setText("Please enter your name!")
            err_box.exec()
            return 

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec() 
            return 

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return
        
        query = f"SELECT * FROM USER WHERE email = ('{email}')"
        result = query_db(query)

        if len(result) > 0:
            err_box.setText("This email had been used for an another account!")
            err_box.exec()
            return
        
        query = f"INSERT INTO USER (name, password, email) VALUES ('{self.name}', '{password}', '{email}')"
        print(query)
        insert_db(query)

        success_box.setText("Register Successfully!")
        loginPage.show()
        self.close()

    def showLoginPage(self):
        loginPage.show()
        self.close()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() #call out the characters of ParentClass
        uic.loadUi("ui/login.ui", self) #Create and load the file ui
        self.name = ""
        self.login.clicked.connect(self.checkLogin)
        self.btnRegister.clicked.connect(self.showRegisterPage)
    
    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec()
            return

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return

        query = f"SELECT * FROM USER WHERE email ='{email}' and password='{password}'" #query select
        result = query_db(query)
        self.name = result[0][1]

        if len(result) == 0:
            err_box.setText("Invalid Username or Password!")
            err_box.exec()
            return
        
        success_box.setText("Succesfully Login!")
        success_box.exec()
        self.showMainPage()

    def showRegisterPage(self):
        registerPage.show()
        self.close()

    def showMainPage(self):
        # mainPage.setUsername(self.name)
        mainPage.show()
        self.close()

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/main.ui", self)
        self.name = ""
        self.renderWeather()
        self.Search.clicked.connect(self.renderWeather)
    
    def setUsername(self, name):
        self.name = name
        # self.txtUsername.setText(name)

    def renderWeather(self):
        city = self.cb_city.currentText()
        # A GET request to the API
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=7&appid=6333a9f7333441bb85536e56729e124c&units=metric'
        response = requests.get(url)
        print(response)
        # Print the response
        response_json = response.json()
        weatherInfo = response_json["list"][0]
        self.Pressure.setText(str(weatherInfo["main"]["pressure"]))
        self.Windstatus.setText(str(weatherInfo["wind"]["speed"]))
        self.Visibility.setText(str(weatherInfo["visibility"]))
        self.Humidity.setValue(weatherInfo["main"]["humidity"])
        self.Clouds.setValue(weatherInfo["clouds"]["all"])
        self.Heat.setText(str(weatherInfo["main"]["temp"]))
        self.sunrise.setText((datetime.datetime.utcfromtimestamp(response_json["city"]["sunrise"]) + datetime.timedelta(hours=7)).strftime("%H:%M"))
        self.sunset.setText((datetime.datetime.utcfromtimestamp(response_json["city"]["sunset"]) + datetime.timedelta(hours=7)).strftime("%H:%M"))
    
if __name__ == '__main__':
    sqliteConnection = sqlite3.connect('data/data.db')
    def insert_db(query):
        cusor = sqliteConnection.cursor()
        cusor.execute(query)
        sqliteConnection.commit()
        cusor.close()

    def query_db(query):
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall() #check if the result was in db(in list)
        cursor.close()
        return result
    
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()
    mainPage = MainPage()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    # msg_box.setStyleSheet()
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)
    # success_box.setStyleSheet
    app.exec()
    
