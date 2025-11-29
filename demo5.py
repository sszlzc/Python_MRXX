# 开发机构 : 涠洲消防救援
# 开发人员 : CG_cheng
# 开发时间 : 2025/11/29 上午9:48

"""计算0到100之间的偶数和"""
sum = 0
a = 1
'''条件判断'''
while a <= 100:
    '''条件执行体(求和)'''
    if a % 2:
        pass
    else:
        sum += a
    a += 1
print('0到100之间的偶数和为：', sum)

# 16进制文本转10进制数：
hex_str = 'a8:a2:3a:7a:4e:e0:30:fd'
'''去除冒号'''
hex_str = hex_str.replace(':', '')
a = int('0x' + hex_str, 16)
print(a)
# 转换为64位有符号整数
a = int(hex_str, 16)
# 判断最高位是否为1，如果是，则将其转换为负数
if a & (1 << 63):
    a -= 1 << 64
print(a)

