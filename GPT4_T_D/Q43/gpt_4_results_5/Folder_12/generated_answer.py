
def find_primes_between_indices(number_list):
    prime_numbers = []
    for i in range(16, 26):
        if i < len(number_list):
            num = number_list[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        break
                else:
                    prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers
