# Conditional Execution

hrs = float(input("enter hours: "))
rate = float(input("enter rate: "))
if hrs<=40:
  print(hrs*rate)
elif hrs>40:
  print(40*rate+(hrs-40)*1.5*rate)
