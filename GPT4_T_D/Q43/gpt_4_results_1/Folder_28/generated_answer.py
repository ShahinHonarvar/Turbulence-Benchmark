
def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(38, 55):
        if i < len(int_list):
            num = int_list[i]
            if num > 1:
                for j in range(2, num):
                    if (num % j) == 0:
                        break
                else:
                    prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list
