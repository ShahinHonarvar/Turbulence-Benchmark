
def gcf_three_nums(nums):
    return find_gcf([nums[62], nums[96], nums[26]])
```
The `find_gcf` function is a helper function that takes a list of numbers and returns their greatest common factor. It uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two numbers, and then iteratively applies the same process to find the GCD of the remaining numbers until only one number remains.
```
def find_gcf(nums):
    if len(nums) == 0:
        return None
    gcd = nums[0]
    for i in range(1, len(nums)):
        while True:
            remainder = gcd % nums[i]
            if remainder == 0:
                break
            gcd = nums[i] - remainder
    return gcd
