
def remove_repeat_chars(s):
    char_counts = {}
    for i in range(3, 7):
        if i < len(s):
            if s[i] in char_counts:
                char_counts[s[i]] += 1
            else:
                char_counts[s[i]] = 1

    final_str = ""
    for char in s:
        if char in char_counts and char_counts[char] > 1:
            continue
        final_str += char
    
    return final_str
