from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, image_name, parent=None):
        super().__init__(parent)

        self.__image_name = image_name
        self.__is_turned = False

        pixmap_size = QSize(200, 200)

        self.__icon_background = QPixmap("questionmark.jpeg").scaled(pixmap_size)
        self.__icon_symbol = QPixmap(image_name).scaled(pixmap_size)

        self.setPixmap(self.__icon_background)

    def mousePressEvent(self, ev) -> None:
        if self.__is_turned:
            self.setPixmap(self.__icon_background)
            self.__is_turned = False
        else:
            self.setPixmap(self.__icon_symbol)
            self.__is_turned = True
