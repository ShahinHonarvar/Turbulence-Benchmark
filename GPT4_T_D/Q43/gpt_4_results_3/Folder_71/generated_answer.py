
def find_primes_between_indices(input_list):
    primes = []
    for i in range(57, 65):
        if i >= len(input_list):
            break
        num = input_list[i]
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
