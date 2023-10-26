from PyQt5.QtWidgets import (QWidget,QPushButton,QSpinBox,QLabel,QRadioButton,#імпортуємо все що потрібно
                             QButtonGroup,QGroupBox,QVBoxLayout,QHBoxLayout)

from PyQt5.QtCore import Qt 
win = QWidget()#Настройка вікна(створення заголовок розмір місце)
win.setWindowTitle("Memorry Card")#
win.resize(600,500)#
win.move(300,300)#

btn_menu = QPushButton("Menu")#створюємо кнопку
btn_rest = QPushButton("Rest")#створюємо кнопку
time_rest = QSpinBox()#створ. спін бокс
time_rest.setValue(30)#задаємо значення 30
lbl_rest = QLabel("minutes")#напис створ.

lbl_qw = QLabel("question")#задаємо текст напису

box_ans = QGroupBox()#створ. груп бокс
box_ans.setTitle("Answers")#встан. заголовок груп боксу
rbn_list = list()#ств. список радіокнопок
rbn_group = QButtonGroup()#створ. груп бокс для радіобатонів
for i in range(4):#цикл
    rbt = QRadioButton("a")#ств радіокнопку
    rbn_group.addButton(rbt)#додаємо радіокнопку до групи
    rbn_list.append(rbt)#додаємо радіокнопку до списку

box_result = QGroupBox()#створ. груп бокс
box_result.setTitle("Result")#встан. заголовок груп боксу
lbl_ans = QLabel("ans")#напис створ.
lbl_result = QLabel("result")#напис створ.

btn_check = QPushButton("Check") #створюємо кнопку

main_line = QVBoxLayout()#ств головний лейаут
line_H1 = QHBoxLayout()#ств горизантальний лейаут
line_H2 = QHBoxLayout()#ств горизантальний лейаут
line_H3 = QHBoxLayout()#ств горизантальний лейаут
line_H4 = QHBoxLayout()#ств горизантальний лейаут

line_H1.addWidget(btn_menu)#додаємо до лейаута віджети
line_H1.addStretch(3)#додаємо до лейаута відступи
line_H1.addWidget(btn_rest)#додаємо до лейаута віджети
line_H1.addWidget(time_rest)#додаємо до лейаута віджети
line_H1.addWidget(lbl_rest)#додаємо до лейаута віджети

line_H2.addWidget(lbl_qw, alignment=Qt.AlignCenter)#додаємо до лейаута віджети


line_H3.addWidget(box_result)#додаємо до лейаута віджети
box_result.hide()#ховаємо напис
line_H3.addWidget(box_ans)#додаємо до лейаута віджети

line_H4.addStretch(2)#додаємо до лейаута відступи
line_H4.addWidget(btn_check)#додаємо до лейаута віджети
line_H4.addStretch(2)#додаємо до лейаута відступи

#block result
line_V1 = QVBoxLayout()#ств вертикальний лейаут
line_V1.addWidget(lbl_result, alignment= Qt.AlignLeft)#додаємо до лейаута віджети(розташування з ліва)
line_V1.addWidget(lbl_ans, alignment=Qt.AlignCenter)#додаємо до лейаута віджети(розташування по центру)
box_result.setLayout(line_V1)#встановлюємо в груп боксі лей аут

#block ans
line_V2 = QVBoxLayout()#ств вертикальний лейаут
line_V3 = QVBoxLayout()#ств вертикальний лейаут
line_H5 = QHBoxLayout()#ств горизантальний лейаут
line_V2.addWidget(rbn_list[0])#додаємо до лейаута віджети
line_V2.addWidget(rbn_list[1])#додаємо до лейаута віджети
line_V3.addWidget(rbn_list[2])#додаємо до лейаута віджети
line_V3.addWidget(rbn_list[3])#додаємо до лейаута віджети
line_H5.addLayout(line_V2)#додаємо до лейаута віджети
line_H5.addLayout(line_V3)#додаємо до лейаута віджети
box_ans.setLayout(line_H5)#додаємо до лейаута віджети


 
main_line.addLayout(line_H1)#додаємо до головного лейаута лейаути
main_line.addLayout(line_H2)#додаємо до головного лейаута лейаути
main_line.addLayout(line_H3)#додаємо до головного лейаута лейаути
main_line.addLayout(line_H4)#додаємо до головного лейаута лейаути

win.setLayout(main_line)#додаємо до вікна головний лейаут
