# 제어문 조건문 실습
# if ...:

num = 60
if 80 < num:
    print('A')
else:
    print('B')

num = 99
if 80 < num:
    print('A')
else:
    print('B')

num = 99
# 80 초과 A
if 80 < num:
    print('A')
# 70 초과 B
elif 70 < num:
    print('B')
# 60 초과 C
elif 60 < num:
    print('C')
# 나머지 D
else:
    print('D')