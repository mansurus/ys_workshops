from collections import Counter

def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())
