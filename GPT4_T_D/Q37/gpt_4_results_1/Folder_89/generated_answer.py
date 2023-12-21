
def filter_chars(text):
    characters = set(text[11:33])
    filtering_chars = [char for char in characters if '!' <= char <= '@']
    return ''.join(char for char in text if char not in filtering_chars)
