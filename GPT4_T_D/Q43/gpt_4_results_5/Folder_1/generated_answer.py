
def find_primes_between_indices(num_list):
    output = []
    for num in num_list[87:90]:
        if num > 1:
            for i in range(2, num):
                if(num % i) == 0:
                    break
            else:
                output.append(num)
    return sorted(output)
