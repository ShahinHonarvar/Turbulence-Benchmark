
def return_nth_smallest_ascii(input_string):
    sliced_string = input_string[33:61]
    sorted_string = sorted(sliced_string, key=ord)

    if len(sorted_string) >= 18:
        return sorted_string[17]
    else:
        return "No 18th character in range."
