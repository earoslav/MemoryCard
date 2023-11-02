class Qwestion:
    def __init__(self, qw, ans, wg1, wg2, wg3):
        self.qw = qw
        self.ans = ans
        self.wg1 = wg1
        self.wg2 = wg2
        self.wg3 = wg3
        self.count = 0
        self.count_right = 0
    def right_ans(self):
        self.count+=1
        self.count_right+=1
    def wg_ans(self):
        self.count+=1



qw1 = Qwestion("Скільки ніг у риби", "0", "2", "5", "3")
qw2 = Qwestion("Скільки років живуть кактуси", "200-300 років", "2 роки", "23 роки", "500-600 років")
qw3 = Qwestion("Якого розміру у страуса мозок", "як горішок", "як у людини", "як у тебе", "як у пк")
qw4 = Qwestion("Який птах можу літати задом-на-перед", "колібрі", "чайка", "папуга", "курка")
qwList = [qw1, qw2, qw3, qw4]
