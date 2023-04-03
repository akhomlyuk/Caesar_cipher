upper_english_alp = {key: chr(value) for key, value in zip(range(26), range(65, 91))}
lower_english_alp = {key: chr(value) for key, value in zip(range(26), range(97, 123))}

upper_russian_alp = {key: chr(value) for key, value in zip(range(32), range(1040, 1072))}
lower_russian_alp = {key: chr(value) for key, value in zip(range(32), range(1072, 1104))}


def encrypt(original_string: str, shift_key: int) -> str:
    enc = ''
    for i in original_string:
        if i.isupper() and i.isalpha() and i in upper_english_alp.values():
            enc += upper_english_alp.get(((ord(i) + shift_key - ord('A')) % 26))
        elif i.lower() and i.isalpha() and i in lower_english_alp.values():
            enc += lower_english_alp.get(((ord(i) + shift_key - ord('a')) % 26))
        elif i.isupper() and i.isalpha() and i in upper_russian_alp.values():
            enc += upper_russian_alp.get(((ord(i) + shift_key - ord('А')) % 32))
        elif i.lower() and i.isalpha() and i in lower_russian_alp.values():
            enc += lower_russian_alp.get(((ord(i) + shift_key - ord('а')) % 32))
        else:
            enc += i
    return enc


def decrypt(encrypted_string: str, shift_key: int) -> tuple[str, int, int]:
    dec = ''
    ru = 0
    en = 0
    for i in encrypted_string:
        if i.isupper() and i.isalpha() and i in upper_english_alp.values():
            dec += upper_english_alp.get(((ord(i) - shift_key - ord('A')) % 26))
            en += 1
        elif i.lower() and i.isalpha() and i in lower_english_alp.values():
            dec += lower_english_alp.get(((ord(i) - shift_key - ord('a')) % 26))
            en += 1
        elif i.isupper() and i.isalpha() and i in upper_russian_alp.values():
            dec += upper_russian_alp.get(((ord(i) - shift_key - ord('А')) % 32))
            ru += 1
        elif i.lower() and i.isalpha() and i in lower_russian_alp.values():
            dec += lower_russian_alp.get(((ord(i) - shift_key - ord('а')) % 32))
            ru += 1
        else:
            dec += i
    return dec, ru, en
