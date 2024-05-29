# 반복문 퀴즈

for index in range(5):  # [0,1,2,3,4]
    print(index)

# 출력 형태
# *
# **
# ***
# ****
# *****
for index in range(6):  # [0,1,2,3,4]
    print("*" * index)

# *****
# ****
# ***
# **
# *
for index in [5,4,3,2,1]:
    print("*" * index)

# VVVV*
# VVV**
# VV***
# V****
# *****
for index in [1, 2, 3, 4, 5]:  # range()5
    print(' ' * (5 - index), end='')
    print('*' * index, end='')
    print()