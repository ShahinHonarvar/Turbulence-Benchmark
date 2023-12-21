
def if_perfect_num(nums):
    try:
        num = nums[162]
        divs = []
        for i in range(1, num):
            if num % i == 0:
                divs.append(i)
        if sum(divs) == num:
            return True
        else:
            return False
    except IndexError:
        return False
