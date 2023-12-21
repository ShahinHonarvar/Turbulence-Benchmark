
def if_perfect_num(numbers):
    return numbers[790] in perfect_numbers()

def perfect_numbers():
    perfect = []
    for i in range(1, 800):
        if sum(divisors(i)) == i:
            perfect.append(i)
    return perfect

def divisors(n):
    divisors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    return sorted(divisors)
