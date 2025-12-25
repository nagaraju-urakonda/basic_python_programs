#first min and second min
array = list(map(int, input("Enter numbers").split()))
firstMinimum = float("inf")
secondMinimum = float("inf")
for num in array:
    if num < firstMinimum :
        secondMinimum = firstMinimum
        firstMinimum = num
    elif num < secondMinimum and num != firstMinimum:
        secondMinimum = num
print(firstMinimum,secondMinimum)
