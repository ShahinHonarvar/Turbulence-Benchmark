
def remove_repeat_chars(input_string):
    selected_string = input_string[45:91]
    repeat_chars = [ch for ch in selected_string if selected_string.count(ch) > 1]
    return ''.join(ch for ch in input_string if ch not in repeat_chars)
