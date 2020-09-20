import time

print("欢迎使用智能计算器系统（仅支持整数）")
time.sleep(0.5)
print("作者:BW-宇辰")

choose=input("""请输入你需要的运算，（加法；减法；乘法；除法；幂）
——""")
if "加" in choose:
    print("仅支持两位数")
    addend1=input("请输入第一个加数:")
    addend1=int(addend1)
    addend2=input("请输入第二个加数:")
    addend2=int(addend2)
    print(addend1,addend2,sep="+",end="=")
    print(addend1+addend2)
elif "减" in choose:
    print("仅支持两位数")
    minuend= input("请输入被减数:")
    minuend=int(minuend)
    subtrahend= input("请输入减数：")
    subtrahend=int(subtrahend)
    print(minuend,subtrahend,sep="-",end="=")
    print(minuend-subtrahend)
elif "乘"in choose:
    print("仅支持两位数")
    factor1=input("请输入第一个因数:")
    factor1=int(factor1)
    factor2=input("请输入第二个因数:")
    factor2=int(factor2)
    print(factor1,factor2,sep="X",end="=")
    print(factor1*factor2)
elif "除"in choose:
    print("仅支持两位数")
    dividend= input("请输入被除数:")
    dividend=int(dividend)
    divisor= input("请输入除数:")
    divisor=int(divisor)
    result=dividend//divisor
    remainder=dividend%divisor
    print(dividend,divisor,sep="÷",end="=")
    if remainder == 0:
        print(result,"无余数")
    else:
        print(result,"余",remainder)
elif "幂" in choose:
    baseNumber=input("请输入底数:")
    baseNumber=int(baseNumber)
    indexNumber=input("请输入指数:")
    indexNumber=int(indexNumber)
    print(baseNumber,indexNumber,sep="^",end="=")
    print(baseNumber**indexNumber)
input()
