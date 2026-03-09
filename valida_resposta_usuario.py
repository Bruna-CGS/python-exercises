#!/usr/bin/env python3

resposta = input("Deseja continuar? [S/N]: ").upper()    

while resposta == 'S':
    resposta = input("Deseja continuar? [S/N]: ").upper()
    print("Continua o programa...")
else:
    print('Programa encerrado')
  