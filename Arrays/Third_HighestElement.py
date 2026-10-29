# Find the third highest element in an array
arr = [37, 55, 19, 85, 20]

def third_highest(arr):
    arr.sort(reverse=True)
    return arr[2]

print(third_highest(arr))