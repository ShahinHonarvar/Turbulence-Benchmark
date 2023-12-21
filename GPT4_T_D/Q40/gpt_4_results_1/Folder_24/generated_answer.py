
def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=lambda x: ord(x))
    if len(sorted_chars) >= 32:
        result = sorted_chars[:32]
    else:
        result = sorted_chars + [' ']*(32-len(sorted_chars))
    return sorted(result, reverse=True)
