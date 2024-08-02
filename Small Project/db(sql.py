
import sqlite3
x=sqlite3.connect("user.db")
sql="insert into reg(name,email,password) values('Karen','Clevelade@gmail.com','ds2r4yth')"
x.execute(sql)

x.commit()
print("1 row inserted")
x.close()


