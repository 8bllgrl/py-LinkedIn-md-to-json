import io
import csv
import json

import testing
import formatting


def get_topic(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    topic = ""
    for i, line in enumerate(lines):
        if '## ' in line:
            topic = line.strip()[3:]
            break

    return topic


def get_choices_array(filename, question_number):
    with open(filename, 'r') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None

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

    choices = []
    for line in lines[start_index + 1:]:
        if '####' in line:
            break
        if '- [ ] ' in line:
            choice_start_index = line.find('- [ ] ') + len('- [ ] ')
            choice_end_index = line.find('\n', choice_start_index)
            text = line[choice_start_index:choice_end_index].strip()
            choices.append(text)
        elif '- [x] ' in line:
            start_index = line.find('- [x] ') + len('- [x] ')
            end_index = line.find('\n', start_index)
            text = line[start_index:end_index].strip()
            choices.append(text.strip())

    return choices


def get_question(filename, question_number):
    with open(filename, 'r') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None
    end_index = None

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
        if line == '\n':
            end_index = i + start_index + 1
            break

    skipLength = len("#### Q")
    question_num_digits = len(str(question_number))
    lineText = ''.join(lines[start_index:end_index])
    return "\"" + lineText[skipLength + question_num_digits + 2:].strip() + "\""


def get_answer(filename, question_number):
    with open(filename, 'r') as file:  # this line opens the file that is being passed in as the string 'filename' and
        # reading it with 'r, and assigning it to the variable 'f'

        lines = file.readlines()  # this is reading all lines in the file and storing them in a list of strings
        # called 'lines'.

    question_count = 0  # initializes a variable for the number of questions and set it to 0 at first
    start_index = None  # initialize the start index as None.

    for enumerateIndex, line in enumerate(lines):  # iterating through each 'line' in the list of 'lines'
        if '####' in line:  # if '####' is reached, is present
            # do one of two things:
            # one: if the string Q is followed by the question_number, assign start index to the i.
            if f'Q{question_number}' in line:  # 'f' at the beginning of the string indicates it's formatted.
                start_index = enumerateIndex
                break
            # two: question count goes up by one
            else:
                question_count += 1

    # if the start_index is none, then the question number was not found.
    if start_index is None:
        print(f'Question {question_number} not found.')
        return

    answer = None  # initialize the answer variable starting as value None

    for line in lines[start_index + 1:]:  # iterate thru lines list starting at the question passed in the method

        # if '####' is found, then break. exit the loop.
        if '####' in line:
            break
        # if '- [x] ' is found, find the amount of characters that '- [x] ' takes up and strip it from the answer
        if '- [x] ' in line:
            answer_start_index = line.find('- [x] ') + len('- [x] ')
            answer = line[answer_start_index:].strip()
            break

    # if the answer has no value, then print out that the answer to the question was not found.
    if answer is None:
        return ""
    # if the answer did have a value, print it out.
    else:
        return "\"" + answer + "\""


def get_explanation(filename, question_number):
    with open(filename, 'r') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None
    end_index = 0
    found_explanation = False

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
        if '**Explanation**' in line:
            found_explanation = True
            start_index = start_index + i + 1
        elif '**Reasoning**' in line:
            found_explanation = True
            start_index = start_index + i + 1

    else:
        # If we didn't find a '####' line after the current question,
        # then the current question is the last one in the file.
        end_index = len(lines)

    if found_explanation:
        return ''.join(lines[start_index + 2:end_index]).strip()
    else:
        return ""


def find_amount_of_questions(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    question_count = 0  # start at index 1

    for line in lines:
        if '#### Q' in line:
            question_count += 1

    if question_count == 0:
        print("No questions found in the file.")
    else:
        question_count = question_count + 1

    return question_count


def write_to_json(md_filename):
    output = {"questions": []}
    output_filename = md_filename.split("/")[-1][:-3]
    amount_of_questions = find_amount_of_questions(fileLocation)
    for i in range(1, amount_of_questions):
        choices = get_choices_array(fileLocation, i)
        question = get_question(fileLocation, i)
        answer = get_answer(fileLocation, i)
        reasoning = get_explanation(fileLocation, i)
        topic = get_topic(fileLocation)

        question_dict = {
            "question": question.strip(),
            "answer": answer.strip(),
            "choices": choices,
            "reasoning": reasoning.strip(),
            "topic": topic.strip()
        }
        output["questions"].append(question_dict)

    with open("fileOutput/" + output_filename + ".json", "w") as outfile:
        json.dump(output, outfile, indent=4)


# the location of the file
fileLocation = "res/aws-lambda-quiz.md"

write_to_json(fileLocation)