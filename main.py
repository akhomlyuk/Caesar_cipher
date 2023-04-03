from colorama import init, Fore

init(autoreset=True)
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


user_choice = input(Fore.BLUE + 'D(d) ' + Fore.GREEN + 'for decrypt or ' + Fore.RED + 'E(e) ' + Fore.GREEN + 'for encrypt: ')
if user_choice == 'D' or user_choice == 'd':
    s = input(Fore.BLUE + 'Message for decryption: ')
    n = int(input(Fore.BLUE + 'Shift(any positive or negative integer): '))
    print(decrypt(s, n))
elif user_choice == 'E' or user_choice == 'e':
    s = input(Fore.RED + 'Message for encryption: ')
    n = int(input(Fore.RED + 'Shift(any positive or negative integer): '))
    print(f'{Fore.GREEN}Encrypted text: {encrypt(s, n)}')
