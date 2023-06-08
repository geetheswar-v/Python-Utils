import datetime
import re
import pickle

city_name_regex = r"(?<=\bin\s|in\s)\b\w+\b"
with open('/home/geetheswar/Documents/projects/ChatMate/chatmate/files/iit_pkd.pkl', 'rb') as file:
    iit_pkd = pickle.load(file)

additional_data = {
    "Seshadri Sekhar": "Dr. A. Seshadri Sekhar is currently the Director of IIT Palakkad, Kerala.  He received the degrees, "
              "B.E (1983) from Andhra University, M.E (1986) from IISc Bangalore and Ph.D (1993) from IIT Madras, "
              "before joining as a visiting lecturer in 1993 at IIT Kharagpur and became Professor in 2003. After "
              "serving at IIT Kharagpur for 13 years, he has been a Professor at IIT Madras since 2006. He has been "
              "the Head (2020-22) of the Mechanical Engineering department at the Indian Institute of Technology, "
              "Madras. Before that he has been the Professor-in-charge of Central Workshop (2018-20). He has also "
              "served (1999-2000) as Organising Vice-Chairman, GATE-2000 at IIT Kharagpur.",

    "Abdul Rasheed": "Dr. Abdul Rasheed P is a lecturer and research scholar. He works on Biosensors," 
                     "Early stage disease diagnosis, Wearable Bioelectronics, 2D Nanomaterials, MXenes, Electrochemistry in IIT palakkad",

    "Afzaal Ahmed": "Dr. Afzaal Ahmed is an Assistant Professor in Department of Mechanical Engineering, IIT Palakkad. "
                    "His research interests broadly centers on the non-coventional machining, hybrid machining, deep hole drilling, "
                    "laser based surface alloying and metal additive manufacturing (AM).",

    "Akshay Bhatnagar": "Dr. Akshay Bhatnagar is an Assistant Professor of Department of Physics at IIT Palakkad.",

    "Amit Kumar Pal": "Dr. Albert Sunny is an Assistant Professor of Computer Science and Engineering at IIT palakkad.",

    "Albert Sunny": "Dr. Albert Sunny is an Assistant Professor of Computer Science and Engineering at IIT palakkad.",

    "Amrita Roy": "Dr. Amrita Roy is an Assistant Professor of Humanities and Social Sciences at IIT palakkad.",

    "Anand TNC": "Dr. Anand T. N. C. is an Associate Professor of Mechanical Engineering at IIT Palakkad."

}

iit_pkd = dict(iit_pkd)
iit_pkd.update(additional_data)

def get_city(s):
    match = re.search(city_name_regex, s, re.IGNORECASE)
    if match:
        city_name = match.group(0)
        return city_name
    

def get_stocks(string):
    match = re.search(r'\b([A-Z]+)\b', string)
    if match:
        return match.group(1)
    return 'Please put the stock symbol or symbol must be uppercase'


def get_name(question):
    pattern = r"\b(?:who is|do you know|did you know|tell me about)\s(?:mr\.|prof\.|dr\.|\bmr\.|\bprof\.|\bdr\.)?\s?(\w+(?:\.\w+)?)"
    match = re.search(pattern, question)
    if match:
        return match.group(1)
    return None


def get_details(name):
    if name is not None:
        name = name.lower()
        for key, value in iit_pkd.items():
            if re.search(r"\b{}\b".format(re.escape(name)), key.lower()):
                return value
    return "I think i don't have Idea"

def is_valid_expression(expression):
    valid_pattern = r"^[()\d+\-*/.^sincotansec!]+(?:\([\d+*/.^]+\))*$"
    factorial_pattern = r"^\d+!$"
    return re.match(valid_pattern, expression) is not None or re.match(factorial_pattern, expression) is not None


def get_expression(text):
    pattern = r"(?i)(?:Calculate|What is the answer for)\s+(.*)"
    match = re.search(pattern, text)
    if match:
        expression = match.group(1)
        if is_valid_expression(expression):
            return expression
    else:
        return None


def get_timeline():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")

    return f'the time is {time} with date {date} and the day is {day}'