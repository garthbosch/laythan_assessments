questions = [
    {
        "question": "Who won the rugby world cup in 2015",
        "options": ["A. South Africa", "B. New Zealand", "C. Ireland", "D. Australia"],
        "correct_answer": "B"
    },
    {
        "question": "Who has bowled the faster ever in cricket?",
        "options": ["A. Brett Lee", "B. Shaun Tait", "C. Shoaib Akhtar", "D. Allan Donald"],
        "correct_answer": "C"
    },
    {
        "question": "Who is the fastest ever 100 meter sprinter?",
        "options": ["A. Usain Bolt", "B. Tyson Gay", "C. Yohan Blake", "D. Justin Gatlin"],
        "correct_answer": "A"
    }
]


# Function to check the answer and update score
def check_answer(question, user_answer, score):
    correct_answer = question["correct_answer"]
    if user_answer.upper() == correct_answer.upper():
        return score + 1
    else:
        return score


# Initialize score
score = 0

# Ask user to answer each question
for i, question in enumerate(questions, 1):
    print(f"Question {i}: {question['question']}")
    for option in question['options']:
        print(option)

    user_answer = input("Your answer: ").strip()
    score = check_answer(question, user_answer, score)

# Display final score
print(f"Your final score is: {score}/{len(questions)}")

