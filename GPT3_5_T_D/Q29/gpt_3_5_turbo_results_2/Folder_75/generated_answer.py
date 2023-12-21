
def gcf_two_nums(numbers):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return find_gcf(numbers[42], numbers[25])
