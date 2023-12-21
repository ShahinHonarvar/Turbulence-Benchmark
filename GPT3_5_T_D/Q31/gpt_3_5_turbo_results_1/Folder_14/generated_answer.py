
def if_perfect_num(lst):
    def is_perfect(num):
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == num

    return is_perfect(lst[17])
