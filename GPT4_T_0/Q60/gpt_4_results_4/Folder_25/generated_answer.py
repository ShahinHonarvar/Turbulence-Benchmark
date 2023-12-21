
def all_left_right_truncatable_prime(t):
    x = t[92]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)) and '0' not in str(num):
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:-1]
                if not all(int(temp)%i!=0 for i in range(2, int(int(temp)**0.5)+1)):
                    break
            else:
                primes.append(num)
    return sorted(primes)
