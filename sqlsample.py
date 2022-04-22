import mysql.connector

conn = mysql.connector.connect(
    host='localhost', database='bankproject', user='test', password='testData1')
cursor = conn.cursor()

name = input('Enter Name :')
addr = input('Enter address ')
phone = input('Enter Phone no :')
email = input('Enter Email :')
actype = input('Account Type (saving/current ) :')
balance = input('Enter opening balance :')


# s = f'{s1} {s2} {s3}'
record = f'{name}, {addr}, {phone}, {email}, {actype}, "active", {balance}'
print(record)
print("SLIT", record.split())
cursor.execute(
    "insert into customer(name,address,phone,email,aacc_type,status,balance) values(%s,%s,%s,%s,%s,%s,%s)", record.split())
conn.commit()
cursor.close()
