
def gcf_three_nums(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return gcd(gcd(arr[66], arr[90]), arr[27])
