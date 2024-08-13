import requests
import json
import pprint

def get_latest_questions_score(site, pagesize=10):
    url = f"https://api.stackexchange.com/2.3/questions"
    params = {
        'order': "desc",
        'sort': "votes",
        'fromdate': "2024-05-30",
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
        pprint.pprint(questions)

"""def display_questions(questions):

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
                print("No questions found.")"""

if __name__ == "__main__":
    
    site = "stackoverflow" 
    questions = get_latest_questions_score(site)
"""display_questions(questions)"""
