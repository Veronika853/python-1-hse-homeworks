def read(file_name='in.txt'):
    file = open(file_name, mode="r", encoding="utf-8")
    content = file.read()
    return content


def write(data, file_name='out.txt'):
    f = open(file_name, "w")
    f.write(data)
    f.close()
