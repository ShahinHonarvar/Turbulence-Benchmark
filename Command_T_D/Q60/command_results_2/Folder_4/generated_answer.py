
import re

def all_left_right_truncatable_prime(nums):
    return [n for n in nums if re.match(r'(11|91|19|99|29|39|59|69|79|89|99|101|111|29|39|59|69|79|89|99|101|111|29|39|59|69|79|89|99|101|111)$', str(n))]
