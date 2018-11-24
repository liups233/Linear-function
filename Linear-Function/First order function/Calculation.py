print('输入关系式 y=kx+b')
k = float(input('输入k: '))
while k == 0:
    print('''
k不能为0
    ''')
    k = float(input('输入k: '))
b = float(input('输入b: '))
mode = int(input('已知x求y输入1 已知y求x输入2: '))
if mode == 1:
    enter_x = float(input('输入x: '))
    result_y = k*enter_x+b
    print('y值为:', result_y)
elif mode == 2:
    enter_y = float(input('输入y: '))
    result_x = (enter_y-b)/k
    print('x值为:', result_x)
