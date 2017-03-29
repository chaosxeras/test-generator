**************************************************************************************************************
                                    Juls generator for migrator
**************************************************************************************************************

HOW TO USE:
gen.py is a case generator. it will generate test cases for canlaw-migrator

1. python3 gen.py to run it.
2. how many cases do you want to generate? TYPE IN THE NUMBER OF CASES YOU WANT
3. watch the terminal/command prompt for warnings.
4. python3 creators/create_ALL.py

this will generate json objects and store them in jsons file under the name:
1. booking_request.json
2. booking.json
3. client.json
4. lawyer_approved.json
5. quote_request.json
6. quote.json

USAGE OF THE DATA GENERATED
1. you can use everything except for the first json object (default object)
2. DO NOT REMOVE EVERYTHING COMPLETELY, leave the first json object (default object)
3. copy and paste everything that follows first json object except for the trailers ---> ]} <--- don't copy this
EG in client.json
YOU CAN STRIP IT BARE UNTIL THE FOLLOWING:
{
    "clients": [
        {
            "password": "julius",
            "id": 3948,
            "approved_at": "now",
            "email": "client2@client.com",
            "role": "\\Canlaw\\User\\Role::CLIENT",
            "phone_number": "+60123456789"
        }
    ]
}
**************************************************************************************************************
1. If you remove any item in any json files, clean ALL of them up except for first object [last resort] including gen_result.json
2. Contact Julius Ting if anything goes wrong
**************************************************************************************************************