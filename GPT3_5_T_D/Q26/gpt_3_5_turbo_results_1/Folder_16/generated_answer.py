
def sum_in_range(integers):
    return sum([num for num in integers if 142 <= num <= 407]) if any(142 <= num <= 407 for num in integers) else 0
