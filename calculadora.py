#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
if len(sys.argv) != 4:
	print
	print "Argumentos inválidos"
else:
	try:
		if sys.argv[1] == '+':
        		Resultado = float(sys.argv[2]) + float(sys.argv[3])
       	 	elif sys.argv[1] == '-':
        		Resultado = float(sys.argv[2]) - float(sys.argv[3])
      		elif sys.argv[1] == 'mul':
      		  	Resultado = float(sys.argv[2]) * float(sys.argv[3])
       		elif sys.argv[1] == '/':
        		Resultado = float(sys.argv[2]) / float(sys.argv[3])
       		print "El resultado es:",Resultado

	except NameError:
		print "Solo hago sumas,restas multi y divisiones"
	except ZeroDivisionError:
		print "Cuidado!! División por cero!"
