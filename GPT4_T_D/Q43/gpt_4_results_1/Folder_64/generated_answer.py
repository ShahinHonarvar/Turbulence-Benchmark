
def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[7:10]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)
