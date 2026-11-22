def is_letter(chra):
    return 'a' <= chra <= 'z' or 'A' <= chra <= 'Z'

def is_isogram(phrase):
    letters = [0]*26
    for chr in phrase:
        if not is_letter(chr):
            continue
        letters[ord(chr.upper()) - ord('A')] += 1
    for chr in letters:
        if chr > 1:
            return False
    return True
