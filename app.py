# Created by: PyQt5 UI code generator 5.15.10
# Nama    : Danar Mas Saputra
# Kelas   : 1IA06
# NPM     : 50423331


#IMPORT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # LABEL JUDUL AWAL
        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(74, 20, 750, 70))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(15)
        self.label_judul.setFont(font)
        self.label_judul.setObjectName("label_judul")

        # LABEL JUDUL KETIGA
        self.label_judul3 = QtWidgets.QLabel(self.centralwidget)
        self.label_judul3.setGeometry(QtCore.QRect(600, 570, 740, 60))
        font3 = QtGui.QFont()
        font3.setFamily("Imprint MT Shadow")
        font.setPointSize(15)
        self.label_judul.setFont(font3)
        self.label_judul.setObjectName("label_judul3")

        # TOMBOL ULANG DATA
        self.pushButton_ulang = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ulang.setGeometry(QtCore.QRect(480, 619, 80, 40))
        self.pushButton_ulang.setObjectName("pushButton_ulang")

        # TOMBOL MULAI AUDIO FULL HIJAIYA
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(650, 600, 30, 40))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_play.setIcon(QIcon('./Assets/play-button.png'))

        # TOMBOL MULAI AUDIO PERBAGIAN HIJAIYA
        self.pushButton_play2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play2.setGeometry(QtCore.QRect(680, 100, 30, 40))
        self.pushButton_play2.setObjectName("pushButton_play2")     
        # TOMBOL STOP AUDIO FULL HIJAIYA
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(690 , 600, 30, 40))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_stop.setIcon(QIcon('./Assets/audioMute.png'))

        # TOMBOL MULAI DATA
        self.pushButton_mulai = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mulai.setGeometry(QtCore.QRect(480, 570, 80, 40))
        self.pushButton_mulai.setObjectName("pushButton_mulai")
        # GAMBAR MASJID
        self.label_masjid = QtWidgets.QLabel(self.centralwidget)
        self.label_masjid.setGeometry(QtCore.QRect(450, 170, 500, 500))
        self.label_masjid.setText("")
        self.label_masjid.setPixmap(QtGui.QPixmap("Assets/7195a93fdb3cdd462c369f8f98a04be9.jpg-removebg-preview 1.png"))
        self.label_masjid.setScaledContents(True)
        self.label_masjid.setObjectName("label_masjid")

        # KOTAK INPUT
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setGeometry(QtCore.QRect(135, 600, 320, 40))
        self.lineEdit_input.setStyleSheet("lineEdit{\n"
"rgb(217, 217, 217) }")
        self.lineEdit_input.setObjectName("lineEdit_input")

        # LABEL JUDUL KEDUA
        self.label_judul2 = QtWidgets.QLabel(self.centralwidget)
        self.label_judul2.setGeometry(QtCore.QRect(85, 530, 500, 40))
        self.label_judul2.setObjectName("label_judul2")



        # GAMBAR KOTAK UNTUK DATA
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(400,94, 400, 425))
        self.label_output.setText("")
        self.label_output.setPixmap(QtGui.QPixmap("Assets/Rectangle 5.png"))
        self.label_output.setScaledContents(True)
        self.label_output.setObjectName("label_output")

        # GAMBAR SETIAP HURUF HIJAIYA
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(545, 100, 100, 100))
        self.label_image.setText("")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")

        # GAMBAR BACKGROUND RAMADHAN FULL WINDOWNYA
        self.label_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_bg.setGeometry(QtCore.QRect(-20, 0, 1000, 700))
        self.label_bg.setText("")
        self.label_bg.setPixmap(QtGui.QPixmap("Assets/BG_Ramadhan.png"))
        self.label_bg.setScaledContents(True)
        self.label_bg.setObjectName("label_bg")

        # GAMBAR LENTERA RAMADHAN
        self.label_lentera = QtWidgets.QLabel(self.centralwidget)
        self.label_lentera.setGeometry(QtCore.QRect(730, -10, 300, 441))
        self.label_lentera.setText("")
        self.label_lentera.setPixmap(QtGui.QPixmap("Assets/19c08be1c53b2937e38e4470a2d8a602.jpg-removebg-preview.png"))
        self.label_lentera.setScaledContents(True)
        self.label_lentera.setObjectName("label_lentera")

        # GAMBAR HIJAIYA
        self.label_gambarhijaiyah = QtWidgets.QLabel(self.centralwidget)
        self.label_gambarhijaiyah.setGeometry(QtCore.QRect(10, 90, 361, 431))
        self.label_gambarhijaiyah.setText("")
        self.label_gambarhijaiyah.setPixmap(QtGui.QPixmap("./Assets/hijaiya.png"))
        self.label_gambarhijaiyah.setScaledContents(True)
        self.label_gambarhijaiyah.setObjectName("label_gambarhijaiyah")

        # INI UNTUK SHOW
        self.label_bg.raise_()
        self.label_judul.raise_()
        self.label_masjid.raise_()
        self.pushButton_ulang.raise_()
        self.label_judul3.raise_()
        self.pushButton_mulai.raise_()
        self.pushButton_stop.raise_()
        self.pushButton_play.raise_()
        self.lineEdit_input.raise_()
        self.label_judul2.raise_()
        self.label_output.raise_()
        self.label_lentera.raise_()
        self.label_image.raise_()
        self.label_gambarhijaiyah.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # KONEKSI TOMBOL KE FUNCTION 
        self.pushButton_mulai.clicked.connect(self.display_hijaiyah)
        self.pushButton_ulang.clicked.connect(self.reset_input)
        self.pushButton_play.clicked.connect(self.audioPlay)
        self.pushButton_stop.clicked.connect(self.audioStop)
        self.pushButton_play2.clicked.connect(self.audioPlay2)

        # KONEKSI MODULE UNTUK MENGGUNAKAN AUDIO 
        self.player = QMediaPlayer()
    
    # SETTING UKURAN DAN WARNA 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_judul.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:55px; font-weight:600; color:#ffd700;\">Selamat Datang di BelajarYuk</span></p></body></html>"))
        self.pushButton_ulang.setText(_translate("MainWindow", "Ulang"))
        self.pushButton_mulai.setText(_translate("MainWindow", "Mulai"))
        self.label_judul2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:30px; color:#87cc81;\">AYO Masukkan angka untuk memulai:</span></p></body></html>"))
        self.label_judul3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15x; color:#87cc81;\">DIBAWAH INI FULL HIJAIYA AUDIO<br/><br/>↪</span></p></body></html>"))

    # SETTING AUDIO FULL HIJAIYA
    def audioPlay(self):
        audio_url = QUrl.fromLocalFile("./Assets/Audio/audioFull.dat.mp3")
        content = QMediaContent(audio_url)
        self.player.setMedia(content)
        self.player.play()

  # SETTING AUDIO PERBAGIAN HIJAIYA
    def audioPlay2(self):
        self.player.play()
    
    # INI ADALAH TAMPILAN DATA
    def display_hijaiyah(self):
        number = self.lineEdit_input.text()
        if number == '1':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioAlif.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/alif.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;
                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:yellow;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                            font-size: 15px;
                                            padding-top: 300px;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }

                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">ALIF</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">A... </span> </h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Tidak ada Tuhan selain Dia yang<br/> Maha Hidup dan Kokoh.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '2':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioBa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ba.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">BA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">B... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">B A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Tetap ada setelah musnah<br/>seluruh makhluk-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '3':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioTa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()            
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ta.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">TA</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">T... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">T A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang maha menerima<br/>taubat</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '4':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioSa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/sa.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">TSA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">S... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">S  A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang mengokohkan<br />semua makhluk.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '5':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioJim.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ja.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">JIM</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">J... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">J  A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Keluhuran sebutan dan<br/>pujian-Nya serta suci seluruh nama.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '6':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioKha.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/kha.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3"> HA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">H... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">H  A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha hidup dan<br />penyayang.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '7':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioKho.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/khaa.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">KHA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">K... </span>H...<span class="color5"> O...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">K  HO</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha mengetahui akan<br />seluruh perbuatan hambanya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '8':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioDal.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/dal.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">DAL</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">D... </span>A... <span class="color5"> L...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">D  A L</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Pemberi balasan pada<br />hari kiamat.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '9':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioDzal.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/dzal.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">DZAL</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">Z... </span>A...<span class="color5"> L...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">Z A L</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Pemilik segala keagungan<br />dan kemuliaan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '10':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioRo.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ro.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">RA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">R... </span>O...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">R O</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Lemah lembut terhadap<br/>hamba-hamba-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '11':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioZay.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/zai.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">ZA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">Z... </span>A...<span class="color5"> Y...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">Z A Y</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Hiasan penghambaan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '12':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioSin.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/sin.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">SIN</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">S... </span>I...<span class="color5"> N...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">S I N</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha mendengar dan<br/>melihat.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '13':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioSyin.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/syin.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">SYIN</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">S... </span>YI...<span class="color5"> N...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">S YI N</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang disyukuri oleh<br/>hamba-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '14':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioSod.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/sod.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">SHAD</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">S... </span>O...<span class="color5"> D...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">S O D</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha benar dalam setiap<br/>janji-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '15':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioDod.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/dod.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">DHAD</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">D... </span>O...<span class="color5"> D...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">D O D</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang memberikan<br/>madharat dan manfaat.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '16':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioTo.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/to.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">THA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">T... </span>O...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">T  O</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang suci dan<br/>mensucikan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '17':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioZo.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/zo.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">ZHA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">Z... </span>O...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">Z O</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang maha nampak dan<br /> menampakan seluruh tanda-tanda.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '18':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioAin.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ain.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">'AIN</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">A... </span>I...<span class="color5"> N...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">A I N</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha mengetahui<br/>hamba-hamba-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '19':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioGoin.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/goin.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }
                                        .color6{
                                          color: #77E4C8;
                                      }                                      
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">GHAIN</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">G... </span>O...<span class="color5"> I...</span><span class="color6"> N...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4"GO IN</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Tempat mengharap para<br/>pengharap dari semua ciptaan-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '20':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioFa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/fa.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">FA'</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">F... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">F A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Yang menumbuhkan<br/>biji-bijian dan tumbuhan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '21':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioKof.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/kof.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                      
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">QAF</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">K... </span>O...<span class="color5"> F...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">K OF</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha kuasa atas<br/>segala makhluk-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '22':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioKaf.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/kaf.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                                
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">KAF</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">K... </span>A...<span class="color5"> F...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">K AF</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Dia tidak beranak dan<br/>tidak diperanakan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '23':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioLam.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/lam.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                                
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">LAM</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">L... </span>A...<span class="color5"> M...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">LA M</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Maha lembut terhadap<br/>hamba-nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '24':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioMim.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/mim.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }                                         
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">MIM</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">M... </span>A...
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">M A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Pemilik semua kerajaan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '25':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioNun.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/nun.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }                                           
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">NUN</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">N... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">N A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Cahaya bagi langit yang<br/>bersumber pada cahaya arasynya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '26':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioWau.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/wau.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                                
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">WAW</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">W... </span>A...<span class="color5"> U...</span></h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">WA U</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Satu, esa, tempat b<br/>ergantung semua makhluk.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '27':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioHa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ha.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }                                
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">HA</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">H... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">H A</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Memberi petunjuk<br/>bagi makhluk-Nya.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '28':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioLamalif.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/lamalif.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                                
                               
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">LAM ALIF</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">LAM... </span>A...<span class="color5"> LIF...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">LA M A LIF</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Kombinasi dari huruf lam<br/>dengan huruf alif.</p>
                                            </div>
                                        </div>
                                      </body></html>''')                                        
        elif number == '29':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioHamzah.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/hamzah.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }
                                        .color5{
                                          color: #9BEC00;
                                      }                                                
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">HAMZAH</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">HAM... </span>Z...<span class="color5"> AH...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">HA M ZA H</h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Kebijaksanaan.</p>
                                            </div>
                                        </div>
                                      </body></html>''')
        elif number == '30':
            audio_url = QUrl.fromLocalFile("./Assets/Audio/audioYa.dat.mp3")
            content = QMediaContent(audio_url)
            self.player.setMedia(content)
            self.pushButton_play2.raise_()
            self.pushButton_play2.setIcon(QIcon('./Assets/play.png'))   
            self.pushButton_play2.show()
            self.label_image.text()
            self.label_image.setPixmap(QtGui.QPixmap("./Assets/ya.png"))
            self.label_output.setText('''<html>
                                      <head>
                                      <style>
                                        .container {
                                            margin: 0px;
                                            padding: 0px;

                                        }
                                        .card{
                                            text-align:center;                                       
                                      }
                                        .color1{
                                            color:yellow;
                                      }
                                        h1{
                                            color:#36BA98;
                                      }
                                        .color3{
                                            color:#FF7F3E;
                                      }
                                        .color4{
                                            color:#F4CE14;
                                      }                                  
                                      </style>
                                      </head>
                                      <body>
                                        <div class="container"> 
                                            <div class="card two"> 
                                                    <h2 class="color3">YA</h2>
                                            </div>
                                            <div class="card three">
                                                    <h1> <span class="color1">Y... </span>A...</h1>
                                            </div>
                                            <div class="card four">
                                                    <h2 class="color4">Y A  </h2>
                                            </div>
                                            <div class="card five"> 
                                                    <p>Artinya: Tangan Allah yang ter<br/>buka bagi seluruh makhluk-Nya</p>
                                            </div>
                                        </div>
                                      </body></html>''')                                                                                                   
        else:
            self.label_output.setText('DATA ANGKA TIDAK DITEMUKAN COBA ULANGI<br/>DENGAN MENGIKUTI KETENTUAN')  

    # INI ADALAH TOMBOL ULANG (RESET)
    def reset_input(self):
        self.lineEdit_input.clear()
        self.label_output.setText('')
        self.label_image.clear()
        self.label_output.setPixmap(QtGui.QPixmap("Assets/Rectangle 5.png"))
        self.pushButton_play2.hide()

    # INI ADALAH TOMBOL STOP AUDIO
    def audioStop(self):
        self.player.stop()

# RUNNING FILE
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
