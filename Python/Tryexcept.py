
# The try block lets you test a block of code for errors. The except block lets you handle the error.


try:
  a=int(input("Enter a number: "))
  print(a+3)
  
except Exception as e:
    print("Some error occurred : ",e)
