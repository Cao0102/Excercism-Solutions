norok = '0123456789-'
chkok = '0123456789X'

def is_valid(isbn):
    if not isbn or any(char not in norok for char in isbn[:-1]) or isbn[-1] not in chkok:
        return False
    arr = [10 if num == 'X' else int(num) for num in isbn if num != '-']
    if len(arr) != 10:
        return False
    arr = [0] + arr[::-1]
    return not sum(arr[i]*i for i in range(11)) % 11