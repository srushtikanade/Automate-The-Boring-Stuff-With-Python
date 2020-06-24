mytableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(tableData):
    colWidths = [0] * len(tableData)
    count=0
    while count < len(tableData):
        for item in tableData[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1
    for col in range(len(tableData[0])):
        for row in range(len(tableData)):
            print(tableData[row][col].rjust(colWidths[row]),end=' ')
        print()
    
        
tablePrinter(mytableData)
    
