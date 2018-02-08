"""
    作者：KsBios
    日期：2017.12.28
    版本：3.0
    功能：汇率兑换
    3.0根据输入判断美元还是人民币
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币输入:")

# 字符串的操作
# print(currency_str_value[3])
# print(currency_str_value[-3:])
# print(currency_str_value[:-3])

unit = currency_str_value[-3:]
money_str_value = currency_str_value[:-3]

if unit == 'CNY':
    # print(currency_str_value[:-3])
    money_converted = int(money_str_value) / USD_VS_RMB
    print(money_converted)

elif unit == 'USD':
    money_converted = int(money_str_value) * USD_VS_RMB
    print(money_converted)

else:
    print("输入的单位错误！")

# # 字符串转换为数字
# rmb_value = eval(rmb_str_value)
#
# # 汇率计算
# usd_value = rmb_value / USD_VS_RMB
#
# # 输出金额
# print("USD is :", usd_value)