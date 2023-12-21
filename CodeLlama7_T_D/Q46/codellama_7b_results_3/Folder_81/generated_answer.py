
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 20, 17 and 28
    gcf = my_list[20]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            gcf = gcd(gcf, my_list[i])
    return gcf
```
Note that the `gcd` function is used to calculate the greatest common divisor of two numbers. It is defined as follows:
```
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
