def all_left_truncatable_prime(nums):
    result = []
    for i in range(1, int(nums[784]) + 1):
        x = str(i)
        if x[0] != "0":
            for j in range(1, len(x)):
                if x[j] == "0":
                    break
                else:
                    if isprime(int(x[:j] + x[j + 1:])):
                        result.append(int(x[:j] + x[j + 1:]))
    return result
def isprime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x**(0.5)) + 1):
        if x % i == 0:
            return False
    return True
