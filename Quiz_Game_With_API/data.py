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

