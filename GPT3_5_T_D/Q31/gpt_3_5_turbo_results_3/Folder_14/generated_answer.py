
def if_perfect_num(lst):
    def perfect_number(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        return sum(divisors) == num

    return perfect_number(lst[17]) if len(lst) > 17 else False
