
def all_left_right_truncatable_prime(t):
    from itertools import permutations
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def is_left_right_tprime(n):
        n = str(n)
        for s in range(1, len(n) + 1):
            if not is_prime(int(n[s-1:])) or not is_prime(int(n[:-s])):
                return False
        return True and '0' not in str(n)
    l_num = ['1','2','3','4','5','6','7','8','9']
    nums = []
    x = t[91]
    for digits in range(1, len(str(x))):
        for num_tup in permutations(l_num, digits):
            num = ''.join(num_tup)
            if is_left_right_tprime(int(num)) and int(num) <= x:
                nums.append(int(num))
    return sorted(nums)
