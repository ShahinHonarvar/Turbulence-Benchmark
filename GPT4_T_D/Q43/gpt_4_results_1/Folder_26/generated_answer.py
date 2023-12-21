
def find_primes_between_indices(int_list):
    prime_numbers = []
    for num in int_list[23:49]:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return sorted(prime_numbers)
