
def if_perfect_num(num_list):
    number = num_list[94]
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_of_divisors == number
