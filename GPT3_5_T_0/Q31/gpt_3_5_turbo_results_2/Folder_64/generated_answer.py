
def if_perfect_num(lst):
    def is_perfect(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors) == num

    if len(lst) > 1 and is_perfect(lst[1]):
        return True
    else:
        return False
