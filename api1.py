import requests
import json

def get_latest_questions(site, pagesize=10):
    url = f"https://api.stackexchange.com/2.3/questions"
    params = {
        'order': 'desc',
        'sort': 'creation',
        'site': site,
        'pagesize': pagesize
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        questions = response.json()
        return questions['items']
    else:
        print(f"Error: {response.status_code}")
        return None

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

if __name__ == "__main__":
    site = "stackoverflow"  
    questions = get_latest_questions(site)
    display_questions(questions)
