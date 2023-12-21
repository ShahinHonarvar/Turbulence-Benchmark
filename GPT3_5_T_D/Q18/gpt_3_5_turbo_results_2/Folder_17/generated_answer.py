
def sum_ints_div_by_either_nums(numbers):
    start_index = 81
    end_index = 89
    divisors = [56, 68]
    sum_divisible = 0

    for num in numbers[start_index:end_index+1]:
        if any(num % divisor == 0 for divisor in divisors):
            sum_divisible += num

    return sum_divisible if sum_divisible != 0 else 0
