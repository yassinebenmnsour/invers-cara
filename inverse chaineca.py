#programme qui demande à l’utilisateur de saisir un mot et de lui renvoyer son inverse exemple yassine >> enissay
#yassine benmansour
#1er solution

a = input("Tapez une chaine a : ")

b = a[::-1]

print("L'inverse de la chaine : '",a,"' est : ", b)

#2eme solution
'''      
         
a = input("Tapez une chaine a : ")

inv = ""

for x in a:
    inv = x + inv
print("L'inverse de la chaine : '",a,"' est : ", inv)


'''