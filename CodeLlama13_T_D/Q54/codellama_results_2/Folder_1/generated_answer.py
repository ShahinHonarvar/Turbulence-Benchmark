
def all_right_truncatable_prime(numbers):
    x = numbers[20]
    prime_list = []
    
    for num in range(10, x+1):
        if is_prime(num) and is_right_truncatable(num):
            prime_list.append(num)
            
    return sorted(prime_list, reverse=True)
