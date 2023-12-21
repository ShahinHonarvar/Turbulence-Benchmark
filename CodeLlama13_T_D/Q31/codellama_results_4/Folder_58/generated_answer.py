
def if_perfect_num(numbers):
    for i in range(len(numbers)):
        if i == 714:
            return is_perfect(numbers[i])
    return False

def is_perfect(n):
    return n == sum(range(1, int(sqrt(n)) + 1)) and all(n % d for d in range(2, int(sqrt(n)) + 1) if n % d == 0)
