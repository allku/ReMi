# -*- coding: utf-8 -*-
import cx_Oracle, string, getpass  
  
def main():  
  # Get password  
  pswd = getpass.getpass()  
        
  # Build connection string  
  user = "lucila"  
  host = "192.168.1.18"  
  port = "1521"  
  sid = "orcl"  
  dsn = cx_Oracle.makedsn (host, port, sid)  
              
  # Connect to Oracle and test  
  con = cx_Oracle.connect (user, pswd, dsn)  
  if (con):
    print("Conexión establecida")  
    print("Versión: " + con.version)  
  else:  
    print("Conexión no establecida")  
  
  con.close()  
  
main()  