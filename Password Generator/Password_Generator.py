#Password_Generator
#It's just the implementation of the algorithms of generation of complex passwords
#Which you might have seen many times suggested by Chrome
#It has been done using OOPS concept as well

import random

class Password_Generator:
    #__init__() function
    def __init__(self,length=16): # Classic __init__() function
        self.max_length=length
        #The Length of the Random Password Suggested by Chrome is 15
        #We are taking here 16 for Convinience
        self.numbers=[chr(i) for i in range(48,58)]
        #Digits that will be used in the password
        self.Lower_case_alpha=[chr(i) for i in range(97,123)]
        #Lower Case Alphabets to be used in the creation of password
        self.Upper_case_alpha=[chr(i) for i in range(65,91)]
        #Upper Case Alphabets to be used in the creation of password
        self.Special_Characters=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
        #Special Characters
        #Very useful in the creation of a strong password
        #As it makes it diffcult to guess
        self.total=self.numbers+self.Lower_case_alpha+self.Upper_case_alpha+self.Special_Characters
        
    #Member Function #1
    def randomizee(self):
        #function to randomly choose 1 elements from each of the four category
        random_numbers=random.choice(self.numbers)
        #Random from Digits
        random_Lower_case=random.choice(self.Lower_case_alpha)
        #Random from Lower Case Alphabets
        random_Upper_case=random.choice(self.Upper_case_alpha)
        #Random from Higher Case Alphabets
        random_Special=random.choice(self.Special_Characters)
        #Random from Special Characters
        
        rand_tot=random_numbers+random_Lower_case+random_Upper_case+random_Special
        return rand_tot
    
    #Member Function #2
    def work(self):
        rand_tot=self.randomizee()
        #now that we are sure we have at least one character from each
        #set of characters, we fill the rest of
        #the password length by selecting randomly from the combined
        #list of character above.
        for i in range(self.max_length-4):
            rand_tot=rand_tot+random.choice(self.total)
            password=list(rand_tot)
            random.shuffle(password)
        return password
    
    #Member Function #3
    def generate(self):
        password=self.work()
        return "".join(password)
    
if __name__=="__main__":
    p=Password_Generator(16)
    print(p.generate())