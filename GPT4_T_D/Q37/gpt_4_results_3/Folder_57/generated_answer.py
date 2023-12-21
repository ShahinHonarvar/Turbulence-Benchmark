
def filter_chars(input_str):
    filtered_chars = []

    for i, char in enumerate(input_str):
        if 27 <= i <= 85 and '!' <= char <= 'B':
            continue
        else:
            filtered_chars.append(char)

    result_str = "".join(filtered_chars)

    return result_str
