vowel = ['a', 'e', 'i', 'o', 'u']

def translate(string):
    words = string.split()
    result = ""
    for text in words:
        if text.startswith(tuple(vowel) + ('xr', 'yt')):
            pass
        elif (pos := text.find("qu")) != -1 and not any(i in text[:pos] for i in vowel + ['y']):
            text = text[pos+2:] + text[:pos+2]
        elif (pos := text.find("y")) != -1 and not any(i in text[:pos] for i in vowel + ['qu']):
            text = text[pos + bool(pos == 0):] + text[:pos + (pos == 0)]
        else:
            pos = min((temp for i in vowel if (temp := text.find(i)) != -1), default=0)
            text = text[pos:] + text[:pos]
        text += 'ay'
        result += text + ' '
    result = result[:-1]
    return result