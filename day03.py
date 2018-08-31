# # 英雄选择器
# # 1，有王者荣耀里面的英雄，随机选出5个，打印
# # 2，根据英雄的职业不同，给出阵容是否合理，合理，不合理
# # 至少有1个法师职业
# # 至少有1个打野
# # 至少有1个战士/坦克
# # 其他两个任意，都是合理的。
# import random
#
#
# tanke = ["孙策","梦奇","苏烈","东皇太一","太乙真人","张飞","牛魔","刘邦","程咬金","关羽","项羽","达摩","夏侯惇","吕布","芈月","白起","钟无艳","刘禅","庄周","墨子","廉颇",]
# zhanshi = ["孙策","狂铁","裴擒虎","苏烈","哪吒","雅典娜","杨戬","钟馗","刘备","孙悟空","亚瑟","橘右京","花木兰","韩信","露娜","关羽","老夫子","达摩","李白","宫本武藏","典韦","曹操","夏侯惇","吕布","钟无艳","赵云",]
# cike = ["元歌","裴擒虎","百里玄策","百里守约","孙悟空","橘右京","娜可露露","不知火舞","花木兰","兰陵王","韩信","貂蝉","李白","阿轲","赵云",]
# fashi = ["米莱狄","弈星","杨玉环","女娲","梦奇","干将莫邪","诸葛亮","钟馗","不知火舞","张良","王昭君","姜子牙","露娜","安琪拉","貂蝉","武则天","甄姬","周瑜","芈月","扁鹊","孙膑","高渐离","嬴政","妲己","墨子","小乔",]
# sheshou = ["公孙离","百里守约","黄忠","成吉思汗","虞姬","李元芳","后羿","狄仁杰","马可波罗","鲁班七号","孙尚香",]
# fuzhu = ["杨玉环","明世隐","鬼谷子","大乔","太乙真人","蔡文姬","张飞","牛魔","刘邦","扁鹊","孙膑","庄周",]
#
# heroes = []
# # 添加
# heroes.extend(tanke)
# heroes.extend(zhanshi)
# heroes.extend(cike)
# heroes.extend(fashi)
# heroes.extend(sheshou)
# heroes.extend(fuzhu)
# # print(heroes)
# # heroes.append("张苞")
# # 每一次，从英雄组内取一个英雄
# # for hero in heroes:
# #     print(hero)
# # #
# # # len() 函数可以获取列表的长度， 字符串  len("abc")
# # for i in range(len(heroes)):
# #     print(i,heroes[i])
#
# all_hero = []
# # 练习
# # 去除重复英雄
# for hero in heroes:
#     if hero not in all_hero:
#         all_hero.append(hero)
#
# # for hero in all_hero:
# #     print(hero)
# # 选取英雄
# # len(all_hero)   # 获取总共有多少个英雄
# # for i in range(5):
# #     index = random.randint(0, len(all_hero) - 1)  # 0~ 长度-1
# #     print(all_hero[index])
# # 有重复英雄，因为会随机出现相同位置
#
# # 获取到5个不同的位置
# weizhi = []
# while True:
#     index = random.randint(0, len(all_hero) - 1)
#     # print(index)
#     if index not in weizhi:
#         weizhi.append(index)
#     if len(weizhi) == 5:     # 当够5个位置，退出
#         break
# # 打印5个英雄
# teams = [] # 放一组英雄
# for i in weizhi:
#     # print(i,all_hero[i])
#     teams.append(all_hero[i]) # 把选出位置的英雄，放到一组中
#
# fs = 0
# dy = 0
# zs = 0
# for hero_t in teams:
#     print(hero_t)
#     if hero_t in fashi:
#         fs += 1
#     if hero_t in zhanshi or hero_t in tanke:
#         zs += 1
#     if hero_t in cike:
#         dy += 1
#
# if fs==0:
#     print("缺少法师")
# if zs==0:
#     print("缺少战士或肉盾")
# if dy==0:
#     print("缺少打野英雄")
#
# if fs and zs and dy:
#     print("阵容合理")

