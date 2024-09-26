class greeting:
    def sayhello(self,name=None,add=None):
        if name is not None and add is not None:
            print("Hello"+name+add)
        elif name is not None and add is None:
            print("Hello"+name)
        else:
            print("None")
c1=greeting()
c1.sayhello("python","23")
c1.sayhello("python")
c1.sayhello()

