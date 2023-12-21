
def return_nth_smallest_ascii(string):
    nth_smallest = 6
    indices = range(8, 27)
    characters = [c for c in string if ord(c) in indices]
    return sorted(characters)[nth_smallest - 1]
