
def remove_repeat_chars(s):
    sub_str = s[3:5]
    for char in set(sub_str):
      if sub_str.count(char) > 1:
          s = s.replace(char, '')
    return s
