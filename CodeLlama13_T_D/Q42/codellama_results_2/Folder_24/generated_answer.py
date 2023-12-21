
def prime_factors(numbers):
    prime_set = set()
    for num in numbers[74]:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime_set.add(i)
    return prime_set
