
def sum_odd_ints_inclusive(numbers):
    return sum(num for i,num in enumerate(numbers[0:3]) if num % 2 != 0)
