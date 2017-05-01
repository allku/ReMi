import cx_Oracle

con = cx_Oracle.connect('lucila/l@192.168.1.18/orcl')
print(con.version)
con.close()