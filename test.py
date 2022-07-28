import xprint as xprint
@xprint.xprint(
    print_level=xprint.INFO,
    level=xprint.DEBUG
)
def test():
    print(111)

@xprint.xprint(
    print_level=xprint.DEBUG,
    level=xprint.INFO
)
def test1():
    print(111)
    test()


test1()
