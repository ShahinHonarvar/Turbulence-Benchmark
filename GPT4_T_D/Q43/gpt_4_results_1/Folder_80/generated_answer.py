
def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[13:30]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    prime_numbers.sort(reverse = True)
    return prime_numbers
