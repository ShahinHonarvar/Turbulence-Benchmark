
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    import itertools, math
  
    def is_prime(n):
        if n < 2: return False
        for number in range(2, int(math.sqrt(n)) + 1):
            if n % number == 0: 
                return False
        return True

    def check_lr_truncatable(num):
        str_num = str(num)
        if '0' in str_num: 
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True

    x = tuple_of_positive_integers[10]
    primes = (number for number in range(x+1) if is_prime(number))
   
    lr_truncatable_primes = [num  for num in primes if check_lr_truncatable(num)]
    lr_truncatable_primes.sort(reverse=True)
  
    return lr_truncatable_primes
