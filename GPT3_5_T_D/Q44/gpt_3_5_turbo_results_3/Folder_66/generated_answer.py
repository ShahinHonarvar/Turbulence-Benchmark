
def composite_nums_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_composite(num):
        return not is_prime(num)

    composite_nums = set()
    for num in numbers[62:64]:
        if is_composite(num):
            composite_nums.add(num)
    
    return composite_nums
