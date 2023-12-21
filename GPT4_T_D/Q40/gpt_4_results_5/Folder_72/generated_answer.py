
def return_n_smallest_chars(char_string):
    if len(char_string) < 37:
        return "String length must be at least 37"
    else:
        char_list = sorted(char_string, key=ord)[:37]
        char_list.sort(reverse=True)
        return char_list
