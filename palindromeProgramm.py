n = int(input("enter a number"))

dummy = n
rev = 0
while n:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    
if rev == dummy:
    print("it is palindorme")
else:
    print("not palindorme")