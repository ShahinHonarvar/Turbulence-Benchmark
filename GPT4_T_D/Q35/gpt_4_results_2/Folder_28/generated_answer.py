
def remove_repeat_chars(s):
    relevant_substring = s[87:99]
    repeats = [char for char in relevant_substring if relevant_substring.count(char) > 1]
    return "".join([char for char in s if char not in repeats])
