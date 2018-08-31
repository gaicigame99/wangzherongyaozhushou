def show_main_view():
    print("-^-"*35)
    welcomes = """
                    欢迎使用中国计量大学学员管理系统
    
                        # 1，学员信息创建
                        # 2，学员信息修改
                        # 3，学员信息删除
                        # 4，学员信息查询
                        # 5，退出
    
    """
    print(welcomes)
    print("-v-"*35)

def show_create_view():
    print("-^-" * 35)
    welcomes = """
                    1,学员信息创建界面

                    # ，创建学员姓名
                    # ，创建学员学号
                    # ，创建学员年龄
                    # ，创建学员籍贯
                    # ，创建学员爱好
                    # , 性取向

    """
    print(welcomes)
    print("-v-" * 35)

def show_search_view():
    print("-^-" * 35)
    welcomes = """
                    1,学员信息查询界面
                    # ，通过姓名查询
                    # ，通过年龄查询
                    # ，通过学号查询
             


    """
    print(welcomes)
    print("-v-" * 35)

all_stu = {}
def create_information():
    while True:
        name = input("请输入学员姓名:")
        number = input("请输入学员学号")
        age = int(input("请输入学员年龄:"))
        addr = input("请输入学员籍贯:")
        hobby = input("请输入学员爱好:")
        lover = input("请输入学员性取向:")
        # lista = [name,number,age,addr,hobby,lover]
        all_stu[number] = [name,number, age, addr, hobby, lover]
        complete = input("是否完成输入(1是/2否)")
        if complete == "1" or complete == "是":
            break
        elif complete == "2" or complete == "否":
            continue
        else:
            all_stu.pop(name)
            print("输入错误，请重新输入")
            pass


def search_information():
    while True:
        search_input = input("请输入查询学员信息姓名/年龄/学号")

        # 如果用户输入的是学号，通过key就可以找到这个同学的信息
        if search_input in all_stu:
            print(f"姓名{all_stu[search_input][0]},详细信息：{all_stu[search_input]}")
            return search_input
        # 年龄
        elif search_input.isdigit():
            # 1,遍历整个字典，把年龄相同的，打印
            for key in all_stu:
                if int(search_input) in all_stu[key]:
                    print(f"姓名{search_input},{all_stu[key]}")
                    return all_stu[key][1]

        # 姓名 isalpha 说明输入的是汉字或字母
        elif search_input.isalpha():
            for key in all_stu:
                if search_input in all_stu[key]:
                    print(f"姓名{search_input},{all_stu[key]}")
                    return all_stu[key][1]
        else:
            print("查无此人")
        search_compelet = input("是否查询完成（1是/2否）")
        if search_compelet == "1" or search_compelet == "是":
            break
        elif search_compelet == "2" or search_compelet == "否":
            continue
        else:
            print("你输入错误，请重新输入")

def change_information():
    search_information()
    create_information()

def delete_information():
    number= search_information()
    delete= input("是否删除该学员信息")
    if delete== "是":
        all_stu.pop(number)
        print("删除成功")



while True:
    show_main_view()
    main_input = input("请输入您的选择(1~5):")
    if main_input=="1":
        show_create_view()
        create_information()
    if main_input=="2":
        print("您选择了修改")
        change_information()
    if main_input=="3":
        print("您选择了删除")
        delete_information()

    if main_input=="4":
        # print("您选择了查询")
        show_search_view()
        search_information()

    if main_input=="5":
        print("您选择了5")
