import re
line="cats are smarter than dogs"
mo=re.match (r'(.*)are (.*?).*',line,re.M|re.I)
if mo:
    print("match abj group:",mo.group())
    print("Group1:",mo.group(1))
    print("Group2:",mo.group(2))
