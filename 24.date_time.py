# datetime

import datetime as d

mydate = d.date(2020, 11, 2)
print('\n mydate: ', mydate)

print('\nmydate.today(): ', mydate.today())

datedetail = '''
Todyas date: {}
Current Year: {}
Current Month: {}
'''.format(mydate.today(), mydate.today().year, mydate.today().month)

curetndatetime = d.datetime(2020, 11, 2)
print('\n Curent date and time: ', curetndatetime.now)



# month = mydate.
print(datedetail)

