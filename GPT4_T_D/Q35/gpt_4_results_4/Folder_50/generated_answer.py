
def remove_repeat_chars(s):
    char_counts = {}
    for i in range(14, min(77, len(s))):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    modified_list = [char if char not in char_counts or char_counts[char] == 1 else '' for char in s]
    return ''.join(modified_list)
