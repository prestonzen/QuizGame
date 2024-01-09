# Trivia Quiz Game

Welcome to the Trivia Quiz Game! This interactive CLI application tests your knowledge with a variety of trivia questions.

## How to Play
- Run the script `quizGame.py` and wait for the questions to load.
- You'll be presented with multiple-choice questions.
- Enter the number corresponding to your answer.
- Your score will be displayed at the end of the quiz.

## Features
- Fetches random trivia questions from an online API.
- Interactive command-line interface.
- Keeps track of your correct answers.

## Requirements
- Python 3
- `requests` library (install using `pip install requests`)

## Setup and Execution
- **Local Execution:**
  - Clone this repository or download the `quizGame.py` file.
  - Run the script with `python quizGame.py`.
- **Google Colab:**
  - Access the provided Google Colab file.
  - Run the cells to execute the quiz interactively.

## Workflow Diagram
```plantuml
@startuml
start
:Start Quiz;
:Fetch Questions from API;
repeat :Display Question;
-> Get User Input;
:Check Answer;
repeat while (More Questions?)
:Display Final Score;
stop
@enduml
