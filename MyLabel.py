from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, image_name, parent=None):
        super().__init__(parent)

        self.__image_name = image_name

        pixmap_size = QSize(200, 200)

        self.__icon_background = QPixmap("questionmark.jpeg").scaled(pixmap_size)
        self.__icon_symbol = QPixmap(image_name).scaled(pixmap_size)

        self.setPixmap(self.__icon_background)
