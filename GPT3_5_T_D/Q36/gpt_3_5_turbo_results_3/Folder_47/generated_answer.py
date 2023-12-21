
def filter_chars(string):
    string = list(string)
    for i in range(45, 57):
        if 'F' < chr(i) < 'n':
            string = [char for char in string if char != chr(i)]
    return ''.join(string)
