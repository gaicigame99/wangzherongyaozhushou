# 练习1
# 获得全班学员姓氏
# 练习2
# 班级大数据，计算姓氏数量，把姓氏从多到少排序
# 练习3
# 同学信息与爱好管理
# 练习1
# names = "蒋欢宇,周家玮,马思聪,程豪杰,邱华彬,陈雨浩,黄璜,王振翔,吕方明,叶挺立,周星宇,赖嘉威,陈嘉威,韩学历,付泽凡,张润森,张锦晖,姜华卿,楼子昊,白洪伟,兰国樑,南高拓,过严耀,余振宇,邹昌伟,黄钢星,吕航,董理,劳家玺,朱伟浩,曹海浩,黄冠铧"
# list_name = names.split(",")
# # ["蒋欢宇","周家玮",...]
# # print(len(list_name))
# for name in list_name:
#     print(name[0])

# 练习2
# names = "蒋欢宇,周家玮,马思聪,程豪杰,邱华彬,陈雨浩,黄璜,王振翔,吕方明,叶挺立,周星宇,赖嘉威,陈嘉威,韩学历,付泽凡,张润森,张锦晖,姜华卿,楼子昊,白洪伟,兰国樑,南高拓,过严耀,余振宇,邹昌伟,黄钢星,吕航,董理,劳家玺,朱伟浩,曹海浩,黄冠铧"
# list_name = names.split(",")
# # 保存全班姓氏列表
# list_stu = []
# for name in list_name:
#     # print(name[0])
#     list_stu.append(name[0])
#
# # key   value
# # 姓     数量
# dict_xing = {}
# for xing in list_stu:
#     if xing in dict_xing:
#         dict_xing[xing] += 1
#     else:
#         dict_xing[xing] = 1
#
# # for xing in dict_xing:
# #     print(xing,dict_xing[xing])
# # 获得姓氏组
# # 获得姓氏组对应的数量组
# # list_xing是不重复的姓氏组
# list_xing = list(dict_xing.keys())
# # 通过姓氏组获取数量组
# list_num = []
# for xing in list_xing:
#     # print(xing,dict_xing[xing])
#     list_num.append(dict_xing[xing])
#
# # 排序
# # 要排序数量组，数量组改变位置后，姓名组也跟着改变
# for i in range(len(list_num)):
#     for j in range(len(list_num)):
#         if list_num[i]>list_num[j]:
#             temp = list_num[i]
#             list_num[i] = list_num[j]
#             list_num[j] = temp
#             temp1 = list_xing[i]
#             list_xing[i] = list_xing[j]
#             list_xing[j] = temp1
#
#
# for i in range(len(list_num)):
#     print(list_xing[i], list_num[i])

# 练习3
# 同学信息与爱好管理
# names = "蒋欢宇,周家玮,马思聪,程豪杰,邱华彬,陈雨浩,黄璜,王振翔,吕方明,叶挺立,周星宇,赖嘉威,陈嘉威,韩学历,付泽凡,张润森,张锦晖,姜华卿,楼子昊,白洪伟,兰国樑,南高拓,过严耀,余振宇,邹昌伟,黄钢星,吕航,董理,劳家玺,朱伟浩,曹海浩,黄冠铧"
# list_name = names.split(",")
# mini = ["叶挺立","张润森","马思聪","蒋欢宇"]
#
# all_stu = {}
# all_message = [
#     ["叶挺立",20,"部落冲突，皇室战争"],
#     ["张润森",20,"部落冲突，皇室战争"],
#     ["马思聪",20,"部落冲突，皇室战争"],
#     ["蒋欢宇",19,"部落冲突，皇室战争"],
# ]
# for i in range(len(mini)):
#     # name = mini[i]
#     # all_stu[name] = all_message[i]
#     all_stu[mini[i]] = all_message[i]
#
#
# for key in all_stu:
#     print(f"姓名:{key},个人信息:{all_stu[key]}")


# 集合
# <1> 无值声明方式
s = set()
# <2> 有值声明方式
s1 = {'a','b',10}

#
# example:
s = set()
s = {"abc"}
s = {"AACCBB"}
s = {True, None, 10, "a"}

