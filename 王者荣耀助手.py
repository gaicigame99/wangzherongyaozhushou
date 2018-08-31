import pygame

pygame.init()

tanke = ["孙策","梦奇","苏烈","东皇太一","太乙真人","张飞","牛魔","刘邦","程咬金","关羽","项羽","达摩","夏侯惇","吕布","芈月","白起","钟无艳","刘禅","庄周","墨子","廉颇",]
zhanshi = ["孙策","狂铁","裴擒虎","苏烈","铠","哪吒","雅典娜","杨戬","钟馗","刘备","孙悟空","亚瑟","橘右京","花木兰","韩信","露娜","关羽","老夫子","达摩","李白","宫本武藏","典韦","曹操","夏侯惇","吕布","钟无艳","赵云",]
cike = ["元歌","裴擒虎","百里玄策","百里守约","孙悟空","橘右京","娜可露露","不知火舞","花木兰","兰陵王","韩信","貂蝉","李白","阿轲","赵云",]
fashi = ["司马懿","米莱狄","弈星","杨玉环","女娲","梦奇","干将莫邪","诸葛亮","钟馗","不知火舞","张良","王昭君","姜子牙","露娜","安琪拉","貂蝉","武则天","甄姬","周瑜","芈月","扁鹊","孙膑","高渐离","嬴政","妲己","墨子","小乔",]
sheshou = ["公孙离","百里守约","黄忠","成吉思汗","虞姬","李元芳","后羿","狄仁杰","马可波罗","鲁班七号","孙尚香",]
fuzhu = ["杨玉环","明世隐","鬼谷子","大乔","太乙真人","蔡文姬","张飞","牛魔","刘邦","扁鹊","孙膑","庄周",]
heros = list(set(tanke+zhanshi+cike+fashi+sheshou+fuzhu))
heros.sort()

all_heroes = [heros,tanke,zhanshi,cike,fashi,sheshou,fuzhu]

WHITE = (255,255,255)  # R G B
QWHITE = (200,200,200)
RED = (255,0,0)
GREEN = (0,255,0)
# 全部/坦克/战士/刺客/法师/射手/辅助
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",26)
font16 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",16)

all_text = font.render("全 部",True,QWHITE)
tanke_text = font.render("坦 克",True,QWHITE)
zhanshi_text = font.render("战 士",True,QWHITE)
cike_text = font.render("刺 客",True,QWHITE)
fashi_text = font.render("法 师",True,QWHITE)
sheshou_text = font.render("射 手",True,QWHITE)
fuzhu_text = font.render("辅 助",True,QWHITE)

back_text = font.render("<-返回首页", True, QWHITE)

background = pygame.image.load("image/background.jpg")
# pygame.Surface.set_alpha(255)

# bzhw = pygame.image.load("image/不知火舞bk.jpg")
# 不知火舞
weizhi = -1
img = pygame.image.load("image/不知火舞bk.jpg")
renfeng = pygame.image.load("image/不知火舞_忍蜂.png")
renfeng_text = pygame.image.load("image/不知火舞_忍蜂text.png")
bsrenfeng = pygame.image.load("image/不知火舞_必杀忍蜂.png")
bsrenfeng_text = pygame.image.load("image/不知火舞_必杀忍蜂text.png")
huadieshan = pygame.image.load("image/不知火舞_花蝶扇.png")
huadieshan_text = pygame.image.load("image/不知火舞_花蝶扇text.png")
feixianglongyanzhen = pygame.image.load("image/不知火舞_飞翔龙炎阵.png")
feixianglongyanzhen_text = pygame.image.load("image/不知火舞_飞翔龙炎阵text.png")


# 获得所有英雄的图片
# allhero_images = []
# for i in range(len(all_heroes)):
#     hero_img = []
#     for [j] in range(len(heros)):
#         temp_hero = pygame.image.load(f"image/{all_heroes[i][j]}.jpg")
#         hero_img.append(temp_hero)
#     all_hero_images.append(hero_img)
hero_images = []
for i in range(len(heros)):
    temp_hero = pygame.image.load(f"image/{heros[i]}.jpg")
    hero_images.append(temp_hero)

