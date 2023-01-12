def readFile(path: str = None):
    if path == None:
        print('Error: Path not specified')
        return

    file = open(path, 'r')
    data = file.read()
    file.close()
    return data