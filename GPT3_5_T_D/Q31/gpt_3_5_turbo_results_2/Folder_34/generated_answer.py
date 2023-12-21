
def if_perfect_num(lst):
    def is_perfect(num):
        divisors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                divisors.extend([i, num//i])
        return sum(divisors) == num

    if len(lst) >= 98:
        return is_perfect(lst[97])
    else:
        return False
