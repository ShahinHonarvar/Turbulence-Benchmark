
def return_n_greatest_chars(str):
    if len(str) < 90:
        return "The given string does not contain enough distinct characters."

    sorted_chars = sorted(str, key=ord, reverse=True)
    return sorted_chars[:90]
