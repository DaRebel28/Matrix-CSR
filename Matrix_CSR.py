# John Burghardt
def toMatrix(values, columnIndices, rowStart) :
    A = []
    for i in range(len(rowStart) - 1) :
        A.append([])
        for j in range(max(columnIndices) + 1) :
            A[i].append(0)
    row = 0
    element = 0
    for i in range(len(columnIndices)) :
        A[row][columnIndices[i]] = values[i]
        element += 1
        if i < len(rowStart) - 1 :
            if element == rowStart[i + 1] - rowStart[i] :
                row += 1
                element = 0
    return A

def toCSR(A) :
    values = []
    columnIndices = []
    rowStart = [0]
    elements = 0
    for i in A :
        for j in range(len(i)) :
            if i[j] != 0 :
                values.append(i[j])
                columnIndices.append(j)
                elements += 1
        rowStart.append(elements)
    return values, columnIndices, rowStart

A_values = [2,3,4,5]
A_columnIndices = [1,0,1,2]
A_rowStart = [0,1,2,4]
print("A values:", A_values)
print("A column indices:", A_columnIndices)
print("A row starts:", A_rowStart)
A = toMatrix(A_values, A_columnIndices, A_rowStart)
print("A = ")
for i in A :
    print(i)
print()
B = [[2,0,0],
     [3,0,0],
     [0,4,5]]
print("B = ")
for i in B :
    print(i)
B_values = toCSR(B)[0]
B_columnIndices = toCSR(B)[1]
B_rowStart = toCSR(B)[2]
print("B values:", B_values)
print("B column indices:", B_columnIndices)
print("B row starts:", B_rowStart)