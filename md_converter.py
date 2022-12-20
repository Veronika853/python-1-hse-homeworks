SOURCE_CODE_DELIMITER = "# ---<source code delimeter>---"
SOURCE_MD_DELIMITER = "<!---source markdown delimeter--->"


def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content


def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()


def parse_data(data):
    lines = data.split('\n')
    new_content = {}
    title, description = '', ''
    source_code = data.split(SOURCE_CODE_DELIMITER)[1]

    for line in lines:
        if line.startswith('# title'):
            title = line.lstrip("# title ")
        elif line.startswith('# description '):
            description = line.lstrip("# description ")
    new_content['title'], new_content['description'], new_content['code'] = title, description, source_code
    return new_content


def parse_txt_data(data):
    old_content = {}
    if data != "":
        old_content['titles'], old_content['description_and_code'] = data.split(SOURCE_MD_DELIMITER)
    return old_content

def format_new_data(new_content):
    title, description, code = new_content['title'], new_content['description'], new_content['code']
    link = "-".join(title.lower().split())
    title_template = '+ [{}](#{})\n{}'
    description_and_code_template = '\n## {}\n\n{}\n\n```python\n{}\n```'
    title_md = title_template.format(title, link, SOURCE_MD_DELIMITER)
    description_and_code_md = description_and_code_template.format(title, description, code.lstrip())
    new_content_md = {}
    new_content_md['title'] = title_md
    new_content_md['description_and_code'] = description_and_code_md
    return new_content_md

def convert_to_md(new_file, old_file):
    old_content = parse_txt_data(old_file)
    new_content_md = format_new_data(parse_data(new_file))
    if not old_content:
        return '{}\n{}'.format(new_content_md['title'], new_content_md['description_and_code'])
    else:
        template = '{}{}{}\n\n{}'
        return template.format(old_content['titles'], new_content_md['title'],
                               old_content['description_and_code'], new_content_md['description_and_code'])


new_file = read_data('solution.py')
old_file = read_data('out.txt')
md_content = convert_to_md(new_file, old_file)
write_data('out.txt', md_content)
