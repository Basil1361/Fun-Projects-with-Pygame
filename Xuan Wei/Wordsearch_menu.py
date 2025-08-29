#pip install PyQt6
#pip install pygame
#pip install wonderwords
import sys, copy, pygame, time, os, multiprocessing
import Wordsearch_logic as WS
import Wordsearch_game as WSG

from PIL.ImageQt import QPixmap
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QWidget, QToolTip, QLabel, QHBoxLayout, QPushButton, QApplication, QVBoxLayout, QComboBox,
                             QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt

from pygame.locals import *
from wonderwords import RandomWord
#____________________MENU____________________
class Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1200, 700)
        self.setWindowTitle("Wordsearch Puzzle - Menu")
        self.setWindowIcon(QIcon("Resources/Wordsearch/Image/python.png"))
        QToolTip.setFont(QFont("Arial", 20))

        self.python_img = QPixmap("Resources/Wordsearch/Image/python.png")
        self.python_lbl = QLabel(self)
        self.python_lbl.setPixmap(self.python_img)

        self.wordsearch_lbl = QLabel("Wordsearch Puzzle", self)

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setToolTip("Start the game.\nOpen setup.")
        self.start_btn.clicked.connect(self.clicked_start)

        self.show()


    def resizeEvent(self, event):
        super().resizeEvent(event)

        width = int(self.size().width())
        height = int(self.size().height())
        self.python_lbl.setGeometry(int(width // 2 - 100), int(height * 0.05), 200, 200)
        self.shrunk_python_img = self.python_img.scaled(200, 200, Qt.AspectRatioMode.IgnoreAspectRatio,
                                                            Qt.TransformationMode.SmoothTransformation)
        self.python_lbl.setPixmap(self.shrunk_python_img)

        self.wordsearch_lbl.setFont(QFont("Comic Sans MS", 70))
        self.start_btn.setFont(QFont("Arial", 50))

        self.wordsearch_lbl.adjustSize()
        self.start_btn.adjustSize()
        self.start_btn.resize(self.start_btn.width() + 100, self.start_btn.height())

        self.wordsearch_lbl.move(int(width//2 - self.wordsearch_lbl.width()//2),
                                 int(height*0.5 - self.wordsearch_lbl.height()//2))
        self.start_btn.move(int(width // 2 - self.start_btn.width() // 2),
                                 int(height * 0.8 - self.start_btn.height() // 2))


    def clicked_start(self):
        self.setup_window = Start()
        self.setup_window.show()
        self.close()


#___________________SETUP____________________
class Start(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1200, 700)
        self.setWindowTitle("Wordsearch Puzzle - Setup")
        self.setWindowIcon(QIcon("Resources/Wordsearch/Image/python.png"))
        QToolTip.setFont(QFont("Arial", 20))


        self.difficulty_lbl = QLabel("Difficulty:", self)
        self.difficulty_combo = QComboBox(self)
        self.difficulty_combo.addItems(["Easy (10x10)", "Medium (13x13)", "Hard (17x17)"])

        self.words_lbl = QLabel("Enter words (comma or line seperated):", self)
        self.generate_words_btn = QPushButton("Generate random words", self)
        self.generate_words_btn.clicked.connect(self.generate_random_words)
        self.words_box = QTextEdit(self)
        self.words_box.setPlaceholderText("apple, banana, cat\ndog, elephant")

        self.audio_lbl = QLabel("Audio:", self)
        self.audio_combo = QComboBox(self)
        self.audio_combo.addItem("Off")
        #self.audio_combo.addItem("1-01-Liyue")
        #self.audio_combo.addItem("1-02-Legend_of_the_Wind")
        #self.audio_combo.addItem("1-05-Sun_Rises_in_Liyue")
        self.audio_combo.addItem("On (1-06-Good_Night_Liyue)")
        #self.audio_combo.addItem("1-08-Another_Day_in_Mondstadt")
        #self.audio_combo.addItem("2-02-The_Fading_Stories_Qingce_Night")

        self.theme_lbl = QLabel("Theme:", self)
        self.theme_combo = QComboBox(self)
        self.theme_combo.addItem("Black (Default)")
        self.theme_combo.addItem("Blue")
        #self.theme_combo.addItem("Yellow")

        self.return_btn = QPushButton("Return", self)
        self.return_btn.clicked.connect(self.clicked_return)
        self.return_btn.setToolTip("Go back.")

        self.start_game_btn = QPushButton("Launch pygame", self)
        self.start_game_btn.clicked.connect(self.clicked_start_game)
        self.start_game_btn.setToolTip("Start the game.\nOpen setup.")
        self.show()


    def resizeEvent(self, event):
        super().resizeEvent(event)

        width = int(self.size().width())
        height = int(self.size().height())

        self.difficulty_lbl.setFont(QFont("Arial", 20))
        self.difficulty_combo.setFont(QFont("Arial", 20))
        self.words_lbl.setFont(QFont("Arial", 20))
        self.generate_words_btn.setFont(QFont("Arial", 20))
        self.words_box.setFont(QFont("Arial", 20))
        self.audio_lbl.setFont(QFont("Arial", 20))
        self.audio_combo.setFont(QFont("Arial", 20))
        self.theme_lbl.setFont(QFont("Arial", 20))
        self.theme_combo.setFont(QFont("Arial", 20))
        self.start_game_btn.setFont(QFont("Arial", 40))
        self.return_btn.setFont(QFont("Arial", 40))

        self.difficulty_lbl.adjustSize()
        self.difficulty_combo.adjustSize()
        self.words_lbl.adjustSize()
        self.generate_words_btn.adjustSize()
        self.generate_words_btn.resize(int(self.generate_words_btn.width()+50), int(self.generate_words_btn.height()))
        self.words_box.setGeometry(int(width*0.15), int(height*0.25), int(width*0.7), int(height*0.25))
        self.audio_lbl.adjustSize()
        self.audio_combo.adjustSize()
        self.theme_lbl.adjustSize()
        self.theme_combo.adjustSize()
        self.start_game_btn.adjustSize()
        self.start_game_btn.resize(int(self.start_game_btn.width() + 50), int(self.start_game_btn.height()))
        self.return_btn.adjustSize()
        self.return_btn.resize(int(self.return_btn.width() + 50), int(self.return_btn.height()))

        self.difficulty_lbl.move(int(width*0.15), int(height * 0.1 - self.difficulty_lbl.height() // 2))
        self.difficulty_combo.move(int(width*0.15 + self.difficulty_lbl.width() + 25),
                                    int(height*0.1 - self.difficulty_combo.height() // 2))
        self.words_lbl.move(int(width*0.15), int(height * 0.2 - self.words_lbl.height() // 2))
        self.generate_words_btn.move(int(width*0.85 - self.generate_words_btn.width()), int(height * 0.2 - self.words_lbl.height() // 2))
        self.words_box.move(int(width*0.15), int(height * 0.25))
        self.audio_lbl.move(int(width*0.15), int(height*0.6 - self.audio_lbl.height() // 2))
        self.audio_combo.move(int(width * 0.15 + self.audio_lbl.width() + 25),
                              int(height * 0.6 - self.audio_combo.height() // 2))
        self.theme_lbl.move(int(width * 0.15), int(height * 0.7 - self.theme_lbl.height() // 2))
        self.theme_combo.move(int(width * 0.15 + self.theme_lbl.width() + 25),
                              int(height * 0.7 - self.theme_combo.height() // 2))
        self.start_game_btn.move(int(width * 0.85 - self.start_game_btn.width()),
                                 int(height * 0.85 - self.start_game_btn.height() // 2))
        self.return_btn.move(int(width * 0.15),
                                 int(height * 0.85 - self.return_btn.height() // 2))


    def generate_random_words(self):
        random_word = RandomWord().random_words(10, word_min_length=3, word_max_length=10)
        text = ""
        for x in random_word:
            if random_word[0] == x:
                text = text + x
            else:
                text = text + "\n" + x

        self.words_box.setPlainText(text)

    def clicked_return(self):
        self.setup_window = Menu()
        self.setup_window.show()
        self.close()

    def clicked_start_game(self):
        try:
            order = self.difficulty_combo.currentIndex()
            if order == 0:
                order = 10
            elif order == 1:
                order = 13
            else:
                order = 17

            words_input = self.words_box.toPlainText()
            if not words_input.strip():
                QMessageBox.critical(self, "Input Error", "Please enter at least one word.",
                                    QMessageBox.StandardButton.Ok)
                return
            words = []
            for part in words_input.replace("\n", ",").split(","):
                if part.strip():
                    words.append(part.strip())

            audio = self.audio_combo.currentText()
            theme = self.theme_combo.currentText()


            crossword = WS.create_crossword(order, words)
            crossword_added_letters = WS.add_random_letters(order, copy.deepcopy(crossword))

            crossword_grid = WS.grid_to_str(copy.deepcopy(crossword))
            crossword_added_letters_grid = WS.grid_to_str(crossword_added_letters)
            #print(crossword_grid)
            #print(crossword_added_letters_grid)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        p = multiprocessing.Process(
            target=WSG.run_game,
            args=(order, crossword_added_letters, audio, theme)
        )
        p.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec())
