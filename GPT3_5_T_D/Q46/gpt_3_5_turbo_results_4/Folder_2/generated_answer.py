
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
    list = [numbers[307], numbers[920], numbers[463]]
    gcf = list[0]
    for num in list[1:]:
        gcf = gcd(gcf, num)
    return gcf
