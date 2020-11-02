# calculater function

def add(a, b):
    print('\nAdditon resutl: ', a + b)

# subtract funciton
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


class Calculater:
    
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    # calculater: fucntion definetion
    def add(self):
        return self.num1 + self.num2
        # pass

    # subtract funciton
    def sub(self):
        return self.num1 + self.num2
        # pass

    def mul(self):
        return self.num1 + self.num2
        # pass