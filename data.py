import requests


parameters = {
    "amount" : 10 ,
    "category" : 9 ,
    "difficulty" : "medium" ,
    "type" : "boolean",

}

response = requests.get("https://opentdb.com/api.php" , params= parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


# question_data =  [
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "Haggis is traditionally ate on Burns Night.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "The French word to travel is &quot;Travail&quot;",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "There are 86400 seconds in a day.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "An eggplant is a vegetable.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "The word &quot;news&quot; originates from the first letters of the 4 main directions on a compass (North, East, West, South).",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "The average woman is 5 inches / 13 centimeters shorter than the average man.",
#             "correct_answer": "True",
#             "incorrect_answers": [
#                 "False"
#             ]
#         },
#         {
#             "type": "boolean",
#             "difficulty": "medium",
#             "category": "General Knowledge",
#             "question": "The US emergency hotline is 911 because of the September 11th terrorist attacks.",
#             "correct_answer": "False",
#             "incorrect_answers": [
#                 "True"
#             ]
#         }
#     ]
#
