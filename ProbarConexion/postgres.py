import cx_Oracle, string, getpass  
  
def main():  
  # Get password  
  pswd = getpass.getpass()  
        
  # Build connection string  
  user = "CS327_jdoe"  
  host = "oracle.microlab.cs.utexas.edu"  
  port = "1521"  
  sid = "orcl"  
  dsn = cx_Oracle.makedsn (host, port, sid)  
              
  # Connect to Oracle and test  
  con = cx_Oracle.connect (user, pswd, dsn)  
  if (con):  
    print "Connection successful"  
    print con.version  
  else:  
    print "Connection not successful"  
  
  con.close()  
  
main()  