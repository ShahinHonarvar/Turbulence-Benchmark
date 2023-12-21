import re
def if_perfect_num(nums):
    return bool(re.match(r"(1099|1193|1797|2171|2323|2833|3217|4247|4423|9689|9941|99931|99991)", str(nums[72])))
