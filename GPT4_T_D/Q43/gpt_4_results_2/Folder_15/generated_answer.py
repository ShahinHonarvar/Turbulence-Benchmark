
def find_primes_between_indices(lst):
    sub_list = lst[6:8]
    prime_list = []
    for num in sub_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list
