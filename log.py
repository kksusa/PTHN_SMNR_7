import json

def ReadData():
    with open("log.json") as dataStorage:
        array = json.load(dataStorage)
    return array

def SaveData(data):
    with open("log.json", "w", encoding = "utf-8") as dataStorage:
        dataStorage.write(json.dumps(data, ensure_ascii = False))
        dataStorage.close()