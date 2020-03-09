class A:

    # def __init__(self):
    #     print("xxx")

    def __getA(self):
        # return self._a
        pass

    def _getA(self):
        return 1000

    def xxx(self):
        self.__getA()

class B(A):
    def __init__(self, a, b):
        super().__init__()
        self.x = a
        self.y = b
        # super().__init__(a, b)

    def __getA(self):
        return 1000

    def _getA(self):
        return 1000

    def xxx(self):
        return self.__getA()

x = B(1,4)
x.xxx()
print(x._a)
print(x.b)