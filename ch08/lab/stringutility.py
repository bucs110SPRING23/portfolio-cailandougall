class StringUtility:
    def __init__ (self, string):
        """
        Takes the string as a parameter and stores it as an instance variable
        args: self.string (str)
        """
        self.string=string
    def __str__ (self):
        """
        Returns the original string, unchanged
        return: self.string (str)
        """
        return self.string
    def vowels (self):
        """
        Counts the number of vowels in the string and returns the result as a string.
        args: self.string (str)
        return: count (str), "many" (str)
        """
        count=0
        for char in self.string:
            if char in ("aeiouAEIOU"):
                count+=1
        if count<5:
            return str(count)
        if count >=5:
            return str("many")
    def bothEnds (self):
        """
        Returns a string made of the first 2 and last 2 characters of the original string. 
        However, if the string length is less than or equal to 2, returns an empty string instead.
        args: self.string(str)
        return: bothends (str), '' (str)
        """
        if len(self.string)>2:
            bothends=self.string[0]+self.string[1]+self.string[-2]+self.string[-1]
            return bothends
        else:
            return ''
    def fixStart (self):
        """
        Returns a string where all occurrences of the first character have been changed to '*', except the first char itself isn't changed.
        args: self.string (str)
        return: star+rest (str)
        """
        if len(self.string)<=1:
            return self.string
        else:
            star = self.string[0]
            rest = self.string[1:]
            rest = rest.replace(star,'*')
            return star+rest
    def asciiSum (self):
        """
        Returns an int that contains the sum of all ascii values in the string.
        args: self.string (str)
        return: sum (int)
        """
        sum=0
        for char in (self.string):
            sum+=ord(char)
        return sum
    def cipher (self):
        """
        This function is going to encrypt the various strings using Caesar cipher technique according to the length of the string
        args: the strings (str)
        shift: the length of the strings (int)
        return: the encrypted message (str)
        """
        text=self.string
        shift=len(self.string)
        result=""
        for char in text:
            if char.isalpha():
                start=ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + shift) % 26
                char = chr(start + new_pos)
            result+=char
        return result