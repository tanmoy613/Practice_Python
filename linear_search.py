def linearsearch (arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print ("Index is ",i)
            break
    else:        
        print("Not present")

print("welcome to my linear search program.")
arr = [45, 78, 66, 52, 28, 36]
print("This is my array. Enter any number to search its index.")
print(arr)
x = int(input("Enter the number : "))

linearsearch(arr, x)
