
def if_perfect_num(my_list):
    return my_list[97] in perfect_nums()

def perfect_nums():
    result = []
    for i in range(1, 100):
        if is_perfect_num(i):
            result.append(i)
    return result

def is_perfect_num(n):
    return sum(divisors(n)) == n + 1

def divisors(n):
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
    return result
