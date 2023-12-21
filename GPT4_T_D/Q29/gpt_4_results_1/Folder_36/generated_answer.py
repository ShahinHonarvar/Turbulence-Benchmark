
def gcf_two_nums(numbers):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    if not numbers or len(numbers) < 430:
        return None

    return gcf(numbers[429], numbers[289])
