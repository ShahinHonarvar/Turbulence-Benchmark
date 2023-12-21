
def filter_chars(my_string):
    filtered_string = ""
    for char in my_string:
        if char >= "6" and char < "_":
            continue

        filtered_string += char

    return filtered_string
