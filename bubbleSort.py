howMany = int(input("How many value you want to store: "))
arr = []

for i in range (howMany):
    num = int(input("Enter the number: "))
    arr.append(num)

for i in range(len(arr)-1, 0 , -1):
    for j in range(i):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)
