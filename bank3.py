
import mysql.connector
from datetime import date
# /Users/jaisri_stuff/opt/anaconda3/lib/python3.9/site-packages


def clear():
    for _ in range(65):
        print()


def account_status(acno):
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    sql = "select status,balance from customer where acno ='"+acno+"'"
    result = cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result


def deposit_amount():
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    print("RESULT", result)
    if result[0] == "active":
        sql1 = "update customer set balance = balance+" + \
            amount + ' where acno = '+acno+' and status="active";'
        sql2 = 'insert into transaction(amount,type,acno,dateoftrans) values(' + \
            amount + ',"deposit",'+acno+',"'+str(today)+'");'
        cursor.execute(sql2)
        cursor.execute(sql1)
        conn.commit()
        # print(sql1)
        # print(sql2)
        print('\n\namount deposited')

    else:
        print('\n\nCAccount closed')

    wait = input('\n\n\n Press any key')
    conn.close()


def withdraw_amount():
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    if result[0] == 'active' and int(result[1]) >= int(amount):
        sql1 = "update customer set balance = balance-" + \
            amount + ' where acno = '+acno+' and status="active";'
        sql2 = 'insert into transaction(amount,type,acno,dateoftrans) values(' + \
            amount + ',"withdraw",'+acno+',"'+str(today)+'");'

        cursor.execute(sql2)
        cursor.execute(sql1)
        # print(sql1)
        # print(sql2)
        print('\n\namount Withdrawn')
        conn.commit()

    else:
        print('\n\nAccount closed')

    wait = input('\n\n\n Press any key.')

    conn.close()


def transaction_menu():
    while True:
        clear()
        print(' Trasaction Menu')
        print("\n1.  Deposit Amount")
        print('\n2.  WithDraw Amount')
        print('\n3.  Transaction Details')
        print('\n4.  Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            deposit_amount()
        if choice == 2:
            withdraw_amount()
        if choice == 3:
            account_details()
        if choice == 4:
            break


def add_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()

    name = input('Enter Name :')
    addr = input('Enter address ')
    phone = input('Enter Phone no :')
    email = input('Enter Email :')
    actype = input('Account Type (saving/current ) :')
    balance = input('Enter opening balance :')

    record = f'{name} {addr} {phone} {email} {actype} active {balance}'
    print(record)
    print("SLIT", record.split())
    cursor.execute(
        "insert into customer(name,address,phone,email,aacc_type,status,balance) values(%s,%s,%s,%s,%s,%s,%s)", record.split())
    conn.commit()
    cursor.close()

    print('New customer added successfully')


def modify_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    print('Modify screen ')
    print('\n 1.  Customer Name')
    print('\n 2.  Customer Address')
    print('\n 3.  Customer Phone No')
    print('\n 4.  Customer Email ID')
    choice = int(input('What do you want to change ? '))
    new_data = input('Enter New value :')
    field_name = ''
    if choice == 1:
        field_name = 'name'
    if choice == 2:
        field_name = 'address'
    if choice == 3:
        field_name = 'phone'
    if choice == 4:
        field_name = 'email'

    sql = f'update customer set {field_name} = \'{new_data}\' where acno={acno} ;'
    # sql = 'update customer set ' + field_name +
    #'="' + new_data + '" where acno='+acno+';'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    print('Customer Information modified..')


def account_details():
    clear()
    acno = input('Enter account no :')
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    sql = 'select * from customer where acno ='+acno+';'
    sql1 = 'select tid,dateoftrans,amount,type from transaction t where t.acno='+acno+';'
    cursor.execute(sql)
    result = cursor.fetchone()
    clear()
    print('Account Details')
    print('-'*45)
    print('Account No :', result[0])
    print('Customer Name :', result[1])
    print('Address :', result[2])
    print('Phone NO :', result[3])
    print('Email ID :', result[4])
    print('Account Type :', result[5])
    print('Account Status :', result[6])
    print('Current Balance :', result[7])
    print('-'*45)
    cursor.execute(sql1)
    results = cursor.fetchall()
    for result in results:
        print(result[0], result[1], result[2], result[3])

    conn.close()
    wait = input('\n\n\nPress any key')


def close_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankproject', user='test', password='testData1')
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql = 'update customer set status="close" where acno ='+acno+';'
    cursor.execute(sql)
    print('Account closed')


def main_menu():
    while True:
        clear()
        print(' Main Menu')
        print("\n1.  Add Account")
        print('\n2.  Modify Account')
        print('\n3.  Close Account')
        print('\n4.  Transactio Menu')
        print('\n5.  Close application')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            add_account()
        if choice == 2:
            modify_account()
        if choice == 3:
            close_account()
        if choice == 4:
            transaction_menu()
        if choice == 5:
            break


if __name__ == "__main__":
    main_menu()
