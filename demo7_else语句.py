# 开发机构 : 涠洲消防救援
# 开发人员 : CG_cheng
# 开发时间 : 2025/11/30 上午9:46
"""
for item in range(3):
    pwd = input("请输入密码：")
    if pwd == "8888":
        print("密码正确，进入系统")
        break
    else:
        print("密码错误，请重新输入")
else:
    print("三次密码错误，退出系统")
"""

a = 0
while a < 3:
    b = input("请输入密码：")
    if b == "8888":
        print("密码正确，进入系统")
        break
    else:
        print("密码错误，请重新输入")
        a += 1
else:
    print("三次密码错误，退出系统")
