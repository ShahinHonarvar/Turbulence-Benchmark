
def all_left_truncatable_prime(numbers):
    x = numbers[41]
    prime_list = []
    for i in range(2,x):
        if is_left_truncatable_prime(i) and i<x:
            prime_list.append(i)
    return sorted(prime_list)
def is_left_truncatable_prime(n):
    if n%10==0 or n%2==0 and n!=2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
