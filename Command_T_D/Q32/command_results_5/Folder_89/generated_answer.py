import re
def insert_after_character(text):
    return re.sub(r"([A-Z])", r"\1W", text)
