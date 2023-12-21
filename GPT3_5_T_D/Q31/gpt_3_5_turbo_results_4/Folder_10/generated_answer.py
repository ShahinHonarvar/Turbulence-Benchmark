
def if_perfect_num(lst):
    def is_perfect_num(num):
        factors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        return sum(factors) == num

    if len(lst) > 54 and is_perfect_num(lst[54]):
        return True
    return False
