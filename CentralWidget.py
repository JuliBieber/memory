from PyQt6.QtWidgets import QWidget, QGridLayout

from MyLabel import MyLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button_1 = MyLabel("ara.jpg")
        self.button_2 = MyLabel("cat.jpg")
        self.button_3 = MyLabel("cat.jpg")
        self.button_4 = MyLabel("dog.jpg")
        self.button_5 = MyLabel("fish.jpg")
        self.button_6 = MyLabel("ara.jpg")
        self.button_7 = MyLabel("fish.jpg")
        self.button_8 = MyLabel("dog.jpg")

        self.button_1.card_clicked.connect(self.handel_clicks)
        self.button_2.card_clicked.connect(self.handel_clicks)
        self.button_3.card_clicked.connect(self.handel_clicks)
        self.button_4.card_clicked.connect(self.handel_clicks)
        self.button_5.card_clicked.connect(self.handel_clicks)
        self.button_6.card_clicked.connect(self.handel_clicks)
        self.button_7.card_clicked.connect(self.handel_clicks)
        self.button_8.card_clicked.connect(self.handel_clicks)

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.button_1, 1, 1)
        layout.addWidget(self.button_2, 1, 2)
        layout.addWidget(self.button_3, 1, 3)
        layout.addWidget(self.button_4, 1, 4)

        layout.addWidget(self.button_5, 2, 1)
        layout.addWidget(self.button_6, 2, 2)
        layout.addWidget(self.button_7, 2, 3)
        layout.addWidget(self.button_8, 2, 4)

        self.__last_card_clicked = None

    def handel_clicks(self):
        if self.__last_card_clicked is None:
            self.__last_card_clicked = self.sender()
        else:
            if self.__last_card_clicked.get_image_name() == self.sender().get_image_name() and \
                    self.__last_card_clicked is not self.sender():
                self.sender().set_found()
                self.__last_card_clicked.set_found()

            self.__last_card_clicked = None
