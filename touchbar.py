import argparse
from pathlib import Path

user = Path('~').expanduser()
items = str(user) + '/Library/Application Support/MTMR/items.json'

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--workspace", type=int)
args = parser.parse_args()
workspace = args.workspace

fin = open(items, "rt")
data = fin.read()
data = data.replace('    "title": "[ I ]",',    '    "title": "I",')
data = data.replace('    "title": "[ II ]",',   '    "title": "II",')
data = data.replace('    "title": "[ III ]",',  '    "title": "III",')
data = data.replace('    "title": "[ IV ]",',   '    "title": "IV",')
data = data.replace('    "title": "[ V ]",',    '    "title": "V",')
data = data.replace('    "title": "[ VI ]",',   '    "title": "VI",')
data = data.replace('    "title": "[ VII ]",',  '    "title": "VII",')
data = data.replace('    "title": "[ VIII ]",', '    "title": "VIII",')
data = data.replace('    "title": "[ IX ]",',   '    "title": "IX",')
data = data.replace('    "title": "[ X ]",',    '    "title": "X",')

if(workspace == 1):
    data = data.replace('    "title": "I",',    '    "title": "[ I ]",')
elif(workspace == 2):
    data = data.replace('    "title": "II",',   '    "title": "[ II ]",')
elif(workspace == 3):
    data = data.replace('    "title": "III",',  '    "title": "[ III ]",')
elif(workspace == 4):
    data = data.replace('    "title": "IV",',   '    "title": "[ IV ]",')
elif(workspace == 5):
    data = data.replace('    "title": "V",',    '    "title": "[ V ]",')
elif(workspace == 6):
    data = data.replace('    "title": "VI",',   '    "title": "[ VI ]",')
elif(workspace == 7):
    data = data.replace('    "title": "VII",',  '    "title": "[ VII ]",')
elif(workspace == 8):
    data = data.replace('    "title": "VIII",', '    "title": "[ VIII ]",')
elif(workspace == 9):
    data = data.replace('    "title": "IX",',   '    "title": "[ IX ]",')
elif(workspace == 10):
    data = data.replace('    "title": "X",',    '    "title": "[ X ]",')

fin.close()
fin = open(items, "wt")
fin.write(data)
fin.close()
