
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[126]
    results = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            n = str(i)
            flag = True
            for j in range(len(n)):
                if not is_prime(int(n[:len(n)-j])):
                    flag = False
                    break
            if flag:
                results.append(i)
    results.sort(reverse=True)
    return results
