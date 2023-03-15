# make code that finds a specific question passed in:
def print_specific_question(filename, question_number):
    with open(filename, 'r') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None
    end_index = 0

    for i, line in enumerate(lines):
        if '####' in line:
            if f'Q{question_number}' in line:
                start_index = i
                break
            else:
                question_count += 1

    if start_index is None:
        print(f'Question {question_number} not found.')
        return

    for i, line in enumerate(lines[start_index + 1:]):
        if '####' in line:
            end_index = i + start_index
            break
    else:
        # If we didn't find a '####' line after the current question,
        # then the current question is the last one in the file.
        end_index = len(lines)

    print(f'Question {question_number}:')

# print("-")
# # this is the body of what i want to achieve.
# exampleJsonText = \
#     '\"question\": \"questionbody\", \n' \
#     '\"choices\": [\"choice1\", \"choice2\",\"choice3\",\"choice4\"], \n' \
#     '\"answer\": \"choice2\", \n' \
#     '\"reasoning\": \"reason is that ...\", \n' \
#     '\"topic\": \"TOPIC\"'
# print(exampleJsonText)
# print("-\n")
# print("--")



# print(amount_of_questions)

# choices = get_choices_array(fileLocation, questionLookup)
# json_topic += get_topic(fileLocation)
# json_choices += formatting.makeArrayWithDoubleQuotes(choices).strip()
# # json_question += specific_questions_question(fileLocation, questionLookup)
# # json_answer += get_specific_questions_answer(fileLocation, questionLookup)
# # json_reasoning += get_explanation(fileLocation, questionLookup)
#
# print(json_question)
# print(json_choices)
# print(json_answer)
# print(json_reasoning)
# print(json_topic)
# print()


# output = {
#         "question": json_question.strip(),
#         "choices": json_choices.strip(),
#         "answer": json_answer.strip(),
#         "reasoning": json_reasoning.strip(),
#         "topic": json_topic.strip()
#     }
#
# json_object = json.dumps(output, indent=4)
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

# This is the body of my result
json_topic = "\"topic\": "
json_question = "\"question\": "
json_choices = "\"choices\": "
json_answer = "\"answer\": "
json_reasoning = "\"reasoning\": "