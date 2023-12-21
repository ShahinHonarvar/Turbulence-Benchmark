 
def find_primes_between_indices(nums):
    lst = []
    for i in range(35, 89):
        if all(nums[j] % i for j in range(1, len(nums) + 1)):
            lst.append(i)
    return sorted(lst)
