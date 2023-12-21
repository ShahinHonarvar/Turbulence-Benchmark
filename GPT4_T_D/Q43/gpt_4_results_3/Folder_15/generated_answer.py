
def find_primes_between_indices(int_list):
    prime_list = []
    for num in int_list[6:8]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)
