glosnosc = 57
if glosnosc <20:
	print("Prawie nic nie słychać.")
elif 20 <=glosnosc <40:
	print ("O,muzyk leci w tle.")
elif 40<= glosnosc <60:
	print("Idealnie,mogę usłyszeć detale.")
elif 60 <= glosnosc <100:
	print("Troszkę za głośno!")
else:
	print("Ojoj! Moje uszy!:(")
def hej(imie):
	if imie=='Ola':
		print('Hej Ola!')
	elif imie=='Sonja':
		print('Hej Sonja')
	else:
		print('Hej nieznajoma!')
hej("Ola")
