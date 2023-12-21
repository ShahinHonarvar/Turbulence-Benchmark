
def if_perfect_num(lst):
    def perfect_check(num):
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num

    try:
        return perfect_check(lst[23])
    except IndexError:
        return False
