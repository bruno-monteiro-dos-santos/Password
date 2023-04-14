print('''Conditions à respecter pour créer votre mot de passe :
● Il doit contenir au moins 8 caractères.
● Il doit contenir au moins une lettre majuscule.
● Il doit contenir au moins une lettre minuscule.
● Il doit contenir au moins un chiffre.
● Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
''')

id = input ('Identifiant :')
mdp = input ("Créer un nouveau mot de passe : " )
SpecialSym = ['!','@','#','$','%','^','&','*']
def test (mdp) :
 val = True
#Notre mot de passe doit contenir au moins 8 caractère, sinon on note un message qui nous dit qu'il est trop court.  
if not len (mdp) > 8 :
    print ("Votre mot de Passe est trop Court !" )
    val = False

if not any (char in SpecialSym for char in mdp):
    print ("Un symbole au moins")
    val = False

    
if sum(1 for c in mdp if c.isalpha()) :
    alpha_present = True
else:
    print ("Une minuscule au moins")
     
if sum(1 for c in mdp if c.isupper()) :
    maj_presente = True
else:
    print ("Une majuscule au moins")

if sum(1 for c in mdp if c.isdigit()) :
    digit_present = True
else:
    print ("Un chiffre au moins")
      
#Fonction principale

mdp = input ("Entrez le mot de passe : " )
    
while test(mdp)==False :
 print ("Erreur dans le mot de passe" )
 mdp = input ("entrez un nouveau mot de passe : " )
    
#Si toutes les conditions sont bonnes :
else :
 mdp2 = input ("Répetez le mot de passe : " )
 while mdp != mdp2 : 
  print ("mot de passe incorrect" ) 
  mdp2 = input ("mot de passe non identique réesseyer : " )
 else :
  print ('''Mot de passe correct. 
Bienvenue!!! ''' )

import hashlib

#La chaine de caractères à hasher
string_to_hash = mdp

#création d'un object hash SHA-256
hash_object = hashlib.sha256()

#Mise à jour de l'object hash avec la chaine de caractères à hasher
hash_object.update(string_to_hash.encode())

#Récupération du hash en hexadécimal
hex_hash = hash_object.hexdigest()

print(f"Hash de la chaine '{string_to_hash}' : {hex_hash}")


