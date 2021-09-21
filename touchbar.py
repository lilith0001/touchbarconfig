import argparse
import subprocess
from pathlib import Path

homePath = Path('~').expanduser()
jsonPath = str(homePath) + '/Library/Application Support/MTMR/items.json'
configPath = str(homePath) + '/touchbarconfig/.config'

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--workspace", type=int)
parser.add_argument("-m", "--windowDest", type=int)
parser.add_argument("-s", "--sleep", type=int)
args = parser.parse_args()
workspace = args.workspace
windowDest = args.windowDest
sleep = args.sleep

json = open(jsonPath, "rt")
jsonBuffer = json.read()
json.close()

experimentalFeatures = 0;

if(workspace != None):
    print(workspace)
    
    # removing all old titles
    jsonBuffer = jsonBuffer.replace('    "title": "[ 1 ]', '    "title": "1')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 2 ]', '    "title": "2')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 3 ]', '    "title": "3')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 4 ]', '    "title": "4')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 5 ]', '    "title": "5')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 6 ]', '    "title": "6')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 7 ]', '    "title": "7')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 8 ]', '    "title": "8')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 9 ]', '    "title": "9')
    jsonBuffer = jsonBuffer.replace('    "title": "[ 0 ]', '    "title": "0')

    # adding new titles
    if(workspace == 1):
        jsonBuffer = jsonBuffer.replace('    "title": "1', '    "title": "[ 1 ]')
    elif(workspace == 2):
        jsonBuffer = jsonBuffer.replace('    "title": "2', '    "title": "[ 2 ]')
    elif(workspace == 3):
        jsonBuffer = jsonBuffer.replace('    "title": "3', '    "title": "[ 3 ]')
    elif(workspace == 4):
        jsonBuffer = jsonBuffer.replace('    "title": "4', '    "title": "[ 4 ]')
    elif(workspace == 5):
        jsonBuffer = jsonBuffer.replace('    "title": "5', '    "title": "[ 5 ]')
    elif(workspace == 6):
        jsonBuffer = jsonBuffer.replace('    "title": "6', '    "title": "[ 6 ]')
    elif(workspace == 7):
        jsonBuffer = jsonBuffer.replace('    "title": "7', '    "title": "[ 7 ]')
    elif(workspace == 8):
        jsonBuffer = jsonBuffer.replace('    "title": "8', '    "title": "[ 8 ]')
    elif(workspace == 9):
        jsonBuffer = jsonBuffer.replace('    "title": "9', '    "title": "[ 9 ]')
    elif(workspace == 10):
        jsonBuffer = jsonBuffer.replace('    "title": "0', '    "title": "[ 0 ]')

    # updating config to reflect current workspace
    config = open(configPath, "wt")
    config.write(str(workspace))
    print('wrote workspace ' + str(workspace))
    config.close()


if(experimentalFeatures == 1):
# add quotations to track the number of windows in workspaces
    if(windowDest != None):

        # removing old mark in source
        config = open(configPath, "rt")
        currentWorkspace = config.read()
        config.close()
        if(currentWorkspace == '1'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 1 ]\'', '    "title": "[ 1 ]')
        if(currentWorkspace == '2'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 2 ]\'', '    "title": "[ 2 ]')
        if(currentWorkspace == '3'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 3 ]\'', '    "title": "[ 3 ]')
        if(currentWorkspace == '4'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 4 ]\'', '    "title": "[ 4 ]')
        if(currentWorkspace == '5'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 5 ]\'', '    "title": "[ 5 ]')
        if(currentWorkspace == '6'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 6 ]\'', '    "title": "[ 6 ]')
        if(currentWorkspace == '7'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 7 ]\'', '    "title": "[ 7 ]')
        if(currentWorkspace == '8'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 8 ]\'', '    "title": "[ 8 ]')
        if(currentWorkspace == '9'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 9 ]\'', '    "title": "[ 9 ]')
        if(currentWorkspace == '10'):
            jsonBuffer = jsonBuffer.replace('    "title": "[ 0 ]\'', '    "title": "[ 0 ]')
        
        # adding new mark in destination
        if(windowDest == 1):
            jsonBuffer = jsonBuffer.replace('    "title": "1', '    "title": "1\'')
        elif(windowDest == 2):
            jsonBuffer = jsonBuffer.replace('    "title": "2', '    "title": "2\'')
        elif(windowDest == 3):
            jsonBuffer = jsonBuffer.replace('    "title": "3', '    "title": "3\'')
        elif(windowDest == 4):
            jsonBuffer = jsonBuffer.replace('    "title": "4', '    "title": "4\'')
        elif(windowDest == 5):
            jsonBuffer = jsonBuffer.replace('    "title": "5', '    "title": "5\'')
        elif(windowDest == 6):
            jsonBuffer = jsonBuffer.replace('    "title": "6', '    "title": "6\'')
        elif(windowDest == 7):
            jsonBuffer = jsonBuffer.replace('    "title": "7', '    "title": "7\'')
        elif(windowDest == 8):
            jsonBuffer = jsonBuffer.replace('    "title": "8', '    "title": "8\'')
        elif(windowDest == 9):
            jsonBuffer = jsonBuffer.replace('    "title": "9', '    "title": "9\'')
        elif(windowDest == 10):
            jsonBuffer = jsonBuffer.replace('    "title": "0', '    "title": "0\'')

json = open(jsonPath, "wt")
json.write(jsonBuffer)
json.close()