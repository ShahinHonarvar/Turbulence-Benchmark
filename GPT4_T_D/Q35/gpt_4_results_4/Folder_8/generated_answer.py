
def remove_repeat_chars(s):
    char_counts = {}
    for i, ch in enumerate(s):
        if i > 45 and i < 48:
            if ch in char_counts:
                char_counts[ch] = char_counts[ch] + 1
            else:
                char_counts[ch] = 1
    for ch, count in char_counts.items():
        if count > 1:
            s = s.replace(ch, "")
    return s
