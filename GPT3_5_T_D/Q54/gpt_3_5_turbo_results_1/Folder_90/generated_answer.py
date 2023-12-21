
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

def get_right_truncatables(n):
    truncatables = []
    for i in range(2, 10):
        num = int(str(n) + str(i))
        if is_prime(num):
            truncatables.extend(get_right_truncatables(num))
            truncatables.append(num)
    return truncatables

def all_right_truncatable_prime(numbers):
    x = numbers[466]
    right_truncatables = []
    for i in range(2, 10):
        if is_prime(i):
            right_truncatables.extend(get_right_truncatables(i))
            right_truncatables.append(i)
    right_truncatables = [num for num in right_truncatables if num < x]
    right_truncatables.sort(reverse=True)
    return right_truncatables
