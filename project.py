import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QWidget, QVBoxLayout, QCheckBox, QScrollArea
from PyQt5.QtCore import Qt, QTimer
from core import choice_generator, checker, review_choice_generator, review_editWord, editWordCheck, editWordRemove

class ReviewWordList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Word List')
        self.setGeometry(1400,165,250,750)
        self.initUI()

    def initUI(self):
        review_list = review_editWord()

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        content = QWidget()
        scroll.setWidget(content)
        
        
        layout = QVBoxLayout(content)
        for word in review_list:
            checkbox = QCheckBox(word, self)
            checkbox.setStyleSheet('font-size: 18px')
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(lambda state, w=word: self.checkboxEdit(w,state))
            layout.addWidget(checkbox)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)


    def checkboxEdit(self, word, state):
        if state == Qt.Checked:
            editWordCheck(word)
        else:
            editWordRemove(word)


class ReviewList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Review List')
        self.setGeometry(535,165,850,750)
        self.initUI()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.load_new_word)
    
    def initUI(self):
        
        temp = review_choice_generator()
        self.random1, self.random2, self.tWord = temp[0]
        self.meaning = temp[1]
        

        label = QLabel('Words you should work on', self)
        label.setGeometry(0,50,850,50)
        label.setStyleSheet('font-size: 25px')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        self.back= QPushButton('Back',self)
        self.back.setGeometry(25,25,110,27)
        self.back.setStyleSheet('font-size: 16px; background-color: #3dd44a;')
        self.back.clicked.connect(self.back_click)


        self.word = QLabel(self.tWord ,self)
        self.word.setGeometry(0,150,850,50)
        self.word.setStyleSheet('font-size: 35px')
        self.word.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.choice1 = QPushButton(self.random1,self)
        self.choice1.setGeometry(150,290,250,100)
        self.choice1.setStyleSheet('font-size: 25px')
        self.choice1.clicked.connect(self.on_click)

        self.choice2 = QPushButton(self.random2,self)
        self.choice2.setGeometry(450,290,250,100)
        self.choice2.setStyleSheet('font-size: 25px')
        self.choice2.clicked.connect(self.on_click)

        self.reviewWords = QPushButton('Edit Words',self)
        self.reviewWords.setGeometry(715,25,115,27)
        self.reviewWords.setStyleSheet('font-size: 16px;' 'background-color: #5caeed')
        self.reviewWords.clicked.connect(self.reviewClick)

        self.load_new_word()

    def on_click(self):
        
        for self.temp in self.choice1, self.choice2:
            self.temp.setText(self.meaning) 
            self.temp.setStyleSheet('font-size: 31px; color: green;')
        
        for button in [self.choice1, self.choice2]:
            button.setEnabled(False)
        
        self.timer.start(2000)
    
    def load_new_word(self):
        temp = review_choice_generator()
        self.random1, self.random2, self.tWord = temp[0]
        self.meaning = temp[1]

        self.word.setText(self.tWord)
        self.choice1.setText(self.random1)
        self.choice2.setText(self.random2)

        for button in [self.choice1, self.choice2]:
            button.setStyleSheet('font-size: 25px')
            button.setEnabled(True)
        

    def back_click(self):        
        self.back_window = MainWindow()
        self.back_window.show()
        self.close()

    def reviewClick(self):
        self.wordWindow= ReviewWordList()
        self.wordWindow.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Word Quiz')
        self.setGeometry(535,165,850,750)
        self.streak_count = 0
        self.initUI()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.load_new_word)
        

    def initUI(self):
        temp = choice_generator()
        self.random1, self.random2, self.random3, self.random4, self.tWord = temp[0]
        self.mean = temp[1]

        self.streak = QLabel(f'Streak: {self.streak_count}', self)
        self.streak.setGeometry(0,200,850,50)
        self.streak.setStyleSheet('font-size: 25px')
        self.streak.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        label = QLabel('what is the meaning of', self)
        label.setGeometry(0,50,850,50)
        label.setStyleSheet('font-size: 25px')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        
        self.word = QLabel(self.tWord ,self)
        self.word.setGeometry(0,125,850,50)
        self.word.setStyleSheet('font-size: 35px')
        self.word.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)



        self.choice1 = QPushButton(self.random1,self)
        self.choice1.setGeometry(150,290,250,100)
        self.choice1.setStyleSheet('font-size: 25px')
        self.choice1.clicked.connect(self.on_click)

        self.choice3 = QPushButton(self.random2,self)
        self.choice3.setGeometry(150,430,250,100)
        self.choice3.setStyleSheet('font-size: 25px')
        self.choice3.clicked.connect(self.on_click)

        self.choice2 = QPushButton(self.random3,self)
        self.choice2.setGeometry(450,290,250,100)
        self.choice2.setStyleSheet('font-size: 25px')
        self.choice2.clicked.connect(self.on_click)


        self.choice4 = QPushButton(self.random4,self)
        self.choice4.setGeometry(450,430,250,100)
        self.choice4.setStyleSheet('font-size: 25px')
        self.choice4.clicked.connect(self.on_click)

        self.dont_know = QPushButton("I don't know",self)
        self.dont_know.setGeometry(150,600,550,100)
        self.dont_know.setStyleSheet('font-size: 30px;' 'background-color: #f2f20a')
        self.dont_know.clicked.connect(self.dknow_click)


        self.reviewButton = QPushButton('Review Words',self)
        self.reviewButton.setGeometry(710,25,120,27)
        self.reviewButton.setStyleSheet('font-size: 16px;' 'background-color: #5caeed')
        self.reviewButton.clicked.connect(self.review_click)

        self.load_new_word()

    def load_new_word(self):
        temp = choice_generator()
        self.random1, self.random2, self.random3, self.random4, self.tWord = temp[0]
        self.mean = temp[1]

        self.word.setText(self.tWord)
        self.choice1.setText(self.random1)
        self.choice2.setText(self.random2)
        self.choice3.setText(self.random3)
        self.choice4.setText(self.random4)

        for button in [self.choice1, self.choice2, self.choice3, self.choice4, self.dont_know]:
            button.setStyleSheet('font-size: 25px')
            button.setEnabled(True)
            self.dont_know.setStyleSheet('background-color: #f2f20a; font-size: 30px')
    
    def on_click(self):
        selected_answer = self.sender().text()
        
        if checker(self.tWord, selected_answer, self.mean):
            self.streak_count += 1
        else:
            self.streak_count = 0
        self.streak.setText(f'Streak: {self.streak_count}')

        for self.temp in self.choice1, self.choice2, self.choice3, self.choice4:
            self.temp.setText(self.mean) 
            self.temp.setStyleSheet('font-size: 31px; color: green;')
        
        for button in [self.choice1, self.choice2, self.choice3, self.choice4]:
            button.setEnabled(False)
        
        self.timer.start(2000)
                
    def dknow_click(self):
        checker(self.tWord,self.sender().text(),'')
        
        for self.temp in self.choice1, self.choice2, self.choice3, self.choice4:
            self.temp.setText(self.mean)
            self.temp.setStyleSheet('font-size: 35px; color: green;')
        for button in [self.choice1, self.choice2, self.choice3, self.choice4, self.dont_know]:
            button.setEnabled(False)
        
        self.timer.start(2000)

    def review_click(self):
        if not review_choice_generator():
            self.show_popup()
        else:
            self.review_window = ReviewList()
            self.review_window.show()
            self.close()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("No words in the review list")
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  