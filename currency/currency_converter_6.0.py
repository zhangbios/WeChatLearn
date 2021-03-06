"""
    作者：KsBios
    日期：2017.12.28
    版本：5.0
    功能：汇率兑换
    3.0根据输入判断美元还是人民币
    4.0循环
    5.0函数封装
    6.0使程序更加结构化，简单函数定义 Lambda
"""


# def convert_currency(im, er):
#     """
#         汇率兑换
#     """
#     out = im * er
#     return out


def main():
    """
        主函数
    """
    # 汇率
    USD_VS_RMB = 6.77
    # 带单位的货币输入
    currency_str_value = input("请输入带单位的货币输入:")
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        convert_currency2 = lambda x: x * exchange_rate

        # # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)
        out_money = convert_currency2(in_money)
        print("转换后的金额：",out_money)
    else:
        print("输入的货币单位不正确！")


# __name__ 特殊变量名
if __name__ == "__main__":
    main()