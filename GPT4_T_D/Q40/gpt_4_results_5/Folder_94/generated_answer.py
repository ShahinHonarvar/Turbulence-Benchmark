
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string)
    if len(sorted_string) >= 87:
        return sorted_string[:87][::-1]
    else:
        return "The string does not contain enough distinct characters."
