# Local scope
# myfun ke liey ye a ek gloabl varaibel
# a = 10

def myfun():
    # use gloabl keyword to make a as gloabl varaibal
    global a
    a = 20
    print('\nIn fun a: ', a)

myfun()
print('\na: ', a)