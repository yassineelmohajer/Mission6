def verify(nom):
    l = []
    t = []
    with open(nom, "r") as file:
        fichier = file.readlines()
        
        for ligne in fichier:
            z = ligne.split(",")
            l.append(z)
        
        for i in l:
            r = []
            for c in i:
                r.append(c.rstrip("\n"))
            t.append(r)  # On ajoute r à t après avoir fini d'itérer sur c
            
    return t  # On retourne t pour l'utiliser dans la fonction file

def file(filename):
    t = verify(filename)  # On récupère t ici
    
    for i in t:
        
        for c in range (len(i)):
            
            if type(i[c])==str and i[-1] in "1234567890":  # Vérifie si c est une chaîne et si c est un chiffre
                v = "open file"
            else:
                v = "please take a good file"
                break  # On quitte la boucle si on trouve un problème
        
    return v




def info(filename):
    count = 0
    recount = 0
    with open(filename, "r") as file:
        data = file.readlines()
        for line in data:
            count += 1  # Compter le nombre de lignes
            recount += len(line)  # Compter le nombre de caractères dans chaque ligne
                
    print(count)  # Affiche le nombre de lignes
    print(recount)  # Affiche le nombre de caractères
            
def words(filename):
    r=[]
    with open(filename,"r") as file:
        fichier = file.readlines()
        for ligne in fichier :
            r.append(ligne)
    print("Read file as list of words")
def chearch(mot,filename):
    with open(filename,"r") as file:
        fichier=file.readlines()
        for i in fichier:
            if str(mot) in i:
                c=(str(mot)+" is in the list of words")
                break
            else:
                c=(str(mot)+" is not in the list of words")
        print(c)


def sum(filename):
    l=[]
    su=0
    with open(filename,"r") as file:
        fichier=file.readlines()
    for i in range( len(fichier)):
        y=""
        for c in fichier[i]:
            if c in "1234567890":
                
                y+=c
            
        l.append(int(y))
        
    for i in l:
       su+=i
    print(su)

def avg(filename):
    
    l=[]
    su=0
    with open(filename,"r") as file:
        fichier=file.readlines()
    for i in range( len(fichier)):
        y=""
        for c in fichier[i]:
            if c in "1234567890":
                
                y+=c
            
        l.append(int(y))
        
    for i in l:
       su+=i

    print(su/len(fichier))

command=""
x=input("choisi")
l=x.split()
print(l)



    





    
