def prime_factors(nums):
    return set(
        str(nums[57])
        .replace(" ","")
        .replace("'","")
        .replace("(","")
        .replace(")","")
        .split("'")
    )
