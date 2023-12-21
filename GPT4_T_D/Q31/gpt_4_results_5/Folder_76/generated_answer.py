
def if_perfect_num(number_list):
    perfect_number = number_list[537]
    sum_of_divisors = sum([i for i in range(1,perfect_number) if perfect_number % i == 0])
    return sum_of_divisors == perfect_number
