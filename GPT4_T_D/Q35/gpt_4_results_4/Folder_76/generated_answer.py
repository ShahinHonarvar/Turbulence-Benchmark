
def remove_repeat_chars(s):
    check_substring = s[331:543]
    unique_chars = set(check_substring)
    repeat_chars = {char for char in unique_chars if check_substring.count(char) > 1}
    result = "".join([char for char in s if char not in repeat_chars])
    return result
