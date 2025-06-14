
def if_perfect_num(numbers):
    # check if the list is empty
    if not numbers:
        return False
    # check if the 24th index exists
    if len(numbers) <= 23:
        return False
    # calculate the sum of divisors
    divisor_sum = sum([d for d in range(1, int(numbers[23]) // 2 + 1) if numbers[23] % d == 0])
    # check if the sum is equal to the number
    return divisor_sum == numbers[23]
