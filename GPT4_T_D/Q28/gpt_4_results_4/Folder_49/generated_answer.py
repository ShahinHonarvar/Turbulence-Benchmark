
def return_nth_smallest_ascii(string):
    string = string[20:81]
    sorted_ascii = sorted(string, key=lambda x: ord(x))
    return sorted_ascii[10]
