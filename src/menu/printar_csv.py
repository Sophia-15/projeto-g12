

lista_runner = []
dict_runner = {}

file_runner = open("infinity_runner.csv", 'r')

for i in file_runner.readlines():

    lista_runner.append(i)

for j in range(len(lista_runner)):
    lista_runner[j] = lista_runner[j].replace('\n', '')
    lista_runner[j] = lista_runner[j].split(',')

    dict_runner[lista_runner[j][0]] = int(lista_runner[j][1])
file_runner.close()

cont = 0
print('===============================================')
print('\rRUNNER HIGH SCORES')
for i in sorted(dict_runner, key = dict_runner.get, reverse=True):
    cont += 1
    if cont <= 10:
        print(i, dict_runner[i])
    else:
        break



lista_tetris = []
dict_tetris = {}

file_tetris = open("tetris.csv", 'r')

for i in file_tetris.readlines():

    lista_tetris.append(i)

for j in range(len(lista_tetris)):
    lista_tetris[j] = lista_tetris[j].replace('\n', '')
    lista_tetris[j] = lista_tetris[j].split(',')

    dict_tetris[lista_tetris[j][0]] = int(lista_tetris[j][1])
file_tetris.close()

cont = 0
print('===============================================')
print('\tTETRIS HIGH SCORES')
for i in sorted(dict_tetris, key = dict_tetris.get, reverse=True):
    cont += 1
    if cont <= 10:
        print(i, dict_tetris[i])
    else:
        break
