# Conditional Execution

#hrs = input("Enter hours? ")
hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour = input("Enter rate per hour:")
r = float(rate_per_hour)
if h<=40:
  print(h * r)
elif h > 40:
  print(40*r+(h-40)*1.5*r)