
def find_primes_between_indices(int_list):
    prime_list = []
    for i in int_list[70:72]:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_list.append(i)
    return sorted(prime_list, reverse=True)
