# 开发机构 : 涠洲消防救援
# 开发人员 : CG_cheng
# 开发时间 : 2025/11/29 上午9:29

"""内置函数range()的用法"""

# range()的三种创建方式
r = range(10)
print(r)  # range(0, 10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 指定起始值和终止值
r = range(2, 10)
print(r)  # range(2, 10)
print(list(r))  # [2, 3, 4, 5, 6, 7, 8, 9]
# 指定步长
r = range(0, 10, 2)
print(r)  # range(1, 10, 2)
print(list(r))  # [0, 2, 4, 6, 8]

'''判断指定的整数 在序列中是否存在 in, not in'''
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)

# 以下两行内存占用相同，但range()创建的对象不同
print(range(1, 20, 1))
print(range(1, 101, 1))
