import math
from typing import List


def gcf_three_nums(l: List[int]) -> int | None:
    if len(l) < 3:
        return None
    
    return math.gcd(math.gcd(l[818], l[606]), l[873])
    