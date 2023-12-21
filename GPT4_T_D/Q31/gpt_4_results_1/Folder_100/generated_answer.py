
def if_perfect_num(numbers):
    def is_perfect(n):
        factors = [i for i in range(1,n) if n%i==0]
        return sum(factors) == n
    try:
        return is_perfect(numbers[99])
    except IndexError:
        return False
