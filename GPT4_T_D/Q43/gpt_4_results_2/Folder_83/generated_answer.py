
def find_primes_between_indices(integer_list):
    prime_numbers = []
    for i in range(14, min(74, len(integer_list))): 
        number = integer_list[i]
        if number > 1:
            is_prime = True
            for j in range(2, number):
                if (number % j) == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)