# # 列表
# # 合并
# la = [10,2,3]
# lb = [4,5,6]
# lab = la + lb  #
# print(lab)
# #
# laabb = la*3
# print(laabb)
#
# # print(la > lb)
# # >=
# # <
# # <=
#
# # in
# # 列表支持in操作，可以检查某个对象是否是当前内容
#
# # 列表切片
# all = [1,2,3,4,5,6,7,8,9]
# print(all[::2])
# print(all[1::2])
#
# # 查询列表数量，，
# # len()
# #
# names = "张锦晖,吕方明,叶挺立,周星宇"
# print(names)
# lname = names.split(',')
# print(lname)

#
# 练习1
# 获得全班学员姓氏
# 练习2
# 班级大数据，计算姓氏数量，把姓氏从多到少排序


# 元组
# -----不能修改
# 声明
# # 方式1：
# t = ()
# # 方式2
# t1 = tuple()

# 获得元素的索引
# t.index()

# 统计元素的数量
# t.count()
#
# t[0] = 10
# print(t)

#
# color_a = (255,255,255)  # 白色
# background = (800,600)  # 场景大小
#
# ta = (1,2,3)
# tb = (4,5,6)
# tab = ta+tb
# print(tab)

# + ， += ，复制操作 *， *=
# >, < ,>=, <=,
# in
# len()

# 字典
# 声明
# []列表 ,()元祖,{}字典
# <1>方式一
d = {}
# <2>方式二
d1 = dict()

student = ["周家玮",19,175,65,"杭州市萧山区"]
d_stu = {'name':"周家玮",'age':19,'height':175,'weight':65,'addr':"杭州"}
# 代码可读性高，
# 优于查询数据
print(d1)
# 插入数据
d1['name'] = "陈雨浩"
#   key       value
#   键         值
# print(d1)
# # print(list(d1.keys()))
# print(d1['name'])
# d1.keys()
names = "蒋欢宇,周家玮,马思聪,程豪杰,邱华彬,陈雨浩,黄璜,王振翔,吕方明,叶挺立,周星宇,赖嘉威,陈嘉威,韩学历,付泽凡,张润森,张锦晖,姜华卿,楼子昊,白洪伟,兰国樑,南高拓,过严耀,余振宇,邹昌伟,黄钢星,吕航,董理,劳家玺,朱伟浩,曹海浩,黄冠铧"
ln = names.split(',')
# print(ln)
# d1['names'] = ln
# print(d1)

# key 的可取值范围
# True,False,
# 1,2,3,4,5,7,89, 1111,22,
# 'a', 'b','c','asdf'
# "姓名" ，"性别"
d1['0'] = 10
d1[0] = 10
print(d1)
d1[False] = 5
d1[1] = 100
d1[True] = 50
print(d1)
# 使用key时
#  1,True 会当作1， False 会当作0
#  2，尽量不要使用数字当作key，
#     容易与列表混淆，导致代码修改难度上升
#  3，所有常量都可以当作key，但是不存在重复的key，
# 如果添加一个已有的key，并且添加内容，那么旧内容被覆盖

#  value取值范围
#
# d{key:value}
# value 原则上，可以使用任意数据
# 可以使用常量
# 可以使用变量
# 可以使用列表
# 可以使用元组
# 可以使用字典
# 可以使用集合
# 也可以方自定义对象

# 获得一个字典副本
d2 = d.copy()

# 弹出指定的value
# print(d.pop('name'))
# d.clear()
# d.fromkeys()
# d.get()
# print(list(d1.items()))
# print(list(d1.keys()))
# for key in d1.keys():
#     print(d1[key])

# d.popitem()
# d.setdefault()
# d.update()
# d.values()
for value in d1.values():
    print(value)

# "姓名","性别","身高","体重","学号"
ds = {}
keys = ["姓名","性别","身高","体重","学号"]
# for key in keys:
#     ds[key] =
for i in range(len(keys)):
    ds[keys[i]] = ""

ds["姓名"] = ln
#
# 练习3
# 同学信息与爱好管理
#
value = ["周家玮","光电1班","2016010122","13800138000"]
ds['周家玮'] = value