# 1,可以改变
# 2，数据唯一，（不能重复），可以用来去重
# la = [1,2,2,2,2,3,4,4,1,2,3,4,2,2,2]
# print(set(la))
# print(la)
# la = set(la)
# print(la)
# la = list(la)
# print(la)
# la = list(set(la))
# print(la)
# 3 ,集合没有顺序，没有先后
# 4，可以把集合认为是一个没有值的字典
# 5，集合是可以迭代，，，，可以使用循环访问
# 6， 集合的内容，必须是不可变对象，

# 交集：两个集合当中公共部分
# 全集：两个集合中的全部元素
# 补集：存在于A中但不存在于B中
#       对于A来说，C是B的补集
A = {1,2,3}
B = {2,3}
C = {1}

#
s1 = {1,2,3}
s2 = {2,3,4}
# 补集
s = s1 - s2  #  s= {1}
# print(s)
# 全集
s = s1 | s2
# print(s)
# 交集
s = s1 & s2
# print(s)

# 对称补集
s = s1^s2
# print(s)

# >
# 判断一个家伙是否是另一个的子集
print(s1 > s)

# <
# 判断某个家伙是否是另一个的父集

# ==
# 判断两个集合是否相同
print(s1==s2)

# !=
# 两个集合是否不同

# in, not in
# 判断某个家伙是否存在，，或者不存在

# len()
# 获取集合长度

# 练习：
# 经理：曹操，刘备，周瑜
# 技术员：曹操，刘备，典韦，关羽，张飞

#,1,用集合求既是经理又是技术员的有谁？
#，2，是经理但不是技术员的是谁？
# 3，是技术员但不是经理的是谁？
# 4，张飞是经理吗？
# 5，只有一种身份的是谁
# 6，经理和技术员一共多少人？
m = {"曹操","刘备","周瑜"}
t = {"曹操","刘备","典韦","关羽","张飞"}
print(m & t)
print(m - t)
print(t - m)
print({"张飞"} < m)
print(m ^ t)
print(m | t)



# 学员管理系统
#
# 1，学员信息创建
# 2，学员信息修改
# 3，学员信息删除
# 4，学员信息查询
# 5，退出

# 一个单独的，能够完成指定功能的代码块，
# 分离出来，独立使用，
# 函数
#声明
def fun(a,list_b,dict_key_for_b):
    b = list_b
    c = dict_key_for_b
    for i in range(a):
        print(b[i],c[b[i]])
    return a,b,c

def f(a):
    return a

s1 = 3
s2 = [1,2,3]
s3 = {1:"aaa",2:"bbb",3:"ccc"}
# 调用
s1,s2,s3 = fun(s1,s2,s3)


# 练习3 (函数版)
# 同学信息与爱好管理
mini = ["叶挺立","张润森","马思聪","蒋欢宇"]
all_message = [
    ["叶挺立",20,"部落冲突，皇室战争"],
    ["张润森",20,"部落冲突，皇室战争"],
    ["马思聪",20,"部落冲突，皇室战争"],
    ["蒋欢宇",19,"部落冲突，皇室战争"],
]
def message_dict(l_name_msg,ll_person_msg):
    all_stu = {}
    mini = l_name_msg
    all_message = ll_person_msg
    for i in range(len(mini)):
        all_stu[mini[i]] = all_message[i]
    for key in all_stu:
        print(f"姓名:{key},个人信息:{all_stu[key]}")
    return all_stu


# print("\n"*3)
# print("欢迎使用中国计量大学学员管理系统")
welcomes = """
                欢迎使用中国计量大学学员管理系统
    
                    # 1，学员信息创建
                    # 2，学员信息修改
                    # 3，学员信息删除
                    # 4，学员信息查询
                    # 5，退出
                    
请输入对应数字进行操作：
"""

my_dict = message_dict(mini,all_message)
# print(my_dict)
# for key in my_dict:
#     print(f"姓名:{key},个人信息:{my_dict[key]}")

print("-^-"*35)
print(welcomes)

# print(my_dict)
# for key in my_dict:
#     print(f"姓名:{key},个人信息:{my_dict[key]}")
print("\n")
print("-v-"*35)
