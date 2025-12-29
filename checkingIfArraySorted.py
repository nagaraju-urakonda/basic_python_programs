#checking if array is sorted
array = list(map(int,input("enter numbers : ").split()))
is_sorted = True
for i in range(len(array) - 1):
    if array[i] > array[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("array is sorted",array)
else:
    print("array is not sorted")
    
