def isDominate(m, n):
    # The function receives a matrix and matrix size
    # and checks whether the matrix has a dominant diagonal

    # for each row
    for i in range(0, n):

        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])

            # removing the
        # diagonal element.
        sum = sum - abs(m[i][i])

        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if abs(m[i][i]) < sum:
            return False

    return True


def jacobiMethod(A, n, b):
    # The function gets a matrix, matrix size and vector b.
    # It is tested whether the matrix has a dominant diagonal.
    # If so, a solution is obtained using the Jacobi method
    # Otherwise, the program ends in an orderly fashion.

    # Stop condition
    e = 0.001
    iteration = 1

    if not isDominate(A, n):
        print("The matrix is not Dominant, Bye Bye!")
        exit(1)
    else:
        print("The matrix is not Dominant, you can continue...")

    # Defining equations to be solved in diagonally dominant form
    f1 = lambda x, y, z: (b[0] - (A[0][1] * y) - (A[0][2] * z)) / A[0][0]
    f2 = lambda x, y, z: (b[1] - (A[1][0] * x) - (A[1][2] * z)) / A[1][1]
    f3 = lambda x, y, z: (b[2] - (A[2][0] * x) - (A[2][1] * y)) / A[2][2]

    x0 = int(input("Please select a guess for x0:"))
    y0 = int(input("Please select a guess for y0:"))
    z0 = int(input("Please select a guess for z0:"))

    print('\niteration\tx\ty\tz\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)

        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (iteration, x1, y1, z1))

        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        x0 = x1
        y0 = y1
        z0 = z1

        iteration += 1

        condition = e1 > e and e2 > e and e3 > e

    print('\nSolution: x=%0.3f, y=%0.3f, z = %0.3f\n' % (x1, y1, z1))


def gaussSeidelMethod(A, n, b):
    # The function gets a matrix, matrix size and vector b.
    # It is tested whether the matrix has a dominant diagonal.
    # If so, a solution is obtained using the Gauss-Seidel method
    # Otherwise, the program ends in an orderly fashion.

    # Stop condition
    e = 0.001
    iteration = 1

    if not isDominate(A, n):
        print("The matrix is not Dominant, Bye Bye!")
        exit(1)
    else:
        print("The matrix is not Dominant, you can continue...")

    # Defining equations to be solved in diagonally dominant form
    f1 = lambda x, y, z: (b[0] - (A[0][1] * y) - (A[0][2] * z)) / A[0][0]
    f2 = lambda x, y, z: (b[1] - (A[1][0] * x) - (A[1][2] * z)) / A[1][1]
    f3 = lambda x, y, z: (b[2] - (A[2][0] * x) - (A[2][1] * y)) / A[2][2]

    x0 = int(input("Please select a guess for x0:"))
    y0 = int(input("Please select a guess for y0:"))
    z0 = int(input("Please select a guess for z0:"))

    print('\niteration\tx\ty\tz\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)

        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (iteration, x1, y1, z1))

        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        x0 = x1
        y0 = y1
        z0 = z1

        iteration += 1

        condition = e1 > e and e2 > e and e3 > e

    print('\nSolution: x=%0.3f, y=%0.3f, z = %0.3f\n' % (x1, y1, z1))


if __name__ == "__main__":
    # Driver Code
    n = 3
    A = []
    b = []

    print("Please enter the matrix values: (a11, a12, ... , a33)")

    for i in range(n):
        row = []
        for j in range(n):
            num = int(input(f"a{i + 1},{j + 1} = "))
            row.append(num)
        A.append(row)

    print("Please enter the values of vector b: (b1, b2, b3)")

    for i in range(n):
        num = int(input(f"b{i + 1} = "))
        b.append(num)

    menu_loop = True

    while menu_loop:
        print("Please choose which method you would like the solution:")
        print("1. Jacobi method.")
        print("2. Gauss - Seidel method.")
        print("3. Exit.")
        choice = int(input())

        if choice == 1:
            jacobiMethod(A, n, b)
        elif choice == 2:
            gaussSeidelMethod(A, n, b)
        elif choice == 3:
            print("Thank you!")
            exit(1)
        else:
            print("Wrong choose, please try again!")
