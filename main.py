from groq import Groq
from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException, Form

load_dotenv()

API_KEY = os.getenv("GROQ_PRACTICE")

client = Groq(api_key=API_KEY)

app = FastAPI()


@app.post("/generate-answers/")
async def generate_answers(
        question: str = Form(None)
):
    if question is None:
        raise HTTPException(status_code=400, detail="Missing question")
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """ You are an expert in teaching English to Foreign Beginners. Your task is to give any 5 generic answers to any type of question asked.

                     Instructions:
                     1. Input: 
                     - A short question in the form of a string. For example: "What is your favorite food?"
                     - If no relevent question is asked, respond with, "Please ask an appropriate question"

                     2. Processing Instructions:
                     - Generate 5 different answers.
                     - Each answer should be line by line separately.
                     - Answer every part of the question (if more than 2).
                     - Frame each answer as a personal preference. For example: "I like pizza", "I like chicken and rice", etc.
                     - If no relevent question is asked, respond with, "Please ask an appropriate question".

                     3. Output Format: 
                     - Return the answers in the following format: "I like pizza", "I like chicken and rice", ... (up to 5 answers).
                     - Provide only the requested answers, with no extra text, or introductory statements.
                     """
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="llama3-70b-8192",
        )
        output = chat_completion.choices[0].message.content
        # Split the input string into lines
        lines = output.strip().split('\n')
        if len(lines) == 1:
            result = {
                "IncorrectQuestion" : lines
            }
        else:
            # Assign each line to a standalone variable
            option1 = lines[0]
            option2 = lines[1]
            option3 = lines[2]
            option4 = lines[3]
            option5 = lines[4]

            # Print the variables to verify
            # print(option1)
            # print(option2)
            # print(option3)
            # print(option4)
            # print(option5)

            result = {
                "option1": option1,
                "option2": option2,
                "option3": option3,
                "option4": option4,
                "option5": option5,
            }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/generate-questions-answers/")
async def generate_questions(
        topic: str = Form(None)
):
    if topic is None:
        raise HTTPException(status_code=400, detail="Missing Topic")
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """ You are an expert in teaching English to Foreign Beginners. Your task is to take the input from the user and provicde 10 basic questions with answers separated.

                     Instructions:
                     1. Input: 
                     - A topic in the form of a string. For example: "Weather" or "Personal Computers" or "Cartoons"
                     - If no relevent topic is entered, respond with, "Please enter an appropriate Topic"
                    
                     2. Processing Instructions:
                     - Generate 10 different questions related to the topic.
                     - Vary the starting words of the questions to avoid repetition.
                     - Ensure each question requires an answer that is at least 2 sentences long.
                     - All the questions should be together separated by a line. (Strictly use the suggested format)
                     - All the answers should be together separated by a line. (Strictly use the suggested format)
                     - Each question should be simple and easy to understand.
                     - Provide a simple answer(2 lines) for each simple question.
                     - Return only the questions and answers in the exact format specified.
                     - If no relevent topic is entered, respond with, "Please enter an appropriate Topic"

                     3. Output Format: 

                     - [Question]
                     - [Question]
                     - ... (up to 10 questions)

                     - [Answer]
                     - [Answer]
                     - ... (up to 10 answers)
                     """
                },
                {
                    "role": "user",
                    "content": topic,
                }
            ],
            model="llama3-70b-8192",
        )

        output = chat_completion.choices[0].message.content
        # print(output)

        # Split the output into lines
        lines = output.strip().split("\n")

        if len(lines) == 1:
            result = {
                "IncorrectTopic" : lines
            }

        else:
            empty_line_count = 0
            separator_index = None

            for i, line in enumerate(lines):
                if line.strip() == "":
                    empty_line_count += 1
                    if empty_line_count == 2:
                        separator_index = i
                        break

            # Find the index of the line that separates questions and answers
            # separator_index = lines.index("")

            # Split the lines into questions and answers based on the separator
            questions = lines[1:separator_index]  # Skipping the first two lines and the separator line
            answers = lines[separator_index + 1:]

            # Store questions and answers in separate variables
            questions_str = "\n".join(questions)
            answers_str = "\n".join(answers)

            # print(questions_str)
            # print(answers_str)

            questions = [q.strip().lstrip('-').strip() for q in questions_str.strip().split('\n') if q]
            answers = [a.strip().lstrip('-').strip() for a in answers_str.strip().split('\n') if a]

            question1 = questions[0]
            question2 = questions[1]
            question3 = questions[2]
            question4 = questions[3]
            question5 = questions[4]
            question6 = questions[5]
            question7 = questions[6]
            question8 = questions[7]
            question9 = questions[8]
            question10 = questions[9]

            answer1 = answers[0]
            answer2 = answers[1]
            answer3 = answers[2]
            answer4 = answers[3]
            answer5 = answers[4]
            answer6 = answers[5]
            answer7 = answers[6]
            answer8 = answers[7]
            answer9 = answers[8]
            answer10 = answers[9]

            # print(question1)
            # print(question2)
            # print(question3)
            # print(question4)
            # print(question5)
            # print(question6)
            # print(question7)
            # print(question8)
            # print(question9)
            # print(question10)
            #
            # print(answer1)
            # print(answer2)
            # print(answer3)
            # print(answer4)
            # print(answer5)
            # print(answer6)
            # print(answer7)
            # print(answer8)
            # print(answer9)
            # print(answer10)

            result = {
                "question1": question1,
                "question2": question2,
                "question3": question3,
                "question4": question4,
                "question5": question5,
                "question6": question6,
                "question7": question7,
                "question8": question8,
                "question9": question9,
                "question10": question10,
                "answer1": answer1,
                "answer2": answer2,
                "answer3": answer3,
                "answer4": answer4,
                "answer5": answer5,
                "answer6": answer6,
                "answer7": answer7,
                "answer8": answer8,
                "answer9": answer9,
                "answer10": answer10
            }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/generate-scenario/")
