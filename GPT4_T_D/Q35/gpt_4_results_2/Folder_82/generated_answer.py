
def remove_repeat_chars(s):
    unique_char_list = []
    final_string_list = list(s)
    if len(s) > 200:
        for i in s[31:200]:
            if s[31:200].count(i) > 1 and i not in unique_char_list:
                unique_char_list.append(i)
                final_string_list = list(filter(lambda x: x != i, final_string_list))
    return "".join(final_string_list)
