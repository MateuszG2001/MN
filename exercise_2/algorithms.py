def gauss_elimination(rows_number, tab, epsilon):
    for i in range(rows_number - 1):
        if abs(tab[i][i]) < epsilon:
            for j in range(i + 1, rows_number):
                if abs(tab[j][i]) > epsilon:
                    for k in range(0, rows_number + 1):
                        tmp = tab[i][k]
                        tab[i][k] = tab[j][k]
                        tab[j][k] = tmp
                    break
        if abs(tab[i][i]) > epsilon:
            for j in range(i + 1, rows_number):
                mn = (-1) * (tab[j][i] / tab[i][i])
                for k in range(i + 1, rows_number + 1):
                    tab[j][k] = tab[j][k] + mn * tab[i][k]
    return 1

def calculate(rows_number, X, tab, epsilon):
    for i in range(rows_number - 1, -1, -1):
        if abs(tab[i][i]) < epsilon:
            if tab[i][i + 1] < epsilon:
                print("The system of equations is unmarked")
            else:
                print("The system of equations is contradictory")
            return 0

        sum = tab[i][rows_number]
        for j in range(rows_number - 1, i, -1):
            sum = sum - (tab[i][j] * X[j])

        X[i] = sum / tab[i][i]
    return 1