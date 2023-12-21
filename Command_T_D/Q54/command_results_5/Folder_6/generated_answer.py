import re
def all_right_truncatable_prime(nums):
    return sorted(filter(lambda x: is_right_truncatable_prime(str(x)), nums))
def is_right_truncatable_prime(s):
    if not re.fullmatch(r'[2-9][\d]0+', s):
        return False
    #If rightmost digit is 9, then must be followed by 0, then another digit
    if s[0] == '9':
        if not s[1] == '0' or not s[2:]:
            return False
    #If rightmost digit is 8, then can be followed by any digit
    if s[0] == '8':
        return True
    #If rightmost digit is less than 8, then must be followed by 0, then another digit
    if s[0] != '9':
        if not s[1] == '0' or not s[2:]:
            return False
    return True
