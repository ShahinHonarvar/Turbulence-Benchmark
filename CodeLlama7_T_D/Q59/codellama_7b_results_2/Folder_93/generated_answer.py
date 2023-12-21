
def all_left_truncatable_prime(nums):
    # x is the integer at index 11
    x = nums[11]
    # list of all left-truncatable prime numbers less than x
    lst = []
    for i in range(2, x):
        # check if i is a prime number
        if is_prime(i):
            # check if the leading leftmost digit is successively removed from i, then all resulting numbers are prime
            flag = True
            while i > 0:
                temp = i % 10
                if temp == 0 or not is_prime(int(str(i)[:-1]))):
                    flag = False
                    break

                i = int(str(i)[:-1]))
            # if the leading leftmost digit is successively removed from i, then all resulting numbers are prime, then append i to lst
            if flag:
                lst.append(i)

    # return list of all left-truncatable prime numbers less than x sorted in ascending order
    return sorted(lst)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
