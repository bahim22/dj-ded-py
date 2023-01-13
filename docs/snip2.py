
adj = input('Adjective: ')
verb1 = input("Verb: ")
time1 = input("Number: ")
verb2 = input("Verb: ")
siteList = input('List of live websites: ')
language1 = input("Coding Language: ")
projects = input("Project Name: ")
contactInfo = input("Email: ")


madLib = f"Learning Python is {verb1}! I've been studying for {time1}. \
I have also been practicing {language1}. \
Follow the links to view my {siteList}. \
Find my {projects} on GitHub and contact me for more information {contactInfo}"

print(madLib)

# run: python3 snip2.py
"""
(.venv) (base) iEH:docs himab$ python3 snip2.py
Adjective: challenging
Verb: code
Verb: repositories
Project Name: react, django
Cumputer programming is so challenging! \
It's exciting I love to code. Find my repositories \
    on GitHub and view my current sites react, django.
"""