async def generating_scenario(
    situation: str = Form(None)
):
    if situation is None:
        raise HTTPException(status_code=400, detail="Missing situation")
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """ You are an expert in teaching English to Foreign Beginners. Your task is to help them navigate various real-life situations by generating dialogues.
    
                    Input:
                    - A situation in the form of a string. For exmaple "Ordering Coffee" or "Booking a Hotel" etc.
    
                    Instructions:
                    - Create a simple and clear dialogue between the user and another person (e.g., barista, cashier, Receptionist etc.).
                    - Include common phrases and vocabulary relevant to the situation but do not highlight it.
                    - Make the conversation easy to follow and understand.
                    - Always encase the participant roles in square brackets.
                    - The conversation must never be started by the user.
    
                    Output Format:  
                    - Situation: {situation}
                    - Dialogue: (Remove the heading "Dialogue")
                      [User]
                      dialogue--
                      [Other Person]
                      dialogue--
    
                     """
                },
                {
                    "role": "user",
                    "content": situation,
                }
            ],
            model="llama3-70b-8192",
        )

        output = chat_completion.choices[0].message.content
        # print(output)
        lines = output.split('\n')

        # Initialize empty lists to hold the parts of the conversation
        bot_parts = []
        user_parts = []

        # Flag to determine if the current speaker is the bot
        is_bot_turn = False

        # Iterate through the lines and categorize them
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith("["):
                # Toggle the flag based on the detected speaker
                is_bot_turn = not is_bot_turn
            elif stripped_line:  # Ignore empty lines
                # Add subsequent lines to the appropriate list based on the flag
                if is_bot_turn:
                    bot_parts.append(stripped_line)
                else:
                    user_parts.append(stripped_line)

        # Join the bot parts into a separate string
        bot_dialogue = "\n".join(bot_parts)

        # Print the separated bot dialogue
        # print("Bot Dialogue:")
        # print(bot_dialogue)
        result = {
            "dialogue": output,
            "questions": bot_dialogue,
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/checking-grammar")
async def checking_grammar(
        grammartext: str = Form(None)
):
    if grammartext is None:
        raise HTTPException(status_code=400, detail="Missing Text")
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """ You are an expert in correcting grammar. Your task is to check any grammatical mistakes in the text.

                    Input:
                    - A text in the form of a string. For example "What is you doing?"

                    Instructions:
                    - Perform grammar correction on the input text.
                    - Compare the "correction" text with the original "question" text.
                    - Do not give any extra notes. Strictly follow the output format.

                    Output Format:
                    - If the "correction" text is identical to the input text, return "The grammar is correct".
                    - If the "correction" text is not identical to the input text, return the correction text only, with no additional explanations or comments.

                    Example: for making corrections
                    Input: "What is you doing?"
                    Output: "What are you doing?"

                    Example: for not making corrections
                    Input: "What are you doing?"
                    Output: "The grammar is correct"
                    """
                },
                {
                    "role": "user",
                    "content": grammartext,
                }
            ],
            model="llama3-70b-8192",
        )
        output = chat_completion.choices[0].message.content
        print(output)
        if output == "The grammar is correct":
            result = {
                "grammar": False,
                "result": output
            }
        else:
            result = {
                "grammar": True,
                "result": output
            }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")