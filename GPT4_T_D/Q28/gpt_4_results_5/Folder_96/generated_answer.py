
def return_nth_smallest_ascii(string):
    sliced_string = string[:18]
    sorted_string = sorted(sliced_string)
    return sorted_string[17]
