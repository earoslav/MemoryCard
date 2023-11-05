from PyQt5.QtWidgets import QApplication,QMessageBox#імпорт всього що нада
from random import shuffle,choice#імпорт з рандому



app = QApplication([])#створюємо додаток

from data import qwList, Qwestion
from main_win import*#імпортуємо з мейну все
from edit_win import*
choce_ans = ""
qw = ""
def stat():
    count = 0
    count_r = 0
    good = 0
    for q in qwList:
        count+=q.count
        count_r+=q.count_right
    if count!=0:    
        good = (count_r/count)*100  
    else:
        good=0   
    lbl_count.setText(f"кількість відповідей {count}")  
    lbl_count_right.setText(f"кількість правельних відповідей {count_r}")
    lbl_good.setText(f"процент правельних відповідей {good}")

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
        
def show_menu():
    stat()
    win.hide()
    win_edit.show()        
   
def show_test():
    win_edit.hide()
    win.show()
def clear():
    edit_ans.clear()
    edit_qw.clear()
    edit_wrg1.clear()
    edit_wrg2.clear()
    edit_wrg3.clear()


def add_qw():
    qw_text = edit_qw.text()
    ans_text = edit_ans.text()
    wg1_text = edit_wrg1.text()
    wg2_text = edit_wrg2.text()
    wg3_text = edit_wrg2.text()
    if qw!="" and ans_text!="" and wg1_text!= "" and wg2_text!="" and wg3_text!="":
        q = Qwestion(qw_text, ans_text, wg1_text, wg2_text, wg3_text)
        qwList.append(q)
        clear()
    else:
        mess_wg = QMessageBox()
        mess_wg.setText("ДОПИШИ")
        mess_wg.show()
        mess_wg.exec()

def click_ans(rbn):
    global choce_ans
    choce_ans = rbn.text()

new_qw()

btn_menu.clicked.connect(show_menu)
btn_back.clicked.connect(show_test)
btn_clear.clicked.connect(clear)
btn_add_qw.clicked.connect(add_qw)

rbn_group.buttonClicked.connect(click_ans)
btn_check.clicked.connect(check_ans)

win.show()#показати вікно
app.exec()#додаток закривається після нажаття на хрестик