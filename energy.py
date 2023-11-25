import random
#import time

#把获取到标签数值信息放在x列表中
def ys():
    
    global id1
    for i in range(5):
        x.append(list1[id1])
        id1= id1+5


#判断识别到的符号是+ - * /中的哪一个
def panduan():
    global fuhao
    ys()
    id3=0
    for i in range(5):
        if int(x[id3])>40:
            fuhao=x[id3]
            break
        else:
            id3=id3+1
    fuhao=int(fuhao)
    if fuhao==43:#乘法
        chengfa()
    elif fuhao==50:#加法
        jiafa()
    elif fuhao==51:#减法
        jianfa()
    elif fuhao==52:#除法
        chufa()

#获取abcd在原列表list1的索引值
def shujvpaixv():
    global a1
    global b1
    global c1
    global d1
    global fuhaoid
    k = 0
    k1 =2
    for i in range(5):
        if int(x[k]) == int(list1[k1]):
            a1=k1
            x[k] = x[k]*10
            list1[k1] = list1[k1]*10
            k1 = k1+5
        elif int(x[k+1]) == int(list1[k1]):
            x[k+1] = x[k+1]*20
            list1[k1] = list1[k1]*20
            b1=k1
            k1 = k1+5
        elif int(x[k+2]) == int(list1[k1]):
            x[k+2] = x[k+2]*300
            list1[k1] = list1[k1]*300
            c1=k1
            k1 = k1+5
        elif int(x[k+3]) == int(list1[k1]):
            x[k+3] = x[k+3]*4000
            list1[k1] = list1[k1]*4000
            d1=k1
            k1 = k1+5
        elif int(list1[k1])>40:
            fuhaoid = k1
            list1[k1] = list1[k1]*30000
            k1 = k1+5
        else:
            k1 = k1+5
#删除x列表中的符号的数据
def del1():
    id2 =0
    while not id2 >= 5 :
        if x[id2]>40:
            del x[id2]
            break
        else:
            id2=id2+1
#射击方式1(a b c d)
def shoot1():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1+1] - 0.5) * hx,(0.5 - list1[a1 + 2]) * fy)#云台旋转到航向轴（）俯仰轴（）
    gun_ctrl.fire_once()#单次发射水弹
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid+1] - 0.5) * hx,(0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx,(0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx,(0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx,(0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[d1 + 1] - 0.5) * hx, (0.5 - list1[d1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)

#射击方式2(a b c)
def shoot2():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1 + 1] - 0.5) * hx, (0.5 - list1[a1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx, (0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx, (0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)

#射击方式3(ab cd)
def shoot3():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1 + 1] - 0.5) * hx, (0.5 - list1[a1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx, (0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx, (0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[d1 + 1] - 0.5) * hx, (0.5 - list1[d1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)

#射击方式4（ab c）
def shoot4():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1 + 1] - 0.5) * hx, (0.5 - list1[a1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx, (0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx, (0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)

#射击方式5（abc d）
def shoot5():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1 + 1] - 0.5) * hx, (0.5 - list1[a1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx, (0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx, (0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[d1 + 1] - 0.5) * hx, (0.5 - list1[d1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)

#射击方式6(ab c d)
def shoot6():
    shujvpaixv()
    gun_ctrl.set_fire_count(1)
    gimbal_ctrl.angle_ctrl((list1[a1 + 1] - 0.5) * hx, (0.5 - list1[a1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[b1 + 1] - 0.5) * hx, (0.5 - list1[b1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[c1 + 1] - 0.5) * hx, (0.5 - list1[c1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[fuhaoid + 1] - 0.5) * hx, (0.5 - list1[fuhaoid + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)
    gimbal_ctrl.angle_ctrl((list1[d1 + 1] - 0.5) * hx, (0.5 - list1[d1 + 2]) * fy)
    gun_ctrl.fire_once()
    time.sleep(time1)


#random.shuffle(x)对列表中的数据进行随机排序
#加法运算
def jiafa():
    del1()
    while True:
        random.shuffle(x)
        a=int(x[0])-10
        b=int(x[1])-10
        c=int(x[2])-10
        d=int(x[3])-10
        if (a*10)+b+(c*10)+d ==24:
            shoot3()
            break
        elif a+b+c+d == 24:
            shoot1()
            break
        elif a+b+c ==24:
            shoot2()
            break
        elif (a*10+b)+c == 24:
            shoot4()
            break
        elif (a*10+b)+c+d == 24:
            shoot6()
            break
#乘法运算
def chengfa():
    del1()
    while True:
        random.shuffle(x)
        a=int(x[0])-10
        b=int(x[1])-10
        c=int(x[2])-10
        d=int(x[3])-10
        if a*b*c*d == 24:
            shoot1()
            break
        elif a*b*c == 24:
            shoot2()
            break
        elif (a*10+b)*c*d == 24:
            shoot6()
            break
        elif (a*10+b)*c==24:
            shoot4()
            break
#减法运算
def jianfa():
    del1()
    while True:
        random.shuffle(x)
        a=int(x[0])-10
        b=int(x[1])-10
        c=int(x[2])-10
        d=int(x[3])-10
        if (a*10+b)-c-d == 24:
            shoot6()
            break
        elif (a*10+b)-c == 24:
            shoot4()
            break
        elif (a*10+b)-(c*10+d) == 24:
            shoot3()
            break
#除法运算
def chufa():
    del1()
    while True:
        random.shuffle(x)
        a=int(x[0])-10
        b=int(x[1])-10
        c=int(x[2])-10
        d=int(x[3])-10
        if (a*10+b)/c/d ==24:
            shoot6()
            break
        elif (a*10+b)/c == 24:
            shoot4()
            break
        elif (a*100+b*10+c)/d == 24:
            shoot5()
            break
def ZHS():
    global list1
    robot_ctrl.set_mode(rm_define.robot_mode_free)#整机运动模式（自由模式）
    gimbal_ctrl.recenter()#控制云台回中
    gun_ctrl.set_fire_count(1)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)#开启视觉标签识别
    gimbal_ctrl.set_rotate_speed(540)#云台旋转速度 1-540
    for i in range(500):
        vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_blue)#设置识别的视觉标签颜色
        list1=RmList(vision_ctrl.get_marker_detection_info())#把识别到的视觉标签信息存储在列表名为list1的列表中
        vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)#设置识别的视觉标签颜色
        list1=RmList(vision_ctrl.get_marker_detection_info())#把识别到的视觉标签信息存储在列表名为list1的列表中
        if len(list1) == 26:
            break
    print(list1)
    panduan()#运行自定义函数
while not (vision_ctrl.check_condition(rm_define.cond_recognized_marker_letter_A)):
    list1 = RmList()
    a1=0
    b1=0
    c1=0
    d1=0
    fuhao = 0
    fuhaoid=0
    hx = 110
    fy = 70
    time1 = 0.08
    id1= 2
    id2 = 1
    x=[]
    ZHS()
    time.sleep(0.5)
        