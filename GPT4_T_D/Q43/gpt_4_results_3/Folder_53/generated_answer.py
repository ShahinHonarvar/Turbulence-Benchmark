
def find_primes_between_indices(numbers):
    prime_sublist = []
    for i in range(43, 60):
        if i < len(numbers):
            number = numbers[i]
            if number > 1:
                for j in range(2, number):
                    if (number % j) == 0:
                        break
                else:
                    prime_sublist.append(number)
    return sorted(prime_sublist, reverse=True)
