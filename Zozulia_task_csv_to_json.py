# developed on python 3.9

BOOLEAN_LIST = ['True', 'False']
COMMA = ','
NEWLINE = '\n'


def read_file(file_name):
    file = open(file_name, 'r')
    data = file.read().splitlines()
    return data


def wrap_with_quotes(content):
    return '"' + content + '"'


def print_whitespaces(whitespace_count):
    return whitespace_count * ' '


def format_key_value(key, value):
    return print_whitespaces(4) + wrap_with_quotes(key) + ': ' + value


def format_value_type(value):
    if len(value) == 0:
        return 'null'
    if value.isalpha():
        if value not in BOOLEAN_LIST:
            return wrap_with_quotes(value)
        return value.lower()
    else:
        return value


def write_data(file_name, content):
    file = open(file_name, "w")
    file.write(content)
    file.close()


def csv_content_to_json_content(csv_content, spliterator=COMMA):
    if len(csv_content) < 2:
        return '[]'
    keys = csv_content[0].split(spliterator)
    result = '[' + NEWLINE
    row_count = len(csv_content[1:])

    # iterate by rows
    for row_i, row in enumerate(csv_content[1:]):
        result += print_whitespaces(2) + '{' + NEWLINE
        values = row.split(spliterator)
        zipped_key_value = dict(zip(keys, values))
        len_my_dict = len(zipped_key_value)

        # iterate by values
        for key_i, key in enumerate(zipped_key_value):
            result += format_key_value(key, format_value_type(zipped_key_value[key]))
            if key_i + 1 != len_my_dict:
                result += COMMA
            result += NEWLINE

        result += print_whitespaces(2) + '}'
        if row_i + 1 != row_count:
            result += COMMA
        result += NEWLINE
    result += ']'
    return result


def csv_file_to_json_file(input_file_path, output_file_path):
    csv_content = read_file(input_file_path)
    json_result = csv_content_to_json_content(csv_content)
    write_data(output_file_path, json_result)


csv_file_to_json_file('input.csv', 'output.json')
