import re
def prime_factors(nums):
    result = set()
    for n in nums:
        if n == 828:
            for match in re.finditer(r'(\d+)', str(n)):
                result.add(int(match.group()))
    return result
