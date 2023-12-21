
def all_left_truncatable_prime(tuple):
    x = tuple[466]
    prime_numbers = []

    for i in range(2,x):
        is_prime = True

        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime = False

                break

        if is_prime:
            prime_numbers.append(i)

    return sorted(prime_numbers,reverse=True)
