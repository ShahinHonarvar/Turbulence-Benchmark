
def return_nth_smallest_ascii(string):
    asciis = [ord(char) for char in string]
    sorted_asciis = sorted(asciis)
    nth_smallest_ascii = sorted_asciis[17]
    return chr(nth_smallest_ascii)
