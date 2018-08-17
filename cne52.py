"""
© Copyright 2001-2018, Python Software Foundation.
Algorithm created by Vinícius Antonioli(tonymtk)
License: GNU Public License(https://www.gnu.org/licenses/gpl.txt)
"""
print('----------------------------------------------------------------')
titulo = ('- Algoritmo CNE52')
repositorio = ('https://github.com/tonymtk/cne52-algorithm')
print(titulo)
presenca = float(input('Digite a nota de presença do aluno: '))
atividades = float(input('Digite a nota de atividades do aluno: '))
avaliacoes = float(input('Digite a nota de avaliações do aluno: '))
soma = (presenca + atividades + avaliacoes)
divisao = (soma / 3)
resultado = str(('A nota final do aluno é {:.3}'.format(divisao)))
print(resultado)
print('\n----------------------------------------------------------------')
print('Repositório oficial: {}'.format(repositorio))
print('Algorithm created by Vinícius Antonioli(tonymtk)\nLicense: GNU Public License')