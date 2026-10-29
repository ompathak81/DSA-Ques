# Find the second highest element in an array

arr = [37, 55, 19, 85, 20]
def second_highest(arr):
    arr.sort(reverse=True)
    return arr[1]
print(second_highest(arr))