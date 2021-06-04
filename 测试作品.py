print('--------欢迎使用方差计算器---------')

try:
    print('用阿拉伯数字！')
    times = int(input('请输入计算的数字个数（用阿拉伯数字！）'))
except BaseException:
    print('用阿拉伯数字！自己重启程序去吧！')

mylist = []
myall = 0
for i in range(0, times):
    num = int(input('请输入数值'))
    mylist.append(num)
for n in mylist:
    myall += n
average = myall/times

print(mylist, average, myall)

num1 = 0
for j in mylist:
    num1 += (j-average)**2
    print(num1)
fangcha = num1/times


print('方差：', fangcha, '平均数：', average)




















