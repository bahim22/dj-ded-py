# from audioop import mul

SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB'],
    1024: [
        'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
    ]
}


def approximate_size(size, kb_is_1024_bytes=True):
    if size < 0:
        raise ValueError('integer must not be non-negative')
    multiple = 1024 if kb_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('integer is too large')


if __name__ == '_main_':
    print(approximate_size(100000, False))
    print(approximate_size(100000))


# List of projects
react_projects1 = ['React.js boilerplate', 'MS auth', 'portfolio v4']

next_projects1 = ['Next.js blog', 'Next.js boilerplate']

full_stack_projects1 = ['MERN Stack']

print(f'My finished projects include:\n\
        a {react_projects1[0]} template,\n\
        a {next_projects1[1]} template,\n\
        and a {full_stack_projects1[0]} web app.')

Projects = [
    {'next_projects': ['blog', 'boilerplate']},
    {'full_stack_projects': ['MERN', 'Athena']},
    {'react_projects': ['boilerplate', 'MS auth', 'portfolio v4']}
]

print(f'My finished projects include \
    {Projects[0], Projects[2], Projects[1]}')


""" initial version 1
def introduction(first_name, last_name):
    {'first_name': 'Hima', 'last_name': 'Balde'}

    print('My first name is {{ first_name }}, My last name is {{ last_name }}')
"""


# def introduction2(first_name, last_name):
#     info = {'first_name': 'Hima', 'last_name': 'Balde'}

#     print('My first name is {{ info.first_name }}, \
#           My last name is {{ last_name }}')


def intro2(f_name: str | dict, l_name: dict | str) -> None:
    # f_name = {'first_name': 'Hima'}
    f_name = 'Hima'
    l_name = {'last_name': 'Balde'}
    print(f"My first name is {f_name}, and \
          my last name is {l_name}")


""" {{ my_date | date: "Y-m-d"}}

{{ my_dict.Key }}

{{ my_object.attribute }}

{{ my_list.0 }} """
