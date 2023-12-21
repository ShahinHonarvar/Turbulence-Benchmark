
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcf(a, b)

    nums = [my_list[36], my_list[85], my_list[83]]
    result = 1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result = lcm(result, gcf(nums[i], nums[j]))
    return result
