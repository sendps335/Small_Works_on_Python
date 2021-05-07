class AddOne:
    def __init__(self,x):
        self.x=x
        
    def two_complement_addition(self):
        return (-(~self.x))
    
    def flip_bits(self):
        m=1
        while(self.x!=0 and m!=0):
            self.x=self.x^m
            m<<=1
        self.x=self.x^m
        return self.x
    
if __name__=="__main__":
    ob=AddOne(99)
    print(ob.two_complement_addition())
    print(ob.flip_bits())
    