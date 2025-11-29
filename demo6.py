# 开发机构 : 涠洲消防救援
# 开发人员 : CG_cheng
# 开发时间 : 2025/11/29 上午10:56


"""
for-in 循环
for 自定义变量 in 可迭代对象:
    循环体
    ...

for-in 循环可以遍历可迭代对象中的每个元素，并将元素赋值给自定义变量。
"""
for item in 'Python':
    print(item)

# range()函数可以生成一个整数序列，可以用for-in循环来遍历这个序列。
for i in range(10):
    print(i)

# 如果在循环体中不需要使用自定义变量，可以用下划线(_)表示。
for _ in range(5):
    print('Hello, world!')

# 使用for循环计算1到100的偶数和。
sum = 0
for i in range(0, 101, 2):
    sum += i
print('1到100的偶数和为：', sum)

# 输出100到999之间的水仙花数。
for num in range(100, 1000):
    # 计算每一个三位数的个位、十位、百位数字的和
    hundreds = num // 100
    tens = (num % 100) // 10
    ones = num % 10
    # print(hundreds, tens, ones)
    # 判断是否为水仙花数
    if hundreds ** 3 + tens ** 3 + ones ** 3 == num:
        print(num)
