
def return_nth_smallest_ascii(string):
    characters = {ord(char): char for char in string}
    nth_smallest = sorted(characters)[18:67]
    return nth_smallest[18]
