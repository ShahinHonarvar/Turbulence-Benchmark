
def all_right_truncatable_prime(numbers):
    x = numbers[14]
    prime_list = []
    
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            
            while len(str(i)) > 1:
                i = int(str(i)[:-1])
                
                if not is_prime(i):
                    right_truncatable = False
                    break
            
            if right_truncatable:
                prime_list.append(i)
    
    return sorted(prime_list, reverse=True)
