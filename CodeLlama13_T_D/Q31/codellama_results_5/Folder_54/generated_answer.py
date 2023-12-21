
def if_perfect_num(numbers):
    if len(numbers) <= 50:
        return False
    n = numbers[50]
    s = sum(range(1, int(n**0.5)+1))
    return n == s*2
