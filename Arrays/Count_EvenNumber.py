# Count the number of even numbers in an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count_even_numbers(arr):
    count = 0
    for n in arr:
        if n % 2 == 0:
            count += 1
    return count

print(count_even_numbers(arr))