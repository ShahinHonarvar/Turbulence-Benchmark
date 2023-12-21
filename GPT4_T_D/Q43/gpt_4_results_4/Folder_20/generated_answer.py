
def find_primes_between_indices(lst):
    prime_numbers = []
    for i in lst[36:41]:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_numbers.append(i)
    prime_numbers = sorted(prime_numbers, reverse=True)
    return prime_numbers
