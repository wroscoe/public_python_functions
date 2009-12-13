
def csv_rows_to_arrs(csvFile, vars={}):
    arrRows = list(str.splitlines(csvFile))
    for i in range(len(arrRows)):
        arrRows[i] = str.split(arrRows[i], ',')
    return arrRows

def get_list_first_row(arr, vars={}):
    return arr.pop(0)

def get_col(csvFile, intColIndex=0, remove=False): 
    col = []
    for rowIndex in range(len(csvFile)):
        if remove is False:
            col.append(csvFile[rowIndex][intColIndex])
        else:
            col.append(csvFile[rowIndex].pop(intColIndex))
    return col

    #make the contents of all lists numeric

def fail(file):
    eval('wrong syntax')


def splitCol (csvFile, colIndex=0):
    col = getCol(csvFile, vars['colIndex'], remove = True)
    data = []
    for i in range(len(csvFile)):
        data.append([csvFile[i], [col[i]]])
    return data

#input: list or array
#output: numeric list or array 
def makeNumeric(someArray): 
    for i in range(len(someArray)):
        if isinstance(someArray, list):
            someArray[i] = makeNumeric(someArray[i])
        else:
            try:
                return int(someArray)
            except:
                try:
                    return float(someArray)
                except:
                    return someArray
    return someArray



#an attempt at creating an auto associative network. THe NN did not learn.
def makeTrainingData(csvFile):
    trainingData = []
    for y in range(len(csvFile)):
        inData = csvFile[y][:]
        for x in range(len(csvFile[y])):
            inData = csvFile[y][:]
            outData = [0]*len(csvFile[y])

            outData[x] = csvFile[y][x]
            inData[x] = 0

            trainingData.append([inData, outData])

    return trainingData

def matchVariables(vars, map = []):
    mapped = [0] * len(map)
    for k, v in vars.iteritems():
        try:
            mapped[map.index(k)] = int(v)
        except:
            continue

    return mapped


if __name__ == '__main__':
    fail()