from PyQt5.QtWidgets import (QWidget,QPushButton,QSpinBox,QLabel,QRadioButton,
                             QButtonGroup,QGroupBox,QVBoxLayout,QHBoxLayout)

from PyQt5.QtCore import Qt 
win = QWidget()
win.setWindowTitle("Memorry Card")
win.resize(600,500)
win.move(300,300)

btn_menu = QPushButton("Menu")
btn_rest = QPushButton("Rest")
time_rest = QSpinBox()
time_rest.setValue(30)
lbl_rest = QLabel("minutes")

lbl_qw = QLabel("question")

box_ans = QGroupBox()
box_ans.setTitle("Answers")
rbn_list = list()
rbn_group = QButtonGroup()
for i in range(4):
    rbt = QRadioButton("a")
    rbn_group.addButton(rbt)
    rbn_list.append(rbt)

box_result = QGroupBox()
box_result.setTitle("Result")
lbl_ans = QLabel("ans")
lbl_result = QLabel("result")

btn_check = QPushButton("Check") 

main_line = QVBoxLayout()
line_H1 = QHBoxLayout()
line_H2 = QHBoxLayout()
line_H3 = QHBoxLayout()
line_H4 = QHBoxLayout()

line_H1.addWidget(btn_menu)
line_H1.addStretch(3)
line_H1.addWidget(btn_rest)
line_H1.addWidget(time_rest)
line_H1.addWidget(lbl_rest)

line_H2.addWidget(lbl_qw, alignment=Qt.AlignCenter)


line_H3.addWidget(box_result)
box_result.hide()
line_H3.addWidget(box_ans)

line_H4.addStretch(2)
line_H4.addWidget(btn_check)
line_H4.addStretch(2)

#block result
line_V1 = QVBoxLayout()
line_V1.addWidget(lbl_result, alignment= Qt.AlignLeft)
line_V1.addWidget(lbl_ans, alignment=Qt.AlignCenter)
box_result.setLayout(line_V1)

#block ans
line_V2 = QVBoxLayout()
line_V3 = QVBoxLayout()
line_H5 = QHBoxLayout()
line_V2.addWidget(rbn_list[0])
line_V2.addWidget(rbn_list[1])
line_V3.addWidget(rbn_list[2])
line_V3.addWidget(rbn_list[3])
line_H5.addLayout(line_V2)
line_H5.addLayout(line_V3)
box_ans.setLayout(line_H5)


 
main_line.addLayout(line_H1)
main_line.addLayout(line_H2)
main_line.addLayout(line_H3)
main_line.addLayout(line_H4)

win.setLayout(main_line)
