def is_char(character):
    return 'a' <= character <= 'z' or 'A' <= character <= 'Z'

def is_pangram(sentence):
    a = [False] * 26
    for i in sentence:
        if not is_char(i):
            continue
        a[ord(i.upper())-ord('A')] = True
    return all(a)
