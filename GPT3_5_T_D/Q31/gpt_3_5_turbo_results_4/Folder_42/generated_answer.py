
def if_perfect_num(lst):
    def is_perfect_number(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return num == sum(divisors)

    return is_perfect_number(lst[276])
