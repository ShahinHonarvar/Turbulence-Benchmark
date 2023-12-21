
def if_perfect_num(integers):
    num = integers[321]
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num
