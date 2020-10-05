# Tic Tac Toe
# debutant
cells = '_________'
FIN = False
cells = cells.replace('_', ' ')
bo = [list(cells[6:9]), list(cells[3:6]), list(cells[:3])]
print('---------')
print('| ' + bo[2][0] + ' ' + bo[2][1] + ' ' + bo[2][2] + ' |')
print('| ' + bo[1][0] + ' ' + bo[1][1] + ' ' + bo[1][2] + ' |')
print('| ' + bo[0][0] + ' ' + bo[0][1] + ' ' + bo[0][2] + ' |')
print('---------')
nbc = 1
jo = 'X'
while not FIN:
    # recherche de victoire
    v = {'X': False, 'O': False}
    for j in ['X', 'O']:
        ali = [j, j, j]
        if bo[0] == ali or bo[1] == ali or bo[2] == ali \
                or [bo[0][0], bo[1][0], bo[2][0]] == ali \
                or [bo[0][1], bo[1][1], bo[2][1]] == ali \
                or [bo[0][2], bo[1][2], bo[2][2]] == ali \
                or [bo[0][0], bo[1][1], bo[2][2]] == ali \
                or [bo[0][2], bo[1][1], bo[2][0]] == ali:
            v[j] = True
    if v['X'] is True and v['O'] is True:
        print('Impossible')
        FIN = True
    elif v['X'] is True and v['O'] is False:
        print('X wins')
        FIN = True
    elif v['X'] is False and v['O'] is True:
        print('O wins')
        FIN = True
    elif v['X'] is False and v['O'] is False:

        if nbc == 10:  # plus d'emplacements vides
            print('Draw')
            FIN = True
        else:
            #  'Game not finished')
            mov = False
            while mov is not True:
                saisie = input('Enter the coordinates:')
                if ' ' in saisie:
                    X, Y = saisie.split(' ')
                else:
                    print('You should enter 2 numbers!')
                    continue
                if X.isdigit() and Y.isdigit():
                    x = int(X)
                    y = int(Y)
                    if x not in (1, 2, 3) or y not in (1, 2, 3):
                        print('Coordinates should be from 1 to 3!')
                    else:  # coord ok
                        if bo[y - 1][x - 1] != ' ':
                            print('This cell is occupied! Choose another one!')
                        else:
                            mov = True
                            bo[y - 1][x - 1] = jo
                            print ("nbc", nbc)
                            nbc += 1
                            if jo == 'X':
                                jo = 'O'
                            else:
                                jo = 'X'
                else:
                    print('You should enter numbers!')
            print('---------')
            print('| ' + bo[2][0] + ' ' + bo[2][1] + ' ' + bo[2][2] + ' |')
            print('| ' + bo[1][0] + ' ' + bo[1][1] + ' ' + bo[1][2] + ' |')
            print('| ' + bo[0][0] + ' ' + bo[0][1] + ' ' + bo[0][2] + ' |')
            print('---------')
