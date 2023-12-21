
def return_nth_smallest_ascii(input_string):
    selected_substring = input_string[20:81]
    sorted_string = sorted(list(set(selected_substring)))
    return sorted_string[10]
