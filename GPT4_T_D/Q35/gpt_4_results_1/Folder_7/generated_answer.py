
def remove_repeat_chars(s):
    s_list = list(s)
    repeat_chars = set()
    for i in range(376, 926):
        if s[i] in s_list[376:i] or s_list[i+1:926].count(s[i]) > 0:
            repeat_chars.add(s[i])
    for char in repeat_chars:
        s_list = list(filter(lambda x: x != char, s_list))
    return ''.join(s_list)
