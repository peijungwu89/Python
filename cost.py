請使用者輸入支出金額，輸入０結束
並印出以下畫面

支出：
支出：
支出：
支出：
支出：
支出：
------（結束後）
最大值：
最小值：
總支出：

#------------------------------------

def getResult(items):
    max = items[0]
    min = items[0]
    sum = 0
    for i in items:
        if i > max:
            max = i
        if i <min:
            min = i
        sum += i
    return max, min, sum


# ---------------------------


items = []
while True:
    pay = int(input('支出：'))
    if pay==0:
        break
    items.append(pay)
print('----------------------')
max, min, sum = getResult(items)
print('最大：', max)
print('最小：', min)
print('總計：', sum)
print('平均：', sum / len(items))
