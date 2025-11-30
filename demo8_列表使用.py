# 开发机构 : 涠洲消防救援
# 开发人员 : CG_cheng
# 开发时间 : 2025/11/30 上午9:55

# a = 10
# lst = ['hello', 'world', 98]
# print(id(lst))
# print(type(lst))
# print(lst)

"""列表创建方式"""
# 直接赋值创建列表
# lst = ['hello', 'world', 98]

# 使用list()函数创建列表
lst2 = list(['hello', 'world', 98])


"""
列表元素按顺序有序排序
索引映射唯一数据,可以用负数索引从后往前索引,也可以用从0开始的正整数索引
列表可以储存重复数据
任意数据类型混存
根据需要动态分配和回收内存
"""

"""列表的查询操作"""
lst = ['hello', 'world', 98, 'hello', 'world', 234]
print(lst.index('hello'))  # 如果列表中有多个相同的元素,则只返回第一个元素的索引
print(lst.index('hello',1))
# 取列表最大下标
print(len(lst)-1)

"""列表的切片操作"""
lst = ['hello', 'world', 98, 'hello', 'world', 234]
print(lst[1:3])  # 切片操作,从索引1开始取,直到索引3结束,不包括索引3
print(lst[1:])  # 切片操作,从索引1开始取,直到列表末尾
print(lst[:3])  # 切片操作,从列表开头取,直到索引3结束,不包括索引3
print(lst[::2])  # 切片操作,从列表开头取,每隔2个取一个元素
print(lst[::-2])  # 切片操作,从列表末尾取,每隔2个取一个元素,反向排序

"""判断元素是否存在于列表"""
lst = ['hello', 'world', 98, 'hello', 'world', 234]
print('hello' in lst)  # 判断元素是否存在于列表中
print(98 not in lst)

"""列表元素的遍历"""
lst = ['hello', 'world', 98, 'hello', 'world', 234]
for i in lst:
    print(i)

"""列表元素的添加、删除、修改"""
lst = ['hello', 'world', 98, 'hello', 'world', 234]
lst2 = ['C/C++', 'C#']
lst.append('Python')  # 在列表末尾添加元素
print(lst)
lst.append(lst2)  # 在列表末尾添加另一个列表
print(lst)
lst.extend(lst2)  # 在列表末尾添加另一个列表
print(lst)
lst.insert(2, 'java')  # 在索引2位置插入元素
print(lst)
lst.remove('hello')  # 删除列表中第一个指定元素
print(lst)
lst.pop(2)  # 删除指定索引的元素,并返回该元素的值
print(lst)
lst[2] = 'c++'  # 修改指定索引的元素的值
print(lst)
lst.pop()  # 删除列表末尾的元素
print(lst)
lst[1:] = lst2  # 切片赋值,将列表lst的索引1到末尾的元素赋值为lst2
print(lst)
