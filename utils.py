def read_file(filename):
    with open(filename, 'r') as txt_file:
        data = txt_file.read()
        data = data.split("\n")
    return data