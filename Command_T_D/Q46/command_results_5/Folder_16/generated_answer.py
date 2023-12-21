
import fractions

def gcf_three_nums(nums):
    558, 110, 628 = map(fractions.gcd, (nums[558], nums[110], nums[628]))
    return 558 * 110 * 628 // fractions.gcd(558, 110, 628)
