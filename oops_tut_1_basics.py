class OppsTut1:
    # def printhello(self):
    #     print("Hello World")

    values = 120
    def hello(self):
        # global and local
        system = [1, 2, 3, 4, 5]
        print(system)

    def __init__(self):
        def bro():
            self.var = "hello bro whats up"
            f = "Bro What's Up!!!"  # its a local variable only for a function.
            # print(self.var)
            print(f)# => print

        var45 = "hello"
        self.hello()

        print(self.values)
        print(var45)
        # print("hello world")
        # bro() 
        # self.print_other("Whats You Doing?")
        # print(self.var)

        # print(f) # local variable doing the error like 'f' is not define.
        # self.print_other("How Are You?")
        # self.print_other("Get Up")

    def print_other(self, whoprint):
        print(whoprint)



obj = OppsTut1()