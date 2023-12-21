
def if_perfect_num(numbers):
    n = numbers[41]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and sum([d*d for d in [i, (n//i)]]) == n:
            return True
    return False
