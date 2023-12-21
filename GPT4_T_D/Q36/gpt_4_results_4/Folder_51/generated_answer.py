
def filter_chars(input_string):
    filtered_string = list(input_string)
    for char in input_string[59:81]:
        if '5' < char < '>':
            filtered_string = [x for x in filtered_string if x != char]
    return "".join(filtered_string) 
