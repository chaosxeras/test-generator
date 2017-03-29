import json
import random

result = open('gen_result.json', 'r')
fRead = open('jsons/quote.json', 'r')
jsonResult = json.load(result)
jsonQuote = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
quoteLen = len(jsonQuote["quotes"])
result.close()
fRead.close()
final = open('jsons/quote.json','w')
count = 1

for x in range (0, resultLen):
    quote_id = jsonResult["CompletedCase"][x]["quote_id"]
    quote_request_id = jsonResult["CompletedCase"][x]["quote_request_id"]
    client_email = jsonResult["CompletedCase"][x]["client_email"]
    lawyers = jsonResult["CompletedCase"][x]["lawyers"]

    for y in range (0, quoteLen):
        id = jsonQuote["quotes"][y]["id"]

        for lawyers in jsonResult["CompletedCase"][x]["lawyers"]:
            lawyer_email = lawyers["lawyer_email"]
            
            if (id != quote_id):
                count +=1
                if count >= quoteLen:
                    count = 0    
                    daObj = {
                        "id": quote_id,
                        "fees": {
                            "total": {
                                "from": 300000,
                                "to": 400000
                            },
                            "consultation": 0,
                            "legal_fees": {
                                "total": {
                                    "from": 250000,
                                    "to": 350000
                                },
                                "breakdown": [
                                    {
                                        "name": "Milestone 1",
                                        "value": {
                                            "from": 150000,
                                            "to": 250000
                                        }
                                    },
                                    {
                                        "name": "Milestone 2",
                                        "value": 100000
                                    }
                                ]
                            },
                            "gst": 6,
                            "disbursements": {
                                "total": 50000,
                                "breakdown": [
                                    {
                                        "name": "Item 1",
                                        "value": 15000
                                    },
                                    {
                                        "name": "Item 2",
                                        "value": 35000
                                    }
                                ]
                            }
                        },
                        "upfront_payment": 100000,
                        "quote_request_id": quote_request_id,
                        "approved_at": "today",
                        "reviewed_by": "gqm@gqm.com",
                        "lawyer_id": lawyer_email,
                        "client_id": client_email,
                        "accepted_by_client_at": "now",
                        "viewed_by_client_at": "yesterday"
                    }
                    JSONDATA = json.JSONEncoder().encode(daObj)
                    jsonQuote["quotes"].append(daObj)
                else:
                    count = 1
            else:
                count = 0
                
json.dump(jsonQuote, final)
final.close()
