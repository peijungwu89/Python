def menu():
    print("帳號、密碼管理系統")
    print("-------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號、密碼")
    print("0. 結  束  程  式")
    print("-------------------------")

def read_data():
    file = open('password.txt', 'r', encoding='utf8')
    originData = file.read()
    if originData != '':
        data = eval(originData)
        return data
    else:
        return dict()

def disp_data():
    print('------------------------')
    for key in data:
        print(f'帳號: {key}\t 密碼: {data[key]}')
    print('------------------------')
    input('按<Enter>回主選單')

def input_data():
    while True:
        name = input('請輸入帳號，輸入<Enter>結束:')
        if name == '':
            break
        if name in data:
            print(f'您輸入的帳號 {name} 已存在!')
            continue
        password = input('請輸入密碼:')
        data[name] = password
        with open('password.txt', 'w', encoding='utf8') as file:
            file.write(str(data))
            print(f'{name} 已經成功存入!')

def edit_data():
    while True:
        name = input('請輸入欲修改的帳號，輸入<Enter>結束:')
        if name == '':
            break
        if name not in data:
            print(f'您輸入的帳號 {name} 不存在!')
            continue
        print(f'原來的密碼為{data[name]}')
        password = input('請輸入新密碼:')
        data[name] = password
        with open('password.txt', 'w', encoding='utf8') as file:
            file.write(str(data))
            input('密碼更改完成，按<Enter>回主選單')
            break

def delete_data():
    while True:
        name = input('請輸入您欲刪除的帳號，輸入<Enter>結束:')
        if name == '':
            break
        if name not in data:
            print(f'您輸入的帳號 {name} 不存在!')
            continue
        print(f'刪除 {name} 的資料')
        yn = input('(Y / N)?')
        if (yn == 'Y' or yn == 'y'):
            del data[name]
            print('資料刪除完成!')
        else:
            print('資料未刪除!')
        with open('password.txt', 'w', encoding='utf8') as file:
            file.write(str(data))
            input('帳號刪除完成，按<Enter>回主選單')
            break



### 主程式從這裡開始 ###
data = dict()

data = read_data()  # 讀取文字檔後轉換為 dict
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice == 1:
        input_data()
    elif choice == 2:
         disp_data()
    elif choice == 3:
         edit_data()
    elif choice == 4:
         delete_data()
    else:
        break

print("程式執行完畢！")