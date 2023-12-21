
def if_perfect_num(integers):
    def is_perfect(num):
        if num <= 0:
            return False
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num / i)
        if sum(divisors) == num:
            return True
        return False
    
    return is_perfect(integers[0])
