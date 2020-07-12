from tablaAscii import * 


def obtener_clave(val, dic):
	clave = ""
	#(c, v)
	for c, v in dic.items():
		if val == v:
			clave = c
	return clave 

def convertir_binario_a_texto(binario):

	diccionario_ascii = obtener_diccionario()
	valores_del_dic = list(diccionario_ascii.values())
	frase_completa = ""

	binarios = str(binario).split(" ")	
	decimales = []

	for binario in binarios:
		decimales.append(convertir_binario_a_decimal(binario))

	for decimal in decimales:
		if decimal in valores_del_dic:
			frase_completa += obtener_clave(decimal, diccionario_ascii)

	return frase_completa

def convertir_texto_a_binario(texto):
	diccionario_ascii = obtener_diccionario()

	binarios_obtenidos = ""

	for letra in texto:
		if letra in diccionario_ascii:
																	#Diccionario => "Letra" : valor en entero
			binarios_obtenidos += " " + str(convertir_decimal_a_binario(diccionario_ascii[letra]))
	
	return binarios_obtenidos	

def convertir_decimal_a_binario(num):

	resultado_del_resto = ""
	resultado_de_la_division = num
	primer_numero = str(num % 2) #cabeza
 
	numero_completo = ""
	binario = ""

	while resultado_de_la_division > 0:

		resultado_de_la_division = resultado_de_la_division // 2 
		resultado_del_resto += str(resultado_de_la_division % 2) 

	resultado_del_resto = primer_numero + resultado_del_resto

	for i in range(len(resultado_del_resto) - 1):
		numero_completo += resultado_del_resto[i]

	binario = numero_completo[::-1]

	return int(binario)

def convertir_binario_a_decimal(num):
    elevadoPor = len(num) 
    salida = sum([( 2 ** int(elevadoPor := elevadoPor - 1)) * (int(num[i])) for i in range(len(num))])
    
    return salida
