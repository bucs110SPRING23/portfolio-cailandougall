import json
def decipher(text):
    """
    This function is going to decrypt the text in thre encrypted-#B... file using the decipher technique
    args: 
        text: the text in the encrypted-#B... file (str)
        shift: i
    return: the decrypted message (str)
    """
    result=""
    for i in range (0,27):
        sentence=str("The quick brown fox jumps over the lazy dog")
        for char in text:
            if char.isalpha():
                start=ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + i) % 26
                char = chr(start - new_pos)
            result+=char
            if sentence==result:
                break
            return result
def main():
    fptr = open("ch07/exercises/encrypted-#B00970858.txt", "r")
    result=decipher(fptr)
    fptr=open("ch07/exercises/decrypted.txt", "w")
    fptr.write(result)
    fptr.close()
main()