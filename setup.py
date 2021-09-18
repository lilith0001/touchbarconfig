import shutil
from pathlib import Path

homePath = Path('~').expanduser()
jsonPath = str(homePath) + '/Library/Application Support/MTMR/items.json'
shutil.copyfile('items.json', jsonPath)