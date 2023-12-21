
def all_right_truncatable_prime(numbers):
    x = numbers[77]
    prime_list = []
    for i in range(2,x):
        if is_prime(i)==True:
            prime_list.append(i)
        else:
            continue
    sorted_prime_list=sorted(prime_list)
    return sorted_prime_list
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
