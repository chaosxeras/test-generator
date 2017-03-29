import string
import random
import json

fJson = ""
data = ""
dLen = ""
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def client_generator():
    done = False
    while done == False:
        gen_string = id_generator()
        gen_email = "client_" + gen_string + "@client.com"
        gen_id = random.randint(0, 9999)

        for x in range (0, dLen):
            id = data["CompletedCase"][x]["client_id"]
            email = data["CompletedCase"][x]["client_email"]
            if(id != gen_id and email !=gen_email):
                done = True
            else:
                print ("Clashing info: ",id,gen_id,email, gen_email)
    return (gen_email, gen_id)

def lawyer_generator():
    done = False
    while done == False:
        gen_string = id_generator()
        gen_email = "lawyer_" + gen_string + "@lawyer.com"
        gen_id = random.randint(0, 9999)
        for x in range (0, dLen):
            for lawyers in data["CompletedCase"][x]["lawyers"]:
                id = int(lawyers["lawyer_id"])
                email = lawyers["lawyer_email"]
                if (id != gen_id and email != gen_email):
                    done = True
                else: 
                    print ("Clashed:",id,gen_id, email,gen_email)
                    
    return (gen_email, gen_id)

def quoteRequest_generator():
    gen_id = id_generator()

    fRead = open('gen_result.json', 'r')
    data = json.load(fRead)
    dLen = len(data["CompletedCase"])
    done = False
    while done == False:
        for x in range (0, dLen):
            id = data["CompletedCase"][x]["quote_request_id"]
            if(id != gen_id):
                gen_quoteID = gen_id + "-" + str(random.randint(0,1000))
                done = True
            else:
                print (id,gen_id)
    return (gen_id, gen_quoteID)

def genCompiled(howManyCases):
    for x in range (0, int(howManyCases)):
        c_gen = client_generator()
        l_gen1 = lawyer_generator()
        l_gen2 = lawyer_generator()
        l_gen3 = lawyer_generator()
        qr_gen = quoteRequest_generator()
        daObj = {
            'client_email': c_gen[0], 
            'client_id': str(c_gen[1]),
            "lawyers":[
                {
                'lawyer_email': l_gen1[0], 
                'lawyer_id': str(l_gen1[1])},
                {
                'lawyer_email': l_gen2[0], 
                'lawyer_id': str(l_gen2[1])},
                {
                'lawyer_email': l_gen3[0], 
                'lawyer_id': str(l_gen3[1])}
            ],
            'quote_request_id': qr_gen[0],
            'quote_id': qr_gen[1]
            }
        JSONDATA = json.JSONEncoder().encode(daObj)
        fJson["CompletedCase"].append(daObj)
        final = open('gen_result.json','w')
        json.dump(fJson, final)
        final.close()

if __name__ == "__main__":
    fRead = open('gen_result.json', 'r')
    data = json.load(fRead)
    dLen = len(data["CompletedCase"])
    print ("Currently there are",dLen,"cases.")
    fRead.close()
    f = open('gen_result.json', 'r')
    fJson = json.load(f)
    f.close()
    genCompiled(input("how many cases do you want to generate?"))

