
def sum_even_ints_inclusive(numbers):
    start_index, end_index = 686, 987
    sum_even = sum(num for num in numbers[start_index:end_index+1] if num % 2 == 0)
    return sum_even if sum_even else 0
