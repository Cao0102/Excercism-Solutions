char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rotate(text, key):
    res = ""
    for let in text:
        if let not in char:
            res += let
            continue
        base_val = ord('A' if let.isupper() else 'a')
        res += chr((ord(let) - base_val + key) % 26 + base_val)
    return res