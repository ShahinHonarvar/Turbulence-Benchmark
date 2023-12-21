
def all_right_truncatable_prime(numbers):
    x = numbers[41]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_list.append(i)
    
    right_truncatable_list = []
    for i in prime_list:
        j = str(i)
        while len(j) > 1:
            k = int(j[:-1])
            if is_prime(k):
                right_truncatable_list.append(k)
            j = j[:-1]
    
    return sorted(right_truncatable_list, reverse=True)
