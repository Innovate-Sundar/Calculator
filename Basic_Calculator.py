#Do a program to calculate add mul div modulo using overriding

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        return self.a+self.b
class Subtraction(Addition):
    def calculate(self):
        return self.a-self.b
class Multiplication(Subtraction):
    def calculate(self):
        return self.a*self.b
class Division(Multiplication):
    def calculate(self):
        return self.a/self.b
class Modulo(Division):
    def calculate(self):
        return self.a%self.b
while True:
    a=int(input('Enter a First Number:'))
    b=int(input('Enter a Second Number:'))
    print('Please select the following operation:\n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Mod')
    choices=str(input('Enter your Choice:'))
    if choices=='Add':
        Add=Addition(a,b)
        print('Answer is:',Add.calculate())
        break
    elif choices=='Sub':
        Sub=Subtraction(a,b)
        print('Answer is:',Sub.calculate())
        break
    elif choices=='Mul':
        Mul=Multiplication(a,b)
        print('Answer is:',Mul.calculate())
        break
    elif choices=='Div':
        Div=Division(a,b)
        print('Answer is:',Div.calculate())
        break
    elif choices=='Mod':
        Mod=Modulo(a,b)
        print('Answer is:',Mod.calculate())
        break
    else:
        print('Invalid Input')
        break