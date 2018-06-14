class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

def main():
	x = OnlyOne('Lucy Wang')
	print(x)
	y = OnlyOne('Patrick Wang')
	print(y)
	z = OnlyOne('Kang Wang')
	
	print(z)
	print(x)
	print(y)



if __name__ == '__main__':
    main()