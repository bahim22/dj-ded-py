from audioop import mul

def approximate_size(size, kb_is_1024_bytes=True):
    if size < 0:
        raise ValueError('number must not be non-negative')
    multiple = 1024 if kb_is_1024_bytes else 1000

    for i in suffix[multiple]:

        size 1 = multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('number too large')
if __name__ == '_main_':
     print(approximate_size(100000, False))
     print(approximate_size(100000))

react_projects = ['boilerplate' 'MS auth' 'portfolio v4']

next_projects = ['blog' 'boilerplate']

full_stack_projects = ['MERN ']



def introduction(first_name, last_name):
	{'first_name': 'Hima', 'last_name': 'Balde'}

print('My first name is {{ first_name }}, My last name is {{ last_name }}')

""" {{ my_date | date: "Y-m-d"}}

{{ my_dict.Key }}

{{ my_object.attribute }}

{{ my_list.0 }} """
