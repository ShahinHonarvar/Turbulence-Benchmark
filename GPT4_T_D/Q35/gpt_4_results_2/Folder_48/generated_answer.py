
def remove_repeat_chars(s):
    substr = s[410:502]
    repeated_chars = [char for char in substr if substr.count(char) > 1]
    return "".join(char for char in s if char not in repeated_chars)
