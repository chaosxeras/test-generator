import json
import random

result = open('gen_result.json', 'r')
fRead = open('jsons/lawyer_approved.json', 'r')

jsonResult = json.load(result)
jsonLawyer = json.load(fRead)
resultLen = len(jsonResult["CompletedCase"])
lawyerLen = len(jsonLawyer["lawyers"])
result.close()
fRead.close()
count = 1

final = open('jsons/lawyer_approved.json','w')
for x in range (0, resultLen):
    for lawyers in jsonResult["CompletedCase"][x]["lawyers"]:
        id = int(lawyers["lawyer_id"])
        email = lawyers["lawyer_email"]

        for y in range (0, lawyerLen):
            lawyer_id = jsonLawyer["lawyers"][y]["id"]
            lawyer_email = jsonLawyer["lawyers"][y]["email"]

            if (id != lawyer_id and email != lawyer_email):
                count +=1
                if count >= lawyerLen:
                    count = 0
                    daObj = {
                        "id": id,
                        "approved_at": "now",
                        "reviewed_by": 495041,
                        "email": email,
                        "password": "lawyer3",
                        "role": "\\Canlaw\\User\\Role::LAWYER",
                        "profile": {
                        "personal": {
                            "photo": "http://lorempixel.com/400/400/people",
                            "general": "I love eating fried chips",
                            "started_practicing_in": 2014,
                            "languages": "English, Malay, Chinese, French, Japanese, Arabic, Esperanto",
                            "qualifications": "Studied languages but prefers to do law and eats potato",
                            "features_publications": "Nothing, I didn't write a thing, I love eating potato, that's why.",
                            "reported_cases": "I got hit by lightning and survived."
                        },
                        "firm": {
                            "opening_hours": "9am - 6 pm, Mon - Fri",
                            "description": "Potato heaven, indulge in all potato goodies while we discuss about your case.",
                            "address": {
                            "lat": 22.22,
                            "lng": 22.11,
                            "address": "1 chip, potato street, frying pan district, Kitchen"
                            }
                        },
                        "satisfaction_rate": random.randint(0,100)
                        },
                        "phone_number": "+60123456789"
                    }
                    JSONDATA = json.JSONEncoder().encode(daObj)
                    jsonLawyer["lawyers"].append(daObj)
                    
                else:
                    count = 1
            else:
                count = 0

json.dump(jsonLawyer, final)
final.close()
  