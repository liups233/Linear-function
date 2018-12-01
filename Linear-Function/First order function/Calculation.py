def computing():
    print('输入关系式 y=kx+b')

    while True:
        k = input('输入k: ')
        if k.replace('.', '') == '0':
            print('''
k不能为0
            ''')
            continue  # 判断k是否为0

        if k.replace('.', '').isdigit():
            k = float(k)
            break  # 判断k是否为数字

        else:
            print('''
k必须输入数字!
            ''')

    while True:
        b = input('输入b: ')
        if b.replace('.', '').isdigit():
            b = float(b)
            break  # 判断b是否为数字

        else:
            print('''
b必须输入数字!
            ''')

    while True:
        mode1 = input('已知x求y输入1 已知y求x输入2: ')
        if mode1 == '1':

            while True:
                enter_x = input('输入x: ')
                if enter_x.replace('.', '').isdigit():
                    enter_x = float(enter_x)
                    break  # 判断输入的x是否为数字

                else:
                    print('''
x必须输入数字!
                    ''')

            result_y = k*enter_x+b
            print('y值为:', result_y)  # 已知x求y
            break
        elif mode1 == '2':

            while True:
                enter_y = input('输入y: ')
                if enter_y.replace('.', '').isdigit():
                    enter_y = float(enter_y)
                    break  # 判断输入的y是否为数字

                else:
                    print('''
y必须输入数字!
                    ''')

            result_x = (enter_y-b)/k
            print('x值为:', result_x)  # 已知y求x
            break
        else:
            print('''
只能输入1或2!
            ''')
            

while True:
    computing()  # 调用computing函数
    mode2 = input('继续计算输入1, 退出输入2: ')
    if mode2 == '1':
        continue
    elif mode2 == '2':
        break
    else:
        while True:
            print('''
只能输入1或2!
                    ''')
            mode2 = input('继续计算输入1, 退出输入2: ')
            if mode2 == '1':
                break
            elif mode2 == '2':
                break
            else:
                continue
        break
