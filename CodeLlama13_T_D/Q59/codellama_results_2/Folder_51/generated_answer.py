
def all_left_truncatable_prime(numbers):
    x = numbers[54]
    prime_list = []
    for num in range(2,x+1):
        if is_prime(num) and '0' not in str(num):
            prime_list.append(num)
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            if str(prime_list[j]) in str(prime_list[i]):
                prime_list.pop(j)
    return prime_list
