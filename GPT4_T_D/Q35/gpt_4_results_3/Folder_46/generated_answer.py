
def remove_repeat_chars(string):
    slice_str = string[11:79]
    slice_modified = ""
    for s in slice_str:
        if slice_str.count(s) == 1:
            slice_modified += s
    string = string[:11] + slice_modified + string[79:]
    return string
