
def remove_repeat_chars(your_string):
    selected_string = your_string[39:81]
    repeated_chars = {char for char in selected_string if selected_string.count(char) > 1}
    return ''.join(char for char in your_string if char not in repeated_chars)
