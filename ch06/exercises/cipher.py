def caesar_cipher(text, shift):
    """
    This function is going to encrypt the phrase "The quick brown fox jumps over the lazy dog" using the Caesar cipher technique
    args: 
        text: "The quick brown fox jumps over the lazy dog" (str)
        shift: 50 (int)
    return: the encrypted message (str)
    """
    text=str("The quick brown fox jumps over the lazy dog")
    shift=50
    result=""
    for char in text:
        if char.isalpha():
            start=ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        result+=char
    return result
def main():
    text=str("The quick brown fox jumps over the lazy dog")
    shift=50
    result=caesar_cipher(text, shift)
    fptr=open("encrypted.txt", "w")
    fptr.write(result)
    fptr.close()
main()

    
