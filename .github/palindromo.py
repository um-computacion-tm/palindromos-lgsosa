def palindrome(palabra):
    palabra = palabra.lower().replace(" ", "")
    palindromo = palabra[::-1]

    if palindromo == palabra:
        return True
    else:
        return False

def palindrome_1(palabra):
    palabra = palabra.lower().replace(" ","")
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return palindrome(palabra[1:-1])
    else:
        return False