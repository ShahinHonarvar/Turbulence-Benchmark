
def sum_of_divisors_in_range(integer):
    divisors_sum = 0
    for num in range(469, 683):
        if integer % num == 0:
            divisors_sum += num
    return divisors_sum
