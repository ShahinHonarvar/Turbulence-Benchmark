
def return_nth_smallest_ascii(string):
    characters = {char: i for i, char in enumerate(string)}
    indices = sorted([indices[i] for i in range(34, 68) if string[i] in characters])
    nth_smallest = sorted(indices)[5]
    return string[nth_smallest]
