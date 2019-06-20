def myinput():
     dbname=input("Enter the Databasenaem")
     username=input("Enter the username")
     passwd=input("Enter the password")
     user=input("Enter the user name")
     return dbname,username,passwd,user

def connect( dbname,username,passwd,user ):

    
    print("Databasename={}  username={} password={} user={}".format( dbname, username, passwd,user))

dbname, username, passwd,user=myinput()
connect( dbname, username, passwd, user )
    
    
    
    
 
