
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
  
    num1 = lst[13]
    num2 = lst[70]
    num3 = lst[32]
  
    result = gcd(gcd(num1, num2), num3)
    return result
