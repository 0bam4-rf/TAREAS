# //Un estacionamiento requiere determinar el cobro 
# 	//que debe aplicar a las personas que lo utilizan. 
# 	//Considere que el cobro es con base en las horas 
# 	//que lo disponen y que las fracciones de hora se 
# 	//toman como completas. realice el
# 	//pseudocódigo que representen el algoritmo
# 	//que permita determinar el cobro.


horas = float(input ("ingrese las horas que paso en el estacionamiento: "))

horaCompleta = int(horas) +1 if horas % 1 != 0 else int (horas)
valor = 1000
pag = (valor) * (horaCompleta)
print("su valor a pagar es: ${pag}")
