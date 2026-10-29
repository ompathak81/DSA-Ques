# Find the smallest element in an array
arr = [37, 55, 19, 85, 20]
def find_min(arr):
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element

print(find_min(arr))