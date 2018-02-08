"""
    作者：KsBios
    日期：2017.12.28
    版本：2.0
    功能：汇率兑换
"""

import keyword
print(keyword.kwlist)
# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
rmb_str_value = input("please input CNY:")

# 字符串转换为数字
rmb_value = eval(rmb_str_value)


# 汇率计算
usd_value = rmb_value / USD_VS_RMB

# 输出金额
print("USD is :", usd_value)