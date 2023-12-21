
def gcf_two_nums(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = arr[66]
    num2 = arr[90]
    
    return gcd(num1, num2)
