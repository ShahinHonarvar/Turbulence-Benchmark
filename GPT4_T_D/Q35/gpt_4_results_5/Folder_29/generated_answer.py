
def remove_repeat_chars(s):
  chars = set(s[71:98])
  for char in chars:
    if s[71:98].count(char) > 1:
      s = s.replace(char, '')
  return s
