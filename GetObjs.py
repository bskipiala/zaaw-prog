import csv
##bsk

def getObjs(files, classRef) -> str:
    objs = []
    with open(files, 'r', encoding='utf-8') as file:
        csvReader = csv.reader(file, delimiter=',')
        headers = next(csvReader)
        for line in csvReader:
            if len(line) == len(headers):
                classObj = {}
                for i, header in enumerate(headers):
                    classObj[header] = line[i]

                obj = classRef(**classObj)
                objs.append(obj.__dict__)
        return objs
