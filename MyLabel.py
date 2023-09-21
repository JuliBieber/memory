from PyQt6.QtCore import QSize, QTimer, pyqtSlot
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyLabel(QLabel):
    def __init__(self, image_name, parent=None):
        super().__init__(parent)

        self.__image_name = image_name
        self.__is_turned = True

        pixmap_size = QSize(200, 200)

        self.__icon_background = QPixmap("questionmark.jpeg").scaled(pixmap_size)
        self.__icon_symbol = QPixmap(image_name).scaled(pixmap_size)

        self.setPixmap(self.__icon_background)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.turn_card)
        self.__timer.setSingleShot(True)

    def mousePressEvent(self, ev) -> None:
        if self.__is_turned:
            self.setPixmap(self.__icon_symbol)
            self.__is_turned = False

            self.__timer.start(3 * 1000)

    @pyqtSlot()
    def turn_card(self):
        print("got a call")

        if not self.__is_turned:
            self.setPixmap(self.__icon_background)
            self.__is_turned = True
