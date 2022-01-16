# 全具的变量
PI = 3.1415926


def input_num():
    """[summary]
    """
    # 使用循环来实现，如果输入的无效，就提示重新输入
    while True:
        # 提醒输入
        radii_str = input("请输入圆的半径: ")
        # 使用异常处理
        try:
            radii = float(radii_str)
            # 返回
            return radii
        except:
            print("输入的半径无效")


def get_area(radii: float):
    return PI * radii * radii


def get_primeter(radii: float):
    """[summary]

    Args:
        radii (float): [description]
    """
    return 2 * PI * radii


# main函数： 程序的入口
if __name__ == '__main__':
    # 调用函数，提醒输入半径，返回一个符合要求的值
    radii = input_num()
    # 输出
    print("圆的周长为: %.1f" % get_primeter(float(radii)))
    print("圆的面积为: %.1f" % get_area(float(radii)))
