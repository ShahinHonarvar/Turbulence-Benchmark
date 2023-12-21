
def prime_factors(input_list):
    number = input_list[45]
    factors = set()
    for i in range(1, number + 1):
        if number % i == 0:
            factors.add(i)
    prime_factors = set()
    for num in factors:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_factors.add(num)
    return prime_factors
