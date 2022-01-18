from calendar import month

# 核心判断是润年还是平年
# 情况1：年份%400 == 0润年
# 情况2：年份%4 ==0 And 年份%100 ！ = 0
if __name__ == '__main__':
    year = int(input("请输入年份: "))
    # 输入的年份转为整数
    month = int(input("请输入月份: "))
    # 输入的年份转为整数

    # 定义一个天数
    days = 0
    # 判断
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        # 处理2月份
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28
    # 输出
    print("%d年%d月: %d天" % (year, month, days))
