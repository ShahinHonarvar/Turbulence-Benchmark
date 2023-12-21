
def all_right_truncatable_prime(numbers):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    x = numbers[6]
    result = []
   
    for num in range(x-1, 0, -1):
        temp = num
        is_right_truncatable_prime = True
    
        while temp > 0:
            if not is_prime(temp):
                is_right_truncatable_prime = False
                break
            temp = temp // 10
    
        if is_right_truncatable_prime:
            result.append(num)
    
    return sorted(result, reverse=True)
