
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(25, 78):
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    
    nth_smallest = sorted(ascii_values)[16]
    for char in string:
        if ord(char) == nth_smallest:
            return char
