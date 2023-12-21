
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if len(lst) >= 9:
        return is_perfect_num(lst[8])
    else:
        return False
