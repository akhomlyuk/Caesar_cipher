from colorama import init, Fore, Style
from cipher_functions import decrypt, encrypt

init(autoreset=True)

user_choice = input(
    f'{Fore.MAGENTA}B(b){Fore.GREEN} bruteforce, {Fore.BLUE}D(d){Fore.GREEN} decrypt or {Fore.RED}E(e){Fore.GREEN} encrypt: ')

if user_choice == 'D' or user_choice == 'd':
    ciphered_string = input(Fore.CYAN + 'Text for decryption: ')
    n = int(input(Fore.CYAN + 'Shift(any positive or negative integer): '))
    print(f'{Fore.BLUE}Decrypted text: {Fore.GREEN}{decrypt(ciphered_string, n)[0]}')
    with open('decrypted.txt', 'w', encoding='UTF-8') as file:
        file.writelines(decrypt(ciphered_string, n)[0])
    print(f'Text saved to: decrypted.txt')
elif user_choice == 'E' or user_choice == 'e':
    string_for_encrypt = input(Fore.CYAN + 'Text for encryption: ')
    n = int(input(Fore.CYAN + 'Shift(any positive or negative integer): '))
    print(f'{Fore.RED}Encrypted text: {Fore.GREEN}{encrypt(string_for_encrypt, n)}')
    with open('encrypted.txt', 'w', encoding='UTF-8') as file:
        file.writelines(encrypt(string_for_encrypt, n))
    print(f'Text saved to: encrypted.txt')
elif user_choice == 'B' or user_choice == 'b':
    ciphered_string = input(Fore.CYAN + 'Text for decryption: ')
    if decrypt(ciphered_string, 1)[1] > decrypt(ciphered_string, 1)[2]:
        for i in range(1, 33):
            ls = ['ROT key ' + str(i) + ': ' + decrypt(ciphered_string, i)[0] + '\n' for i in range(1, 33)]
            with open('bruted.txt', 'w', encoding='UTF-8') as file:
                file.writelines(ls)
            print(f'{Fore.CYAN}ROT key {Fore.GREEN}{i}: {Style.RESET_ALL}{Style.BRIGHT}{decrypt(ciphered_string, i)[0]}')
        print(f'Text saved to: bruted.txt')
    else:
        for i in range(1, 27):
            ls = ['ROT key ' + str(i) + ': ' + decrypt(ciphered_string, i)[0] + '\n' for i in range(1, 27)]
            with open('bruted.txt', 'w', encoding='UTF-8') as file:
                file.writelines(ls)
            print(f'{Fore.CYAN}ROT key {Fore.GREEN}{i}: {Style.RESET_ALL}{Style.BRIGHT}{decrypt(ciphered_string, i)[0]}')
        print(f'Text saved to: bruted.txt')
