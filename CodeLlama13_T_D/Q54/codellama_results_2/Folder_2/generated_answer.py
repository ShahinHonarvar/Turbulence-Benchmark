
def all_right_truncatable_prime(numbers):
    x = numbers[618]
    prime_list = []
    for i in range(2,x):
        if is_prime(i) == True:
            prime_list.append(i)
    truncatable_prime_list = []
    for j in prime_list:
        temp = j
        while len(str(temp)) > 1:
            temp = int(str(temp)[:-1])
            if is_prime(temp) == True:
                truncatable_prime_list.append(j)
    return sorted(truncatable_prime_list)
