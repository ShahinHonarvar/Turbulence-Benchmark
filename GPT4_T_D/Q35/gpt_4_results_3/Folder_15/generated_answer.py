
def remove_repeat_chars(s):
    char_counts = {}
    for index in range(1, 4): 
      if index < len(s):
          if s[index] in char_counts:
              char_counts[s[index]] += 1
          else:
              char_counts[s[index]] = 1

    new_s = ''
    for char in s:
        if char not in char_counts or char_counts[char] == 1:
            new_s += char

    return new_s
