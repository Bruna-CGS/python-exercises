#!/usr/bin/env python3

primeiro_semestre = float(input("Digite a nota final do primeiro semestre: ") .replace(',' , '.'))
segundo_semestre = float(input("Digite a nota final do segundo semestre: ") . replace( ',' , '.'))

media_das_notas =( primeiro_semestre + segundo_semestre) / 2

if media_das_notas >= 8:
	print(f"Prabéns, você foi APROVADO com média de {media_das_notas}")
elif media_das_notas > 6 and media_das_notas < 8:
	print(f"Quase lá, você precisará de RECUPERAÇÃO, sua média foi de {media_das_notas}")
else:
	print(f"Que pena, você foi REPROVADO, sua média foi de {media_das_notas}")	