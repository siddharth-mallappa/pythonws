def myinput():
     dbname=input("Enter the Databasenaem")
     username=input("Enter the username")
     passwd=input("Enter the password")
     user=input("Enter the user name")
     return dbname,username,passwd,user



dbname, username, passwd,user=myinput()
print("Databasename={}  username={} password={} user={}".format( dbname, username, passwd,user))    
    
    
    
 
