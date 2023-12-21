
def filter_chars(string):
    start_index = 1
    end_index = 7
    
    for i in range(start_index, end_index):
        if string[i] > '-' and string[i] < 'L':
            string = string.replace(string[i], '')
    
    return string
