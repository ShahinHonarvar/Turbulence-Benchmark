def find_primes_between_indices(nums):
    start = next((i for i in range(len(nums)) if i % 2 == 0 and nums[i] < 55), -1)
    end = next((i for i in range(len(nums)) if i % 2 == 0 and nums[i] <= 87), -1)
    if start == -1 or end == -1:
        return []
    return sorted(nums[start:end+1])
