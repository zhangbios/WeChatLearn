"""
    作者：KsBios
    日期：2017.12.28
    版本：1.0
    功能：汇率兑换
"""

rmb_str_value = input("please input CNY:")

rmb_value = eval(rmb_str_value)

USD_VS_RMB = 6.77

usd_value = rmb_value / USD_VS_RMB

print("USD is :", usd_value)