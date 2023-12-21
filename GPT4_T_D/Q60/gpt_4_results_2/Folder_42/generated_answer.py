
def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    primes = []
    for num in range(2, x + 1):
        if all(num%i!=0 for i in range(2, int(num**.5)+1)) and str(num).find('0') == -1:
            str_num = str(num)
            left_right_prime = True
            for i in range(len(str_num)):
                if not all(int(str_num[i:])%i!=0 for i in range(2, int(int(str_num[i:])**.5)+1)):
                    left_right_prime = False
                    break
                if not all(int(str_num[:len(str_num)-i])%i!=0 for i in range(2, int(int(str_num[:len(str_num)-i])**.5)+1)):
                    left_right_prime = False
                    break
            if left_right_prime:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
