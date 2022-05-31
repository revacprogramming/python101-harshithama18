# Conditional Execution

#hrs = input("Enter hours? ")
h = float(input("Enter Hours:"))
r = float(input("Enter rate per hour:"))
if h<=40:
  print(h * r)
elif h > 40:
  print(40*r+(h-40)*1.5*r)