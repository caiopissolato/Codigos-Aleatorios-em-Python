class Data:
    def __init__(self, d, m ,a):
        self.d = d
        self.m = m
        self.a = a

    def formatada(self):
        print("{}/{}/{}".format(self.d, self.m, self.a))