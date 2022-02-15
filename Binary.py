import math
import colorama
from os import system
from colorama import Fore, Style, init

BINARY_CODE_DICT = {
    'A': '1000001',     'N': '1001110',     'a': '1100001',     'n': '1101110',     '0': '110000',
    'B': '1000010',     'O': '1001111',     'b': '1100010',     'o': '1101111',     '1': '110001',
    'C': '1000011',     'P': '1010000',     'c': '1100011',     'p': '1110000',     '2': '110010',
    'D': '1000100',     'Q': '1010001',     'd': '1100100',     'q': '1110001',     '3': '110011',
    'E': '1000101',     'R': '1010010',     'e': '1100101',     'r': '1110010',     '4': '110100',
    'F': '1000110',     'S': '1010011',     'f': '1100110',     's': '1110011',     '5': '110101',
    'G': '1000111',     'T': '1010100',     'g': '1100111',     't': '1110100',     '6': '110110',
    'H': '1001000',     'U': '1010101',     'h': '1101000',     'u': '1110101',     '7': '110111',
    'I': '1001001',     'V': '1010110',     'i': '1101001',     'v': '1110110',     '8': '111000',
    'J': '1001010',     'W': '1010111',     'j': '1101010',     'w': '1110111',     '9': '111001',
    'K': '1001011',     'X': '1011000',     'k': '1101011',     'x': '1111000',     ' ': '100000',
    'L': '1001100',     'Y': '1011001',     'l': '1101100',     'y': '1111001',     '.': '101110',
    'M': '1001101',     'Z': '1011010',     'm': '1101101',     'z': '1111010',     ',': '101100',
    
}
 
################################################## MAIN ##################################################

def main():
    
    system ('cls')
    init()

    print( Fore.CYAN + 
    """
 ________  ___  ________   ________  ________      ___    ___ 
 |\   __  \|\  \|\   ___  \|\   __  \|\   __  \    |\  \  /  /|
 \ \  \|\ /\ \  \ \  \\ \  \ \  \|\  \ \  \|\  \   \ \  \/  / /
  \ \   __  \ \  \ \  \\ \  \ \   __  \ \   _  _\   \ \    / / 
   \ \  \|\  \ \  \ \  \\ \  \ \  \ \  \ \  \\  \|   \/  /  /  
    \ \_______\ \__\ \__\\ \__\ \__\ \__\ \__\\ _\ __/  / /    
     \|_______|\|__|\|__| \|__|\|__|\|__|\|__|\|__|\___/ /     
                                                  \|___|/      
    
    """
    )

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + 'Text to Binary code\n' +
        Fore.RED + ' [2] ' + Fore.WHITE + 'Binary code to Text'
    )
    
    main_input = input(Fore.GREEN + " >> ")
    
    if main_input == '1':
        TexttoBinary()
    elif main_input == '2':
        BinarytoText()
    else:
        pass

################################################## TEXT to BINARY ##################################################

def TexttoBinary():
    
    system('cls')
    
    print()
    
    text = input(Fore.RED + " [TEXT] " + Fore.LIGHTYELLOW_EX)
        
    print()
    
    cipher = ''
    
    for i in text:
        if i != ' ':
            cipher += BINARY_CODE_DICT[i] + ' '
        
        else:
            cipher += ' '
            
    print(Fore.GREEN + " [BINARY] " + Fore.LIGHTCYAN_EX + cipher)
    
    print()
    
    print(Fore.WHITE + " Back to Main ? (y/n) ")
    answer = input(Fore.RED + " >> ")
    if answer == 'y' or answer == 'Y':
        main()
    else:
        pass

################################################## BINARY to TEXT ##################################################

def BinarytoText():
    system('cls')
    
    print()
    
    binary = input(Fore.RED + " [BINARY] " + Fore.LIGHTYELLOW_EX)
        
    print()
    
    binary = binary.split()
    
    asciiString = ""
    
    for i in binary:
        num = int(i, 2)
        asciichar = chr(num)
        asciiString += asciichar
        # asciiString = asciiString + (asciichar + " ")
      
    print(Fore.GREEN + " [TEXT] " + Fore.LIGHTCYAN_EX + asciiString)
    
    print()
    
    print(Fore.WHITE + " Back to Main ? (y/n) ")
    answer = input(Fore.RED + " >> ")
    if answer == 'y' or answer == 'Y':
        main()
    else:
        pass

################################################## BODY ##################################################

main()