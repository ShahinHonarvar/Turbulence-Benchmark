
def find_primes_between_indices(lst):
    prime_number_list = []
    desired_list = lst[7:10]
    for num in desired_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_number_list.append(num)
    return sorted(prime_number_list, reverse=True)
