#利用Event类模拟红绿灯
import threading
import time

event = threading.Event()
a = 0
b = time.time()
while(True):
    try:
        speed = float(input("speed"))
        if(speed == 0):
            print("try agein")
            continue
        break
    except:
        print("try agegin")

c = 1/speed



def lighter():
    count = 0
    event.set()     #初始值为绿灯
    while True:
        if 5 < count <=10 :
            event.clear()  # 红灯，清除标志位
            print("\33[41;1m考试 \033[0m")
        elif count > 10:
            event.set()  # 绿灯，设置标志位
            count = 0
        else:
            print("\33[42;1m放假\033[0m")

        time.sleep(c)
        count += 1

def car(name):
    global a
    while True:
        if (a == 1):
            print(time.time() - b)
            a = 0
        if event.is_set():      #判断是否设置了标志位
            print("[%s] 玩"%name)
            time.sleep(c)
        else:
            print("[%s] 玩鬼！"%name)
            event.wait()
            print("[%s] 继续"%name)

light = threading.Thread(target=lighter,)
light.start()
time.sleep(5)
car1 = threading.Thread(target=car,args=("学生1",))
car2 = threading.Thread(target=car,args=("学生2",))
car1.start()
time.sleep(5)
car2.start()
a = 1