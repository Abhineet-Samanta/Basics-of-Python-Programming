import pymysql as p
# 3 things neede to be passed in myobj in p.connect(comma seperated)
#Server name->localhost , Username->root, Password->''
myobj = p.connect(host="localhost", user="root", password="")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")
except:
    print("database error")
