import ChucknorrisAPI
import YomammaAPI
import DeveloperAPI

def caesar_cipher(text, shift):
    """
    This function is going to encrypt a random Chuck Norris response, a random Yo Mamma response and a random Developer response from API websites using the Caesar cipher technique
    args: 
        text: Random Chuck Norris response (str), random Yo Mamma response (str), random Developer response (str)
        shift: 10 (int)
    return: the encrypted message (str)
    """
    result=""
    for char in text:
        if char.isalpha():
            start=ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)
        result+=char
    return result
    
def main():
    cnapi=ChucknorrisAPI.ChucknorrisAPI()
    text=cnapi.get()
    shift=10
    result=caesar_cipher(text, shift)
    fptr=open("encryption.txt", "w")
    fptr.write(result)
    fptr.close()

    ymapi=YomammaAPI.YomammaAPI()
    text=ymapi.get()
    shift=10
    result=caesar_cipher(text, shift)
    fptr=open("encryption2.txt", "w")
    fptr.write(result)
    fptr.close()

    dapi=DeveloperAPI.DeveloperAPI()
    text=dapi.get()
    shift=10
    result=caesar_cipher(text, shift)
    fptr=open("encryption3.txt", "w")
    fptr.write(result)
    fptr.close()

main()