def all_even_ints_exclusive(nums):
    result = [n for n in nums if n % 2 == 0]
    return result[:90] + result[90:-200] + result[-200:]
