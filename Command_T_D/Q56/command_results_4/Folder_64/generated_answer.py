import re
def all_substring_of_size_n(s):
    return re.findall(r'(?<=.)(.)\1\1(.)\2\2(.)\3\3(.)\4\4(.)\5\5(.)\6\6(.)\7\7', s)
