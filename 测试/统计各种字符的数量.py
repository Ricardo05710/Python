if __name__ == '__main__':
    str = input("请输入您要查询的语句: ")
    # 定义变量
    # upper_char_num = 0
    # low_char_num = 0
    # numbers_char_num = 0
    # chinese_char_num = 0
    # other_char_num = 0
    # 字典 dict ---key_value
    num = {'upper': 0, 'lower': 0, 'number': 0,
           'chinese': 0, 'other': 0}  # json
    # 遍历每一个字符
    for char in str:
        # 判断大写字母
        if char.isupper():
            num['upper'] += 1
            # 判断大写字母
        elif char.islower():
            num['lower'] += 1
            # 判断是不是小写字母
        elif char.isdigit():
            num['number'] += 1
            # 判断是不是数字
        elif char >= '\u4E00' and char <= '\u9FA5':
            num['chinese'] += 1
        # 判断是不是汉字
        else:
            num['other'] += 1
        # 其他
    print("大写字母: %d\n小写字母: %d\n数字字符: %d\n汉字: %d\n其他: %d" % (num['upper'],
                                                            num['lower'], num['number'], num['chinese'], num['other']))
    # 输出
