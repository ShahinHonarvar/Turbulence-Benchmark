
def if_perfect_num(lst):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if len(lst) < 19:
        return False
    num_at_index_18 = lst[18]
    return is_perfect(num_at_index_18)
