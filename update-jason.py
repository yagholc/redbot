import os, json, uuid

# Pega os dados do json
def getJson(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        return data

#Insere novo valor,
def insertValue(dataToBeAdded):
    filename = 'people.json'
    dictA = json.loads(dataToBeAdded)
    dictB = getJson("people.json")
    dictB["Accounts"].append(dictA)
    print(dictB)
    
    with open(filename, 'w') as f:
       json.dump(dictB, f, indent=4)

#Recebe nome de usuario e retorna nivel
def consultData(username, data):
    contas = getJson("people.json")
    for conta in contas["Accounts"]:
        if(conta['id'] == username):
            return conta[data]

def transformDataToJsonObject(idAccount, nivel, beneficios, desafios):
    data = {'id': idAccount,'nivel': nivel, 'beneficios': beneficios, 'desafios': desafios}
    return json.dumps(data)

def getChallenges():
    filename = 'challenges.json'
    print(getJson(filename)["challenges"])

def getBenefits():
    filename = 'benefits.json'
    print(getJson(filename)["benefits"])

def setAccount(id, index):
    contas = getJson("people.json")
    i = 0
    for conta in contas["Accounts"]:
        if(i==index):
            conta["id"] = id
            print(conta)
        i += 1
    filename = 'people.json'
    with open(filename, 'w') as f:
       json.dump(contas, f, indent=4)

def main():
    #getChallenges()
    #getBenefits()
    dataToBeAdded = transformDataToJsonObject(123,1,[],[])
    setAccount(123,0)
    print(consultData(123, "beneficios"))

    
if __name__ == "__main__":
    main()