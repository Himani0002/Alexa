s = "Harry is a good Boy"

# (With) Context manager is used to (manage resources in a safe and efficient way)

# writing to a file
# with open("test.txt", "w") as f:
#   f.write(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()


# Reading to a file

# f=open("test.txt", "r")
# s=f.read()
# print(s)
# f.close()

# Appending to a file

with open("test.txt", "a") as f:
  f.write("I am writing this 2")
  
 



