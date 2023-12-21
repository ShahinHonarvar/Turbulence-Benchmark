
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        return sum(divisors) == num

    if len(lst) > 537 and is_perfect_num(lst[537]):
        return True
    else:
        return False
