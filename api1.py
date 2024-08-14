import requests
import json
import webbrowser
from datetime import datetime, timedelta



def get_latest_questions_score(site, time, pagesize=10):
    url = f"https://api.stackexchange.com/2.3/questions"
    params = {
        'order': "desc",
        'sort': "votes",
        'fromdate': int(time.timestamp()),
        'tagged' : "python",
        "min" : "15",
        'site': site,
        'pagesize': pagesize
    }

    response = requests.get(url, params)
    
    try:
        questions = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format")
    else:
        if "items" in questions:
            for question in questions["items"]:
                webbrowser.open_new_tab(question["link"])
        else:
            print("No question withone meet conditions")


if __name__ == "__main__":
    site = "stackoverflow" 
    time = (datetime.today() - timedelta(weeks=3))
    questions = get_latest_questions_score(site, time)

"""display_questions(questions)"""
"""
def display_questions(questions):

    if questions:
       for question in questions:
            print(f"Title: {question['title']}")
            print(f"Link: {question['link']}")
            print(f"Tags: {', '.join(question['tags'])}")
            print(f"Creation Date: {question['creation_date']}")
            print(f"Score: {question['score']}")
            print('-' * 80)
            if question['answer_count']== 0:
                print(f"Its{question['answer_count']} new without any answer")
            else:
                print(f"That's not new question")

            
            else:
                print("No questions found.")
"""