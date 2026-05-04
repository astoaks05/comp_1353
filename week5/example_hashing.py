# W Ram model of computation
# FACT 1: EVERYTHING IS A BITSTRING (everything is a number 0101000101100111)
# FACT 2: We can do math very fast O(1)!!!
# FACT 3: We can direct index an array in constant time O(1)

class names:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        self.ssn = 650374768
    def hash(self):
        return hash(self.ssn)
    
aidans = names('aidan', 'stoaks')
print(hash(aidans))




