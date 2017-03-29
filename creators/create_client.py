import json

result = open('gen_result.json', 'r')
fRead = open('jsons/client.json', 'r')

jsonResult = json.load(result)
jsonClient = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
clientLen = len(jsonClient["clients"])
result.close()
fRead.close()
final = open('jsons/client.json','w')

count = 1
for x in range (0, resultLen):
    id = int(jsonResult["CompletedCase"][x]["client_id"])
    email = jsonResult["CompletedCase"][x]["client_email"]

    for y in range (0, clientLen):
        client_id = jsonClient["clients"][y]["id"]
        client_email = jsonClient["clients"][y]["email"]

        if (id != client_id and email != client_email):
            
            count +=1
            if count >= clientLen:
                count = 0
                daObj = {
                    "id": id,
                    "approved_at": "now",
                    "email": email,
                    "password": "client",
                    "role": "\\Canlaw\\User\\Role::CLIENT",
                    "phone_number": "+60123456789"
                }
                JSONDATA = json.JSONEncoder().encode(daObj)
                jsonClient["clients"].append(daObj)
            else:
                count = 1
        else:
            count = 0
                
        

json.dump(jsonClient, final)
final.close()