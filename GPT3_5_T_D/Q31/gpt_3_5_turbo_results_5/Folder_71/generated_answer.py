
def if_perfect_num(lst):
    def is_perfect(num):
        if num <= 1:
            return False
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != 1 and num // i != i:
                    divisors.append(num // i)
        return sum(divisors) == num

    return is_perfect(lst[78])
