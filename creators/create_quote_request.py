import json
import random

result = open('gen_result.json', 'r')
fRead = open('jsons/quote_request.json', 'r')

jsonResult = json.load(result)
jsonQuoteReq = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
quoteLen = len(jsonQuoteReq["quote_requests"])
result.close()
fRead.close()
final = open('jsons/quote_request.json','w')
count = 1

for x in range (0, resultLen):
    quote_request_id = jsonResult["CompletedCase"][x]["quote_request_id"]
    client_id = jsonResult["CompletedCase"][x]["client_email"]
    lawyers = jsonResult["CompletedCase"][x]["lawyers"]

    for y in range (0, quoteLen):
        id = jsonQuoteReq["quote_requests"][y]["id"]

        if (id != quote_request_id):
            count +=1
            if count >= quoteLen:
                daObj = {
                    "id": quote_request_id,
                    "answers": {
                        "What's the time again?": {
                        "order": 0,
                        "answer": "Maybe 7 am or something"
                        },
                        "Why there is no such thing as mouse-flavoured cat food?": {
                        "order": 1,
                        "answer": "Man, come on, it's because mouse tastes like crap"
                        },
                        "Why does Giant always play that Hallelujah song?": {
                        "order": 2,
                        "answer": "Cause it sticks to your head and you'll end up singing that in your head whenever you're buying milk somewhere... It's annoying though. I'm listening to it now."
                        }
                    },
                    "client_id": client_id,
                    "category_id": "bankruptcy",
                    "approved_at": "today",
                    "reviewed_by": "gqm@gqm.com",
                    "lawyers": lawyers,
                    "lat": 80.1133,
                    "lng": 80.1133,
                    "address": "Some street in the deserts"
                }
                JSONDATA = json.JSONEncoder().encode(daObj)
                jsonQuoteReq["quote_requests"].append(daObj)
            else:
                count = 1
        else:
            count = 0
            
json.dump(jsonQuoteReq, final)
final.close()
