class calculator:
    
    def __init__(self):
        Number1=int(input("Enter the first Operend:-"))
        Number2=int(input("Enter the Second Operend:-"))
        self.Number1=Number1
        self.Number2=Number2
        print("""              1.ADDITION
              2.SUBTRACTION
              3.MULTIPLICATION
              4.DIVISION
              5.MODULUS
              6.FLOORDIVISION
              7.EXIT """)
        choice=int(input("Enter Your choice:"))
        if choice==1:
            self.addition()
        elif choice==2:
            self.subtraction()
        elif choice==3:
            self.multipication()
        elif choice==4:
            self.division()
        elif choice==5:
            self.modulus()
        elif choice==6:
            self.floordivision()
        elif choice==7:
            return
        else:
            print("your enter wrong operator TRY AGAIN")
            om=calculator()
            
    def printer(self,values):
        print(f"The Number of {self.Number1}and {self.Number2} value is:-{values}")

    def addition(self):
        self.printer(self.Number1+self.Number2)

    def subtraction(self):
        self.printer(self.Number1-self.Number2)

    def multipication(self):
        self.printer(self.Number1*self.Number2)
        
    def division(self):
        try:
           self.printer(self.Number1/self.Number2)
        except ZeroDivisionError:
            print(f"The second operend should not ZERO,TRY ONCE AGAIN")
            om=calculator()

    def modulus(self):
        self.printer(self.Number1%self.Number2)

    def floordivision(self):
        try:
            self.printer(self.Number1//self.Number2)
        except ZeroDivisionError:
            print(f"The second operend should not ZERO ,TRY ONCE AGAIN")
            om=calculator()

om=calculator()
