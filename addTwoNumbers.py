def insert():
       
      n1 = int(input('enter the two number'))
      n2 = int(input ('enter the two number'))
      return n1,n2

def compute(num1,num2):
      
      return  num1+num2
      




def main():
    num1,num2=insert()
    
    sum1=compute(num1,num2)
    
    print("The sum of two numbers{}".format(sum1))

main()    
