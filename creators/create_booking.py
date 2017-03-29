import json
import random

result = open('gen_result.json', 'r')
fRead = open('jsons/booking.json', 'r')
jsonResult = json.load(result)
jsonBooking = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
bookingLen = len(jsonBooking["bookings"])
result.close()
fRead.close()
final = open('jsons/booking.json','w')
count = 1
for x in range (0, resultLen):
    quote_id = jsonResult["CompletedCase"][x]["quote_id"]
    client_email = jsonResult["CompletedCase"][x]["client_email"]
    lawyers = jsonResult["CompletedCase"][x]["lawyers"]

    for y in range (0, bookingLen):
        id = jsonBooking["bookings"][y]["quote_id"]

        for lawyers in jsonResult["CompletedCase"][x]["lawyers"]:
            lawyer_email = lawyers["lawyer_email"]
            if (id != quote_id):
                count +=1
                if count >= bookingLen:
                    count = 0
                    daObj =   {
                        "client_id": client_email,
                        "lawyer_id": lawyer_email,
                        "quote_id": quote_id,
                        "time_slot": {
                        "start": "+5 days",
                        "end": "+5 days 1 hour"
                        },
                        "confirmed_at": "now",
                        "lawyer_notes": "Please bring Document A and B with you.",
                        "address": {
                        "lat": 22.1133,
                        "lng": 22.1133,
                        "address": "Some street in the deserts"
                        }
                    }
                    JSONDATA = json.JSONEncoder().encode(daObj)
                    jsonBooking["bookings"].append(daObj)
                else:
                    count = 1
            else:
                count = 0
                
json.dump(jsonBooking, final)
final.close()