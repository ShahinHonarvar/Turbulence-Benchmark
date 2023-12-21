
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(1, int(len(str(n))/2)):
        prime = True
        for div in range(2, int(n**0.5)+1):
            if n % div == 0:
                prime = False
                break
        if not prime:
            return False
    return True
