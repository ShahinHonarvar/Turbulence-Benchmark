
def if_perfect_num(lst):
    return lst[73] in list_of_perfect_numbers()

def list_of_perfect_numbers():
    perfect_numbers = []
    for i in range(1, 100):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers

def is_perfect_number(n):
    if n <= 1:
        return False
    sum_of_divisors = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_divisors += i + n // i
    return sum_of_divisors == n * (n + 1) / 2
