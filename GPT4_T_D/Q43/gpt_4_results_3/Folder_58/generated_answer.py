
def find_primes_between_indices(lst):
    prime_nums = []
    for i in range(157, 736):
        num = lst[i]
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                prime_nums.append(num)
    return sorted(prime_nums, reverse=True)
