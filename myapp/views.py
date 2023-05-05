from django.shortcuts import render
from . import chatbot
from django.http import HttpResponse
import pymongo
from bson import ObjectId
from datetime import datetime
# Create your views here.

conn_str = "mongodb+srv://yash9657:Yash2001@cluster0.jpyaug7.mongodb.net/?retryWrites=true&w=majority"

# create a MongoClient object
client = pymongo.MongoClient(conn_str)

# access a database
db = client.test

# access a collection
collection = db.users

def next_lecture(timetable, current_time, date_index):
    # Convert current time to datetime object
    current_time = datetime.strptime(current_time, "%H:%M")

    # Find the next lecture
    if date_index == 5 or date_index == 6:
        return "Today is a Holiday !!!"
    else:
        for lecture in timetable[date_index]:
            lecture_time = datetime.strptime(lecture["time"], "%H:%M")
            if lecture_time >= current_time:
                return f"Next lecture: {lecture['subject']} at {lecture['time']} in room {lecture['room_no']}"

        # Return None if no lecture is found
        return "No more lectures for today, enjoy !!"


def day_of_week_as_index(date_string):
    # Convert date string to a datetime object
    date = datetime.strptime(date_string, '%Y-%m-%d')

    # Return the index of the day of the week
    # Monday is 0, Tuesday is 1, ..., Sunday is 6
    return date.weekday()


date_index = day_of_week_as_index("2023-04-17")

