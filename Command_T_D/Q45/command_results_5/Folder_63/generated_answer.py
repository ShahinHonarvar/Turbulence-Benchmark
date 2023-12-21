import re
def palindromes_between_indices(text):
    text = re.sub("([A-Z])([A-Z])([A-Z])([A-Z])", r" \1 \2 \3 \4", text)
    return set(re.findall(r"([A-Z])([A-Z])([A-Z])([A-Z])", text))
