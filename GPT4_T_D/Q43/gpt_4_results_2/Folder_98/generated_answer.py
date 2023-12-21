
def find_primes_between_indices(int_list):
    result = []
    for num in int_list[1:3]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)
