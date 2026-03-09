#!/usr/bin/env python3

email = input("Digite seu e-mail: ")

if "@nomedaempresa.com.br" in email:
	print("Acesso liberado, é um funcionário.")
else:
	print("Acesso negado, não é um funcionário.")
