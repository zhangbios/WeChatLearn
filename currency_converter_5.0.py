"""
    作者：KsBios
    日期：2017.12.28
    版本：5.0
    功能：汇率兑换
    3.0根据输入判断美元还是人民币
    4.0循环
    5.0函数封装
"""


def convert_currency(im, er):
    """
        汇率兑换
    """
    out = im * er
    return out


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
    out_money = convert_currency(in_money, exchange_rate)
    print("转换后的金额：",out_money)
else:
    print("输入的货币单位不正确！")