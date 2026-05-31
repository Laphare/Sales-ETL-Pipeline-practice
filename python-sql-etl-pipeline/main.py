from file import FileReader,TextReader,JsonReader
from data_def import Rec
from pymysql import Connection


text_reader = TextReader('/Users/laphare/Desktop/project/py/sales_2011_02.txt')
json_reader = JsonReader('/Users/laphare/Desktop/project/py/sales_2011_03.txt')
Feb_data:list[Rec] = text_reader.read_data()
Mar_data:list[Rec] = json_reader.read_data()

all_data:list[Rec] = Feb_data+Mar_data

conn=Connection(
    host='localhost',
    port=3306,
    user='root',
    password='12345678',
    autocommit=True
)

cursor=conn.cursor()
conn.select_db('py_sql')

sql = "INSERT INTO orders(order_date, order_id, amount, country) VALUES (%s, %s, %s, %s)"
for rec in all_data:
    data_tuple = (rec.date, rec.id, rec.amount, rec.country)
    cursor.execute(sql, data_tuple)

conn.commit()

print(f"🎉 成功把 {len(all_data)} 条销售数据洗入 py_sql 数据库！")

cursor.close()
conn.close()