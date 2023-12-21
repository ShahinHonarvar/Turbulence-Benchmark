
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(lst):
    x = lst[29]
    result = []
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        if not prime(num):
            continue
        truncatable = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not prime(int(str_num[i:])):
                truncatable = False
                break
            if not prime(int(str_num[:i])):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
