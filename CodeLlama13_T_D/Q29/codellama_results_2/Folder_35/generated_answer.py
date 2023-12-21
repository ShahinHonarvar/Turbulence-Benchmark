
def gcf_two_nums(numbers):
    if len(numbers) < 380 or len(numbers) < 327:
        return None
    else:
        num1 = numbers[380]
        num2 = numbers[327]
        for i in range(min(num1, num2), 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i
        return 1
