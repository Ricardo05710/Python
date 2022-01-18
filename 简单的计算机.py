# data_one   data_two    symbol

flag = 1

if __name__ == '__main__':
    data_one = int(input("请输入第一个数: "))   #
    symbol = input("选择操作运算符(+, -, *, /, %)")
    data_two = int(input("请输入第二个数"))
    # 进行加运算
    if symbol == "+":
        results = data_one + data_two
    # 进行减运算
    elif symbol == "-":
        results = data_one - data_two
    # 进行乘运算
    elif symbol == "*":
        results = data_one * data_two
    # 进行除运算
    elif symbol == "/":
        results = data_one / data_two
    # 运算
    elif symbol == "%":
        results = data_one % data_two
    else:
        flag = 0
    #判断
    if flag == 0:
        print("输入的运算符有错误，请重新输入!")
    else:
        print(results)
