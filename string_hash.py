def string_hash(s):
    total = 0
    for ch in s:
        total += ord(ch)
    return total