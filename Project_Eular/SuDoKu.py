# Enter your code here. Read input from STDIN. Print output to STDOUT
def gen_matrix(match_x,match_y,match_z):
    matrix = [[[] for i in range(9)]for j in range(9)]
    for i in range(9):
        for j in range(9):
            if given[i][j] == '0':
                z = (i/3)*3 + (j/3)
                set_xy = set(match_x[i]).intersection(set(match_y[j]))
                matrix[i][j] = list(set_xy.intersection(set(match_z[z])))
    return matrix
def accepted(given):
    actual = ['1','2','3','4','5','6','7','8','9']
    match_x = []
    match_y = []
    match_z = []
    given_z = [[] for i in range(9)]
    given_y = [[] for i in range(9)]
    output = given
    for i in range(9):
        for j in range(9):
            block = (i/3)*3 + (j/3)
            given_z[block].append(given[i][j])
            given_y[i].append(given[j][i])
    for i in range(9):
        match_x.append(list(set(actual) - set(given[i])))
        match_y.append(list(set(actual) - set(given_y[i])))
        match_z.append(list(set(actual) - set(given_z[i])))
    matrix = gen_matrix(match_x,match_y,match_z)
    #print matrix
    empty = [[],[],[],[],[],[],[],[],[]]
    while(match_x != empty and match_y != empty and match_z != empty):
        for i in range(9):
            for j in range(9):
                if output[i][j] == '0' and len(matrix[i][j]) == 1:
                    output[i][j] = matrix[i][j][0]
                    match_x[i].remove(matrix[i][j][0])
                    match_y[j].remove(matrix[i][j][0])
                    z = (i/3)*3 + (j/3)
                    match_z[z].remove(matrix[i][j][0])
                    matrix = gen_matrix(match_x,match_y,match_z)
    for i in range(9):
        print ''.join(output[i])

given = [list(raw_input()) for i in range(9)]
accepted(given)
