#Find the sum of all elements in an array

arr = [14, 22, 35, 41, 59]
def find_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

print(find_sum(arr))