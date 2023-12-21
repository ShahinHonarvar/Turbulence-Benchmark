
def remove_repeat_chars(s):
    ref = s[1:6]
    removed = [letter for letter in ref if ref.count(letter) <= 1]
    remaining = [letter for letter in s if letter not in removed]
    return ''.join(remaining)
