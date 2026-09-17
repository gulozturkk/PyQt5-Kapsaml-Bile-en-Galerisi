import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Optimize Edilmiş Bileşen Projesi")
        self.setGeometry(100, 100, 1000, 800)

        #ana sekme yapısı
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs) #Oluşturduğumuz sekmeleri ana pencerenin ana gövdesi yapar.

        #üst menü çubuğu
        self.init_menu()

        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "1.Butonlar - Temel")
        self.init_tab1()

        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "2.Sayısal - Medya")
        self.init_tab2()

        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "3.Veri - Metin")
        self.init_tab3()

        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4, "4.Yerleşim & Çerçeve")
        self.init_tab4()


    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Dosya")
        exit_action = QAction("Çıkış",self) # QAction :Menü veya araç çubuklarına eklendiğinde tıklandığında bir komut çalıştıran arayüz bileşeni oluşturur
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def init_tab1(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 30, 20, 20) #Üstten ve yanlardan boşluk bırakmak için margins ekliyoruz sol-üst-sağ-alt
        form_layout = QFormLayout()
        self.label_info = QLabel("Lütfen adınızı giriniz:")
        self.entry_input = QLineEdit()
        self.entry_input.setPlaceholderText("Adınızı buraya giriniz")

        form_layout.addRow(self.label_info, self.entry_input)

        self.checkbox_agree = QCheckBox("Kullanım şartlarını onaylıyorum")
        self.radio_btn1 = QRadioButton("Standart Üyelik")
        self.radio_btn2 = QRadioButton("VIP Üyelik")
        self.radio_btn1.setChecked(True) #varsayılan olarak standart üyelik seçili

        #buton çeşitleri grubu
        button_group = QGroupBox("Buton Çeşitleri")
        button_layout = QVBoxLayout()

        self.btn_submit = QPushButton("Gönder")
        self.btn_submit.clicked.connect(self.on_submit_clicked)

        self.btn_toggle = QPushButton("Toggle Buton (Aç/Kapa)")
        self.btn_toggle.clicked.connect(self.on_toggle_clicked)

        self.tool_btn = QToolButton() #Araç çubuklarında simge veya metinle hızlı erişim sağlayan bir düğme oluşturur.
        self.tool_btn.setText("Hızlı İşlem")
        self.tool_btn.clicked.connect(lambda: QMessageBox.information(self,"ToolButton","ToolButton tıklandı"))


        #Ana başlığı ve alt açıklama metni bulunan, tıklanabilir bir komut düğmesi oluşturur.
        self.command_btn = QCommandLinkButton("Fontu değiştir","Yazı tipini değiştimek için tıklayın")
        self.command_btn.clicked.connect(self.change_font)

        button_layout.addWidget(self.btn_submit)
        button_layout.addWidget(self.btn_toggle)
        button_layout.addWidget(self.tool_btn)
        button_layout.addWidget(self.command_btn)
        button_group.setLayout(button_layout)

        #ana layouta ekleme
        layout.addLayout(form_layout)
        layout.addWidget(self.label_info)
        layout.addWidget(self.entry_input)
        layout.addWidget(self.checkbox_agree)
        layout.addWidget(self.radio_btn1)
        layout.addWidget(self.radio_btn2)
        layout.addWidget(button_group)
        layout.addStretch()

        self.tab1.setLayout(layout)

    def init_tab2(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 30, 20, 20)
        layout.setSpacing(20)

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0,100)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)

        self.progressbar = QProgressBar()
        self.progressbar.setStyleSheet("QProgressBar{color:black}   QProgressBar::chunk {background-color:white;}")
        self.progressbar.setValue(0)

        # Senkronizasyon (Biri değiştiğinde diğerleri de güncellenir)
        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)
        self.slider.valueChanged.connect(self.progressbar.setValue)

        #takvim
        self.calendar = QCalendarWidget()
        self.calendar_label = QLabel("Seçilen Tarih:")
        self.calendar.selectionChanged.connect(self.update_calendar_Date)

        #görsel alanı
        self.image_label = QLabel("Henüz görsel yüklenmedi")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px dashed gray; background-color: #2b2b2b; color: gray;")
        self.image_label.setFixedHeight(100)

        btn_load_image = QPushButton("Bilgisayardan resim seç")
        btn_load_image.clicked.connect(self.load_image)

        #layouta ekleme
        layout.addWidget(QLabel("Değer Seçimi:"))
        layout.addWidget(self.spinbox)
        layout.addWidget(self.slider)
        layout.addWidget(self.progressbar)

        layout.addWidget(self.calendar_label)
        layout.addWidget(self.calendar)

        layout.addStretch()
        self.tab2.setLayout(layout)

    def init_tab3(self):
        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(15)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Seçiniz...","Python", "PyQt5", "Yazılım Geliştirme"])
        self.combo_label = QLabel("Seçim:Yok")
        self.combo_box.currentIndexChanged.connect(
            lambda i: self.combo_label.setText(f"Seçilen: {self.combo_box.currentText()}" if i > 0 else "Seçim: Yok")
        )
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Görev1","Görev2","Görev3"])
        self.list_input = QLineEdit()
        self.list_input.setPlaceholderText("Yen öğe yazın...")

        btn_add_item = QPushButton("Listeye Ekle")
        btn_add_item.clicked.connect(self.add_list_item)

        btn_del_item = QPushButton("Seçileni Sil")
        btn_del_item.clicked.connect(self.delete_list_item)

        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText("Notlarınızı buraya yazabilirsiniz")
        btn_clear_text = QPushButton("Metni Temizle")
        btn_clear_text.clicked.connect(self.text_editor.clear)

        self.table = QTableWidget(2,2)
        self.table.setHorizontalHeaderLabels(["Ürün","Fiyat"])
        self.table.setItem(0,0 ,QTableWidgetItem("Kalem"))
        self.table.setItem(0,1,QTableWidgetItem("20 TL"))
        self.table.setItem(1,0 ,QTableWidgetItem("Defter"))
        self.table.setItem(1,1,QTableWidgetItem("45 TL"))

        layout.addWidget(QLabel("ComboBox:"), 0, 0)
        layout.addWidget(self.combo_box, 0, 1)
        layout.addWidget(self.combo_label, 0, 2)

        layout.addWidget(QLabel("List Widget:"),1,0)
        layout.addWidget(self.list_widget,1,1)

        list_btn_layout = QVBoxLayout()
        list_btn_layout.addWidget(self.list_input)
        list_btn_layout.addWidget(btn_add_item)
        list_btn_layout.addWidget(btn_del_item)
        layout.addLayout(list_btn_layout,1,2)

        layout.addWidget(QLabel("Text Editor:"),2,0)
        layout.addWidget(self.text_editor,2,1)
        layout.addWidget(btn_clear_text,2,2)

        layout.addWidget(QLabel("Table Widget:"),3,0)
        layout.addWidget(self.table,3,1)

        self.tab3.setLayout(layout)

    def init_tab4(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        group_box = QGroupBox("Grup kutusu")
        group_layout = QVBoxLayout()
        group_layout.addWidget(QLabel("Bu alan bir QGroupBox İçerisindedir"))

        h_layout = QHBoxLayout()
        btn_h1 = QPushButton("Yatay buton1")
        btn_h2 = QPushButton("Yatay buton2")
        h_layout.addWidget(btn_h1)
        h_layout.addWidget(btn_h2)
        group_layout.addLayout(h_layout)
        group_box.setLayout(group_layout)

        splitter = QSplitter(Qt.Horizontal)

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.StyledPanel)
        f1_layout = QVBoxLayout()
        self.f1_label = QLabel("Sol Çerçeve(Frame1)")
        btn_f1 = QPushButton("Sağı değiştir")
        f1_layout.addWidget(self.f1_label)
        f1_layout.addWidget(btn_f1)
        frame1.setLayout(f1_layout)

        frame2 = QFrame()
        frame2.setFrameShape(QFrame.StyledPanel)
        f2_layout = QVBoxLayout()
        self.f2_label = QLabel("Sağ Çerçeve(Frame2)")
        f2_layout.addWidget(self.f2_label)
        frame2.setLayout(f2_layout)

        btn_f1.clicked.connect(lambda: self.f2_label.setText("Splitter ile ayrılan alan güncellendi!"))
        splitter.addWidget(frame1)
        splitter.addWidget(frame2)

        main_layout.addWidget(group_box)
        main_layout.addWidget(QLabel("Çerçeve Bölücü:"))
        main_layout.addWidget(splitter)
        main_layout.addStretch()

        self.tab4.setLayout(main_layout)


    def add_list_item(self):
        text = self.list_input.text().strip()
        if text:
            self.list_widget.addItem(text)
            self.list_input.clear()

    def delete_list_item(self):
        for item in self.list_widget.selectedItems():
            self.list_widget.takeItem(self.list_widget.row(item))

    def update_calendar_Date(self):
        date_str = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.calendar_label.setText(f"Seçilen tarih:{date_str}")

    def load_image(self):
        file_path,_ = QFileDialog.getOpenFileName(self, "Resim Aç","","Resimler (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

    def on_submit_clicked(self):
        name = self.entry_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Hata", "Lütfen bir ad giriniz")
            return
        membership = "VIP Üyelik" if self.radio_btn2.isChecked() else "Standart Üyelik"
        agreement = "Onaylandı" if self.checkbox_agree.isChecked() else "Onaylanmadı"
        QMessageBox.information(self, "Sonuç", f"Ad: {name}     Üyelik: {membership}        Şartlar: {agreement}")

    def on_toggle_clicked(self):
        checked = self.btn_toggle.isChecked()
        state = "Açık" if checked else "Kapalı"
        QMessageBox.information(self, "Toggle", f"Buton durumu: {state}")

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_info.setFont(font)
            self.entry_input.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())