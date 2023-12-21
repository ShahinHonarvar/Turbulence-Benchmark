
def find_primes_between_indices(int_list):
    prime_lst = []
    
    if len(int_list)< 449: return [] #If list length is less than intended index.
    
    for num in int_list[413:449]: 
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_lst.append(num)

    return sorted(prime_lst)
