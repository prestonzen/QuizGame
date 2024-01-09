import requests
import html

def get_questions():
    response = requests.get('https://the-trivia-api.com/v2/questions')
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to retrieve questions.')
        return []

def play_quiz():
    questions = get_questions()
    score = 0

    for i, question_data in enumerate(questions):
        question = html.unescape(question_data['question'])
        correct_answer = html.unescape(question_data['correctAnswer'])
        options = [html.unescape(ans) for ans in question_data['incorrectAnswers']]
        options.append(correct_answer)
        options.sort()

        print(f"Q{i+1}: {question}")
        for idx, option in enumerate(options):
            print(f"{idx+1}. {option}")

        user_answer = input("Your answer (number): ")
        if options[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", correct_answer)

        print()

    print("Quiz Completed. Your Score:", score)

if __name__ == "__main__":
    play_quiz()
