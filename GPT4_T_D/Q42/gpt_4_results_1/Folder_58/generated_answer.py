
def prime_factors(nums):
    def prime(num):
        if num < 2:
            return []
        for i in range(2, num):
            if num % i == 0:
                return [i] + prime(num//i)
        return [num]

    if len(nums) > 714:
        return set(prime(nums[714]))
    else:
        return "List index out of range"
