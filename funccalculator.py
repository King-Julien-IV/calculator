''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

def al():
   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")

   # Take input from the user 
   choice = str(input("Enter choice(1/2/3/4):"))

   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))

   if choice == '1':
       print("{} + {} = {}".format(num1, num2, float(add(num1,num2))))
     
   

   elif choice == '2':
       print("{} - {} = {}".format(num1, num2, float(subtract(num1,num2))))

   elif choice == '3':
       print("{} x {} = {}".format(num1, num2, float(multiply(num1,num2))))

   elif choice == '4':
       print("{} / {} = {}".format(num1, num2, float(divide(num1,num2))))
   else:
       print("Invalid input")
   def spelling():
      goover = input("Run calculator Again?(yes or no) : ").lower()
      yes = "yes"
      no = "no"
      if goover == yes:
         al()
      
      elif goover == no:
         print("bye")
      else:
         print("you spelt something wrong")
         spelling()
   spelling()

al()

      
   
   


