import re
def if_decimal_is_divisible(s):
    return int(re.sub(r'0+', '', s), 2) == 987559822365390484250565527365546887552711280348959962810559855987
def __starting_point():
    print(if_decimal_is_divisible("100110001100001"))
