
def prime_factors(numbers):
    # Calculate the set of all prime factors of the integer at index 222
    prime_factor_set = set()
    for i in range(len(numbers)):
        if i == 222:
            current_number = numbers[i]
            while current_number % 2 == 0:
                prime_factor_set.add(2)
                current_number //= 2
            for j in range(3, int(current_number ** 0.5) + 1, 2):
                while current_number % j == 0:
                    prime_factor_set.add(j)
                    current_number //= j
    return prime_factor_set
