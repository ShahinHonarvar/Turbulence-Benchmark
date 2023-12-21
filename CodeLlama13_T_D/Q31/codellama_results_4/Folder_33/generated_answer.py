
def if_perfect_num(my_list):
    if len(my_list) <= 321:
        return False
    else:
        n = my_list[321]
        sum_of_divisors = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if n / i == i:
                    sum_of_divisors += i
                else:
                    sum_of_divisors += i + (n // i)
        return sum_of_divisors == n
