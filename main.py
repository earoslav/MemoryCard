from PyQt5.QtWidgets import QApplication,QMessageBox#імпорт всього що нада
from random import shuffle,choice#імпорт з рандому
from data import qwList

app = QApplication([])#створюємо додаток

from main_win import*#імпортуємо з мейну все

choce_ans = ""
qw = ""

def new_qw():
    global qw
    qw_text = lbl_qw.text()
    qw = choice(qwList)
    while qw_text == qw.qw:
        qw = choice(qwList)
   
    answers = [qw.ans, qw.wg1, qw.wg2, qw.wg3]    
    shuffle(answers)
    for i in range(4):
        rbn_list[i].setText(answers[i])
    lbl_qw.setText(qw.qw)  
    
def null_ans():
    global choce_ans
    choce_ans = ''
    rbn_group.setExclusive(False)
    for i in range(4):
        rbn_list[i].setChecked(False)
    rbn_group.setExclusive(True)
def check_ans():
    if btn_check.text() == "Check":
        if choce_ans == "":
            mess = QMessageBox()
            mess.setText("chose your answer")
            mess.show()

            mess.exec()
        else:    
            if choce_ans == qw.ans:
                lbl_result.setText("Well done")
                qw.right_ans()
            else:
                lbl_result.setText("Not good")
                qw.wg_ans()
            lbl_ans.setText(qw.ans)
            btn_check.setText("Next")
            box_ans.hide()
            box_result.show()
    else:
        new_qw()
        null_ans()
        btn_check.setText("Check")
        box_result.hide()
        box_ans.show()
        
        

def click_ans(rbn):
    global choce_ans
    choce_ans = rbn.text()

new_qw()

rbn_group.buttonClicked.connect(click_ans)
btn_check.clicked.connect(check_ans)

win.show()#показати вікно
app.exec()#додаток закривається після нажаття на хрестик