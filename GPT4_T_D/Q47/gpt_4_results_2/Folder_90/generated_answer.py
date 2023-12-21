
def palindromes_of_specific_lengths(s):
    import re
    
    sub_s = s[106:281].lower()
    
    valid_chars = re.sub(r'[^a-z]', '', sub_s)
  
    total_chars = len(valid_chars)

    pal_set = set()

    for i in range(total_chars):
        for l in range(136, min(152, total_chars - i + 1)):
            segment = valid_chars[i:i+l]
              
            if segment == segment[::-1]:
                pal_set.add(segment)
              
    return pal_set
