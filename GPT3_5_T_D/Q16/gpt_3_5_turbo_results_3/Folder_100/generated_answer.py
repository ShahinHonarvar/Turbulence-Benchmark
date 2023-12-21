 
def sum_even_ints_inclusive(numbers):
    count = 0
    for num in numbers[42:69]:
        if num % 2 == 0:
            count += num
    return count
