
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        primes = []
        for i in range(x, 10**len(str(x))-1, -1):
            num = str(i)
            if int(num[0]) not in [1, 2, 3, 5, 7] or "0" in num:
                continue
            if is_prime(i):
                flag = True
                for j in range(1, len(num)):
                    left_trunc = int(num[j:])
                    right_trunc = int(num[:-j])
                    if not is_prime(left_trunc) or not is_prime(right_trunc):
                        flag = False
                        break
                if flag:
                    primes.append(i)
        result.extend(primes)
    return sorted(result, reverse=True)
