#Mission 6
def verify(blase):
    file=open(blase,"r")
    t=file.readlines()
    while c is False:
        for i in range(len(t)):
            if type(t[i][1])!=int() and type(t[i][0])!=str():
                c=False
                print("Please enter a real files")
            else:
                c=True
                v =blase
                print("Loaded file")





    if x!="all-words.dat":
        print("This files does not exist!\nPlease enter a good file name")

    else:
        print("Loaded all-words.dat")
        file=open("all-words.dat","r")

def info()             
print("Welcome to your personalized tool!")
x="hello"
while x!="exit":
    x=input()
    
