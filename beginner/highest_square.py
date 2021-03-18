"""
exercise - 02
write a program that finds the highest square lower than a certain other number
"""

max_num = 500


def highest_square(max_num: str) -> int:
    """Returns the next highest square below the given max_num"""
    ans = None
    for i in range(max_num):
        if i ** 2 > max_num:
            break
        ans = i ** 2
    return ans
