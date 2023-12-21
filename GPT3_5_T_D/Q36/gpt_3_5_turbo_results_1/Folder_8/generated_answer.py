
def filter_chars(string):
    removed_chars = set()
    indices = []
    for i, char in enumerate(string):
        if 82 <= i < 93 and '!' < char < '*':
            removed_chars.add(char)
        if char not in removed_chars:
            indices.append(i)
    return ''.join([char for i, char in enumerate(string) if i in indices])
