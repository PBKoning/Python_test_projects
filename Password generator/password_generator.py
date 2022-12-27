# Made by Paul Koning

import secrets
import string

class Password:
    '''
    This class generates a password
    '''    
    @staticmethod
    def generate(length, special_chararacters = True):
        '''
        Method to generate the password.

        length:             integer; indicates how long the password should be
        special_characters: boolean; if True (default) the password wil include special characters

        return value: string; the generated password
        '''    

        CHARACTERS = string.ascii_letters + string.digits
               
        SPECIAL = "!@#$%&*()_?<>[]{}"
        
        password = ""
        characters_string = CHARACTERS
        if special_chararacters:
            characters_string += SPECIAL
        
        for i in range(length):
            password += secrets.choice(characters_string)
                         
        return password


# Example
if __name__ == "__main__":
    print(Password.generate(25))
    print(Password.generate(10, False))