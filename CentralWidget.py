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
