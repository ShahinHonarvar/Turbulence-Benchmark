
import fractions

def gcf_three_nums(nums):
    gcf = 1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                gcf = fractions.gcd(gcf, nums[i])
                if gcf == 1:
                    break
            if gcf == 1:
                break
    return gcf
