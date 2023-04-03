```def encrypt(original_string: str, shift_key: int) -> str:
    enc = ''
    for i in original_string:
        if i.isupper() and i.isalpha():
            enc += upper_alp.get(((ord(i) + shift_key - ord('A')) % 26))
        elif i.lower() and i.isalpha():
            enc += lower_alp.get(((ord(i) + shift_key - ord('a')) % 26))
        else:
            enc += i
    return enc