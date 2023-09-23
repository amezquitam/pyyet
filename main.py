import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class PostCard(QWidget):
    def __init__(self, text, background_color):
        super().__init__()

        self.text = text
        self.background_color = background_color

        self.initUI()

    def initUI(self):
        self.setStyleSheet(f"background-color: {self.background_color}; margin: 5px 10px; padding: 10px;")

        self.text_button = QPushButton(self.text)
        self.text_button.setStyleSheet("border: none; font-size: 16px;")
        self.text_button.clicked.connect(self.changeColor)

        layout = QVBoxLayout()
        layout.addWidget(self.text_button)
        self.setLayout(layout)

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()}; margin: 5px 10px; padding: 10px;")

class SocialMediaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #1f2324")

        self.setWindowTitle('Publicaciones')
        self.setGeometry(650, 90, 500, 900)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none; background-color: #121414;")

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area.setWidget(self.scroll_widget)

        self.addButton = QPushButton("Agregar Publicación")
        self.addButton.setStyleSheet(
            """
            background-color: #1f2324;
            border: 1px solid #18b4cc;
            color: #fff;
            padding: 15px 8px;
            font-size: 17px;
            """
        )
        self.addButton.clicked.connect(self.addPost)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.addButton)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

    def addPost(self):
        text, ok = PostInputDialog.getText()
        if ok:
            background_color = QColorDialog.getColor()
            if background_color.isValid():
                post_card = PostCard(text, background_color.name())
                self.scroll_layout.addWidget(post_card)

class PostInputDialog(QWidget):
    @staticmethod
    def getText():
        text, ok = QInputDialog.getText(None, "Nueva Publicación", "Escribe tu publicación:")
        return text, ok

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SocialMediaApp()
    window.show()
    sys.exit(app.exec_())
