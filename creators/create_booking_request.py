import json
import random

result = open('gen_result.json', 'r')
fRead = open('jsons/booking_request.json', 'r')
jsonResult = json.load(result)
jsonBookingReq = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
bookingReqLen = len(jsonBookingReq["booking_requests"])
result.close()
fRead.close()
final = open('jsons/booking_request.json','w')
count = 1
for x in range (0, resultLen):
    quote_id = jsonResult["CompletedCase"][x]["quote_id"]
    client_email = jsonResult["CompletedCase"][x]["client_email"]
    lawyers = jsonResult["CompletedCase"][x]["lawyers"]

    for y in range (0, bookingReqLen):
        id = jsonBookingReq["booking_requests"][y]["quote_id"]

        for lawyers in jsonResult["CompletedCase"][x]["lawyers"]:
            lawyer_email = lawyers["lawyer_email"]
            if (id != quote_id):
                count +=1
                if count >= bookingReqLen:
                    count = 0
                    daObj = {
                        "client_id": client_email,
                        "lawyer_id": lawyer_email,
                        "quote_id": quote_id,
                        "time_slot": {
                            "start": "+1 week 2 days",
                            "end": "+1 week 2 days 1 hour"
                        },
                        "confirmed_at": "null",
                        "address": {
                            "lat": 22.1133,
                            "lng": 22.1133,
                            "address": "Some street in the deserts"
                        }
                    }
                    JSONDATA = json.JSONEncoder().encode(daObj)
                    jsonBookingReq["booking_requests"].append(daObj)
                else:
                    count = 1
            else:
                count = 0
                
json.dump(jsonBookingReq, final)
final.close()