timetable = [
    [
        [
            {"subject": "Math", "time": "09:00", "room_no": "A1-103"},
            {"subject": "English", "time": "10:00", "room_no": "A1-203"},
            {"subject": "Science", "time": "11:00", "room_no": "A1-303"},
        ],
        [
            {"subject": "Physics", "time": "09:00", "room_no": "A1-104"},
            {"subject": "Chemistry", "time": "10:00", "room_no": "A1-204"},
            {"subject": "Math", "time": "11:00", "room_no": "A1-304"},
        ],
        [
            {"subject": "Biology", "time": "09:00", "room_no": "A1-205"},
            {"subject": "Physics", "time": "10:00", "room_no": "A1-105"},
            {"subject": "Science", "time": "11:00", "room_no": "A1-305"},
        ],
        [
            {"subject": "Algebra", "time": "09:00", "room_no": "A1-306"},
            {"subject": "English", "time": "10:00", "room_no": "A1-206"},
            {"subject": "Geometry", "time": "11:00", "room_no": "A1-106"},
        ],
        [
            {"subject": "Sports", "time": "09:00", "room_no": "A1-203"},
            {"subject": "Arts", "time": "10:00", "room_no": "A1-203"},
            {"subject": "Geometry", "time": "11:00", "room_no": "A1-203"},
        ]
    ],
    [
        [
            {"subject": "DSA", "time": "09:00", "room_no": "A1-103"},
            {"subject": "DELD", "time": "10:00", "room_no": "A1-203"},
            {"subject": "Spanish", "time": "11:00", "room_no": "A1-303"},
        ],
        [
            {"subject": "Seminar", "time": "09:00", "room_no": "A1-104"},
            {"subject": "PBL", "time": "10:00", "room_no": "A1-204"},
            {"subject": "DSA", "time": "11:00", "room_no": "A1-304"},
        ],
        [
            {"subject": "DELD", "time": "09:00", "room_no": "A1-205"},
            {"subject": "Economics", "time": "10:00", "room_no": "A1-105"},
            {"subject": "DSA", "time": "11:00", "room_no": "A1-305"},
        ],
        [
            {"subject": "Gym", "time": "09:00", "room_no": "A1-306"},
            {"subject": "Spanish", "time": "10:00", "room_no": "A1-206"},
            {"subject": "Geometry", "time": "11:00", "room_no": "A1-106"},
        ],
        [
            {"subject": "EM2", "time": "09:00", "room_no": "A1-203"},
            {"subject": "DELD", "time": "10:00", "room_no": "A1-203"},
            {"subject": "Spanish", "time": "11:00", "room_no": "A1-203"},
        ]
    ],
    [
        [
            {"subject": "Internship", "time": "09:00", "room_no": "A1-103"},
            {"subject": "EM3", "time": "10:00", "room_no": "A1-203"},
            {"subject": "DAA", "time": "11:00", "room_no": "A1-303"},
        ],
        [
            {"subject": "SPOS", "time": "09:00", "room_no": "A1-104"},
            {"subject": "Cyber Security", "time": "10:00", "room_no": "A1-204"},
            {"subject": "Data Science", "time": "11:00", "room_no": "A1-304"},
        ],
        [
            {"subject": "DAA", "time": "09:00", "room_no": "A1-205"},
            {"subject": "SPOS", "time": "10:00", "room_no": "A1-105"},
            {"subject": "Gym", "time": "11:00", "room_no": "A1-305"},
        ],
        [
            {"subject": "EM3", "time": "09:00", "room_no": "A1-306"},
            {"subject": "German", "time": "10:00", "room_no": "A1-206"},
            {"subject": "Cyber Security", "time": "11:00", "room_no": "A1-106"},
        ],
        [
            {"subject": "CNS", "time": "09:00", "room_no": "A1-203"},
            {"subject": "Arts", "time": "10:00", "room_no": "A1-203"},
            {"subject": "German", "time": "11:00", "room_no": "A1-203"},
        ]
    ],
    [
        [
            {"subject": "HPC", "time": "09:00", "room_no": "A1-103"},
            {"subject": "DL", "time": "10:00", "room_no": "A1-203"},
            {"subject": "AIBDA", "time": "11:00", "room_no": "A1-303"},
        ],
        [
            {"subject": "NLP", "time": "09:00", "room_no": "A1-104"},
            {"subject": "BI", "time": "10:00", "room_no": "A1-204"},
            {"subject": "Games", "time": "11:00", "room_no": "A1-304"},
        ],
        [
            {"subject": "BI", "time": "09:00", "room_no": "A1-205"},
            {"subject": "BI", "time": "10:00", "room_no": "A1-105"},
            {"subject": "NLP", "time": "11:00", "room_no": "A1-305"},
        ],
        [
            {"subject": "HPC", "time": "09:00", "room_no": "A1-306"},
            {"subject": "NLP", "time": "10:00", "room_no": "A1-206"},
            {"subject": "DL", "time": "11:00", "room_no": "A1-106"},
        ],
        [
            {"subject": "DL", "time": "09:00", "room_no": "A1-203"},
            {"subject": "DL", "time": "10:00", "room_no": "A1-203"},
            {"subject": "Games", "time": "11:00", "room_no": "A1-203"},
        ]
    ]
]

def home(request):
    return render(request,"index.html")

def get_bot_response(request):
    userText = request.GET.get("msg","")
    userText = userText.lower()
    document = collection.find_one({"_id": ObjectId("6410b83159b68712c0a2c570")})
    if("cgpa" in userText):
        cgpa = document["cgpa"]
        print('Your cgpa is: ', cgpa)
        return HttpResponse(cgpa)
    if("attendance" in userText):
        attendance = document["attendance"]
        return HttpResponse(attendance)
    if("practicals" in userText or "exams" in userText or "exam" in userText or "schedule" in userText):
        return HttpResponse('As a chatbot I am unable to answer that please contact your CC for more information.')
    if("cc" in userText or "class cordinator" in userText):
        return HttpResponse('Dr. A. G Phakatkar')
    if("hod" in userText):
        return HttpResponse('CE: Dr. G V Kale, IT: Dr. Archana Ghotkar, EnTc: Dr. Mousami Munot')
    if("next lecture" in userText):
        next_lec = next_lecture(timetable[3], "9:01", date_index)
        return HttpResponse(next_lec)
    if(userText=='OK' or userText=='Ok' or userText=='ok' or userText=='oK'):
        return HttpResponse('Bye!, see you again')
    print(userText)
    return HttpResponse(str(chatbot.gen_response(userText)))