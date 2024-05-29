# 연산자 실습
# 산술, 비교, 논리

# 변수 선언

v_int1 = 7
v_int2 = 10
v_float1 = 10.0
v_float2 = 23.9
v_num = -99

# +, -, *, /
print(v_int1 + v_int2)
print(v_float1 + v_float2)

print(v_int1 - v_int2)
print(v_float1 - v_float2)

print(v_int1 * v_int2)
print(v_float1 * v_float2)

print(v_int1 / v_int2)
print(v_float1 / v_float2)

result = v_int1 + v_int2
print(result)

v_str1 = 'str1'
v_str2 = 'str2'
v_str3 = "str3"
v_str4 = """
str4"""
v_str5 = '''str5
'''

print(v_str1 + v_str1)
# print(v_str1 - v_str1)

# 비교 연산자
# == != > >= < <=
print(1 == 1)  # 같은지
print(1 != 1)  # 다른지
print(1 > 1)  # 좌측이 큰지
print(1 >= 1)  # 좌측이 크거나 같은지
print(1 < 1)  # 우측이 큰지
print(1 <= 1)  # 우측이 크거나 같은지

print(1 == '1')

# 논리 연산자
# and, or, not
print(1 == 1 and 2 == 2)  #
print(1 == 1 and 2 != 2)  #

print(1 == 1 or 2 == 2)  #
print(1 == 1 or 2 != 2)  #

print(1 == 1)  # True
print(not 1 == 1)  # False
