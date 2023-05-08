import json
def decipher(fptr, shift):
    """
    This function is going to decrypt the text in the encrypted-#B... file using the decipher technique
    args: 
        text: the text in the encrypted-#B... file (str)
        shift: 1
    return: the decrypted message (str)
    """
    result=""
    for char in fptr:
        if char=="W":
            result+=" "
        elif char=="1":
            result+="T"
        elif char.isalpha():
            start=ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
            result+=char
    return result
def main():
    text=str("1ifWrvjdlWcspxoWgpyWkvnqtWpwfsWuifWmbazWeph")
    shift=-1
    result=decipher(text, shift)
    fptr=open("ch07/exercises/decrypted.txt", "w")
    fptr.write(result)
    fptr.close()
main()