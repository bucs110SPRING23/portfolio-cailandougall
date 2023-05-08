euro=1
print ("What is the current exchange rate between euro and dollars?")
rate=float(input("Enter a number:"))
print ("How much currency should I exchange?")
amount=float(input("Enter a number:"))
total=rate*amount
print (total)
result=total-3
print ("Your result minus a $3 convenience fee is",  result)