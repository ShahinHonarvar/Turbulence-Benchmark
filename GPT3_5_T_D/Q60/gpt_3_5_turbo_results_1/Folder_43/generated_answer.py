
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    results = []
    x = numbers[89]
    
    for num in range(x, 0, -1):
        if all(int(digit) != 0 for digit in str(num)):
            truncated_num = num
            
            while is_prime(truncated_num):
                truncated_num = int(str(truncated_num)[1:-1])
                if truncated_num < 10:
                    results.append(num)
                    break
    
    results.sort(reverse=True)
    return results
