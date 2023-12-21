
def filter_chars(string):
    start_index = 81
    end_index = 86
    exclusion_start = '!'
    exclusion_end = 's'

    filtered_string = string[:start_index] + ''.join([char for char in string[start_index:end_index] if not exclusion_start < char < exclusion_end]) + string[end_index:]
    return filtered_string
