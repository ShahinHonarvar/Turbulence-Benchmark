import random
import string


# This function generates 100 unique rows of random suitable parameter values for the question and writes them to
# all_params.txt.
def gen_params(q_no, seed):
    if seed != "default":
        random.seed(seed)
    params = []
    s0 = string.ascii_letters
    s1 = string.punctuation
    chars = ["\\", "`", "'", '"']
    for char in chars:
        s1 = s1.replace(char, "")
    s2 = string.digits
    s = s0 + s1 + s2
    selected_range = (
        [range(0, 10)] * 10 + [range(10, 100)] * 70 + [range(100, 1000)] * 20
    )
    p0, p1, p2, p3 = "a", "a", 0, 0
    for a_range in selected_range:
        while (p0, p1, p2, p3) in params or ord(p1) <= ord(p0) + 1 or p3 <= p2 + 1:
            p0, p1 = random.sample(s, 2)
            p2, p3 = random.sample(a_range, 2)
        params.append((p0, p1, p2, p3))

    return params