tank_images = []
for i in range(len(tanke)):
    temp_hero = pygame.image.load(f"image/{tanke[i]}.jpg")
    tank_images.append(temp_hero)

zhanshi_images = []
for i in range(len(zhanshi)):
    temp_hero = pygame.image.load(f"image/{zhanshi[i]}.jpg")
    zhanshi_images.append(temp_hero)

cike_images = []
for i in range(len(cike)):
    temp_hero = pygame.image.load(f"image/{cike[i]}.jpg")
    cike_images.append(temp_hero)

fashi_images = []
for i in range(len(fashi)):
    temp_hero = pygame.image.load(f"image/{fashi[i]}.jpg")
    fashi_images.append(temp_hero)

sheshou_images = []
for i in range(len(sheshou)):
    temp_hero = pygame.image.load(f"image/{sheshou[i]}.jpg")
    sheshou_images.append(temp_hero)

fuzhu_images = []
for i in range(len(fuzhu)):
    temp_hero = pygame.image.load(f"image/{fuzhu[i]}.jpg")
    fuzhu_images.append(temp_hero)

hero_x = []
hero_y = []
for i in range(20):
    for j in range(10):
        x = 50 + 100 * j + 20 * j
        y = 60 + 100* i + 50 * i
        hero_x.append(x)
        hero_y.append(y)

