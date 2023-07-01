def doublr_decker():
    print('starting the double decker')
    def inner_func():
        print('In inner function')
        return 2
    return inner_func

# print(doublr_decker()())

def do_something(work):
    print('work started')
    # print(work())
    work()
    print('work done')

# do_something('Imma bz')

def coding():
    print('Coding in python')

# do_something(coding)
def sleeping():
    print('sleeping and dreaming')

do_something(sleeping)
