#usr/bin/env python3
def even(array):

	array_1 = [] 
	count = 0
	for  i in array:
		count = 0
		
		for j in i:
			if '1' in j:
				count = count + 1
		if (count % 2 == 0):
			array_1.append("0"+i)
		else:
			array_1.append("1"+i)
	return array_1
	
chiffre = int(input("Entrez un chiffre svp: ")) 

new_chiffre = "{0:b}".format(chiffre)
print("Le binaire = ", new_chiffre)

array = [new_chiffre]
print("Le resultat = ", even(array))

