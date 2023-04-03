upper_alp = {key: chr(value) for key, value in zip(range(26), range(65, 91))}
lower_alp = {key: chr(value) for key, value in zip(range(26), range(97, 123))}


def encrypt(original_string: str, shift_key: int) -> str:
    enc = ''
    for i in original_string:
        if i.isupper() and i.isalpha():
            enc += upper_alp.get(((ord(i) + shift_key - ord('A')) % 26))
        elif i.lower() and i.isalpha():
            enc += lower_alp.get(((ord(i) + shift_key - ord('a')) % 26))
        else:
            enc += i
    return enc


def decrypt(encrypted_string: str, shift_key: int) -> str:
    dec = ''
    for i in encrypted_string:
        if i.isupper() and i.isalpha():
            dec += upper_alp.get(((ord(i) - shift_key - ord('A')) % 26))
        elif i.lower() and i.isalpha():
            dec += lower_alp.get(((ord(i) - shift_key - ord('a')) % 26))
        else:
            dec += i
    return dec
