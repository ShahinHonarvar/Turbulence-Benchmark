
def find_primes_between_indices(int_list):
    prime_nums = []
    for val in int_list[40:69]:
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                prime_nums.append(val)
    prime_nums.sort(reverse=True)
    return prime_nums
