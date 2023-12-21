
def sum_even_ints_inclusive(numbers):
    sum_of_evens = 0
    for number in numbers[91:100]:
        if number % 2 == 0:
           sum_of_evens += number
    return sum_of_evens
