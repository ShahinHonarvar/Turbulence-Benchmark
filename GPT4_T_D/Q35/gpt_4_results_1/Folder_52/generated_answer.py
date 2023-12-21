
def remove_repeat_chars(s):
    between_38_and_81 = s[39:81]
    repeat_chars = set([char for char in between_38_and_81 if between_38_and_81.count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])
