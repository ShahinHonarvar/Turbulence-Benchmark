
def remove_repeat_chars(input_string):
    work_string = input_string[21:35]
    used_chars = set()
    for ch in work_string:
        if work_string.count(ch) > 1:
            used_chars.add(ch)
    for ch in used_chars:
        input_string = input_string.replace(ch, "")
    return input_string
