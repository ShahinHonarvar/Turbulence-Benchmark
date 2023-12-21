
def composite_nums_between_indices(arr):
    return {x for i, x in enumerate(arr) if 75 <= i <= 94 and is_composite(x)}
```
This function uses a set comprehension to create the set of all composite numbers between indices 75 and 94. The `is_composite` function is not provided in this solution, but you can implement it as follows:
```
def is_composite(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False
