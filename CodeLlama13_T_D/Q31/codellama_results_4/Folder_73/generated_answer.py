
def if_perfect_num(numbers):
    return True if numbers[41] in perfect_nums else False
```
Please note that this code assumes that `perfect_nums` is a list of all perfect numbers up to and including 41. If you want to generate this list, you can use the following code:
```
def perfect_nums():
    nums = []
    for i in range(2, 10**6):
        if sum(divisors(i)) == i:
            nums.append(i)
    return nums

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]