mbx = 0
mby = 720
move = 0
screen = pygame.display.set_mode((1280,720))
all_flag = 0
tanke_flag = 0
zhanshi_flag = 0
cike_flag = 0
fashi_flag = 0
sheshou_flag = 0
fuzhu_flag = 0
back_flag = 1
position = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0,0))
    screen.blit(all_text, (70,20))
    screen.blit(tanke_text, (170, 20))
    screen.blit(zhanshi_text, (270, 20))
    screen.blit(cike_text, (370, 20))
    screen.blit(fashi_text, (470, 20))
    screen.blit(sheshou_text, (570, 20))
    screen.blit(fuzhu_text, (670, 20))

    mx,my = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    # height 26
    # 两个字的宽度26 + 13 +26
    # x,70, y = 50,
    # 根据鼠标位置改变状态
    if 70 < mx < 70+26 + 13 +26 and \
        20 < my < 20+26:
        all_text = font.render("全 部", True, RED)
        if m1:
            position = 0
            all_flag = 1
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 0
    else:
        all_text = font.render("全 部", True, QWHITE)
    if 170 < mx < 170+26 + 13 +26 and \
        20 < my < 20+26:
        tanke_text = font.render("坦 克", True, RED)
        if m1:
            position = 1
            all_flag = 0
            tanke_flag = 1
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 0
    else:
        tanke_text = font.render("坦 克", True, QWHITE)
    if 270 < mx < 270+26 + 13 +26 and \
        20 < my < 20+26:
        # print("您进入全部区域")
        zhanshi_text = font.render("战 士", True, RED)
        if m1:
            position = 2
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 1
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 0
    else:
        zhanshi_text = font.render("战 士", True, QWHITE)
    if 370 < mx < 370+26 + 13 +26 and \
        20 < my < 20+26:
        cike_text = font.render("刺 客", True, RED)
        if m1:
            position = 3
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 1
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 0
    else:
        cike_text = font.render("刺 客", True, QWHITE)
    if 470 < mx < 470+26 + 13 +26 and \
        20 < my < 20+26:
        # 道士到寺盗十柿
        # 武士无事舞石狮
        fashi_text = font.render("法 师", True, RED)
        if m1:
            position = 4
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 1
            sheshou_flag = 0
            fuzhu_flag = 0
    else:
        fashi_text = font.render("法 师", True, QWHITE)
    if 570 < mx < 570+26 + 13 +26 and \
        20 < my < 20+26:
        sheshou_text = font.render("射 手", True, RED)
        if m1:
            position = 5
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 1
            fuzhu_flag = 0
    else:
        sheshou_text = font.render("射 手", True, QWHITE)
    if 670 < mx < 670+26 + 13 +26 and \
        20 < my < 20+26:
        fuzhu_text = font.render("辅 助", True, RED)
        if m1:
            position = 6
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 1
    else:
        fuzhu_text = font.render("辅 助", True, QWHITE)

    # 根据状态显示不同内容
    if all_flag:
        for i in range(len(heros)):
            image = hero_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image,(100,100))
            screen.blit(image, (x,y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x+50 - len(heros[i])*16/2
            y1 = y + 100 + 5
            text = font16.render(heros[i], True, GREEN)
            screen.blit(text, (x1,y1))
    if tanke_flag:
        for i in range(len(tanke)):
            image = tank_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(tanke[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(tanke[i], True, GREEN)
            screen.blit(text, (x1, y1))
    if zhanshi_flag:
        for i in range(len(zhanshi)):
            image = zhanshi_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(zhanshi[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(zhanshi[i], True, GREEN)
            screen.blit(text, (x1, y1))
    if cike_flag:
        for i in range(len(cike)):
            image = cike_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(cike[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(cike[i], True, GREEN)
            screen.blit(text, (x1, y1))
    if fashi_flag:
        for i in range(len(fashi)):
            image = fashi_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(fashi[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(fashi[i], True, GREEN)
            screen.blit(text, (x1, y1))
    if sheshou_flag:
        for i in range(len(sheshou)):
            image = sheshou_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(sheshou[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(sheshou[i], True, GREEN)
            screen.blit(text, (x1, y1))
    if fuzhu_flag:
        for i in range(len(fuzhu)):
            image = fuzhu_images[i]
            x = hero_x[i]
            y = hero_y[i]
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (x, y))
            # 名字有不同长度,根据不同名字长度，计算位置
            x1 = x + 50 - len(fuzhu[i]) * 16 / 2
            y1 = y + 100 + 5
            text = font16.render(fuzhu[i], True, GREEN)
            screen.blit(text, (x1, y1))
    for i in range(len(heros)):
        if m1 == 1 and move==0 and mx > hero_x[i] and mx < hero_x[i] + 100 and \
                my > hero_y[i] and my < hero_y[i] + 100:
            move = 1
            back_flag = 1
            weizhi = i
            all_flag = 0
            tanke_flag = 0
            zhanshi_flag = 0
            cike_flag = 0
            fashi_flag = 0
            sheshou_flag = 0
            fuzhu_flag = 0

    if move and back_flag:
        # 获取到当前页面英雄组
        temp_heros = all_heroes[position]
        img = pygame.image.load(f"image/{temp_heros[weizhi]}bk.jpg")
        screen.blit(img, (mbx, mby))
        mby -= 20
        if mby < 0:
            mby = 0
        if mby == 0:
            screen.blit(back_text, (0, 0))
            screen.blit(renfeng, (1080, 70))   #  1080, +93 ，70 ，+93
            screen.blit(feixianglongyanzhen, (1080, 200))   #  1080, +93, 233,+93
            screen.blit(huadieshan, (1080, 330))    #  163
            screen.blit(bsrenfeng, (1080, 460))
        if m1 and 1080 < mx < 1080+93 and \
                70 < my < 70+93:
            screen.blit(renfeng_text, (1080-780, 70))
        if m1 and 1080 < mx < 1080+93 and \
                200 < my < 200+93:
            screen.blit(renfeng_text, (1080-780, 200))
        if m1 and 1080 < mx < 1080+93 and \
                330 < my < 330+93:
            screen.blit(renfeng_text, (1080-780, 330))
        if m1 and 1080 < mx < 1080+93 and \
                460 < my < 460+93:
            screen.blit(renfeng_text, (1080-780, 460))

        if m1 and 0 < mx < 0 + 26*5 and \
                0 < my < 30:
            back_text = font.render("<-返回首页", True, RED)
            move = 0
        else:
            back_text = font.render("<-返回首页", True, QWHITE)
    if move == 0:

        screen.blit(img, (mbx, mby))
        mby += 20
        if mby > 720:
            mby = 720
    pygame.display.update()
