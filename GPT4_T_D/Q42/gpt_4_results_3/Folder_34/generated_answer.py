
def prime_factors(numbers):
    num = numbers[97]
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
    return set([number for number in factors if all(number % num != 0 for num in range(2, number))])
