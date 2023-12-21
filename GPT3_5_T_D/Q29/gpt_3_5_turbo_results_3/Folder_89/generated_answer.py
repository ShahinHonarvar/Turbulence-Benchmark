
def gcf_two_nums(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(arr[37], arr[30])
