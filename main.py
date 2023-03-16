import json
import os
import io
import csv


# print("Hello world")
def makeArrayWithDoubleQuotes(my_array):
    # check if array is None
    if my_array is None:
        print("Error: array is None")
        return ""

    # create a string buffer to hold the output
    output = io.StringIO()

    # create a CSV writer with quotechar='"'
    writer = csv.writer(output, quoting=csv.QUOTE_ALL, quotechar='"')

    # write the array to the output buffer
    writer.writerow(my_array)

    # return the output buffer as a string
    return output.getvalue()


def get_topic(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    topic = ""
    for i, line in enumerate(lines):
        if '## ' in line:
            topic = line.strip()[3:]
            break

    return topic


def get_choices_array(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None
    choicesHasBeenReached = False
    for i, line in enumerate(lines):
        if '####' in line:
            if f'Q{question_number}' in line:
                start_index = i
                break
            else:
                question_count += 1

    if start_index is None:
        print(f'Question {question_number} not found.')
        print(filename)
        return []

    choices = []
    recording = False

    for line in lines[start_index + 1:]:
        if '####' in line:
            break
        if '- [' in line:
            choicesHasBeenReached = True
            # break
        if '- [ ] ' in line:
            choice_start_index = line.find('- [ ] ') + len('- [ ] ')
            choice_end_index = line.find('\n', choice_start_index)
            text = line[choice_start_index:choice_end_index].strip()
            choices.append(text)
        elif '- [x] ' in line:
            start_index = line.find('- [x] ') + len('- [x] ')
            end_index = line.find('\n', start_index)
            text = line[start_index:end_index].strip()
            choices.append(text)

        if choicesHasBeenReached:
            if recording:
                contents.append(line.strip())
                if "```" in line:
                    recording = False
                    choices.append('\n'.join(contents))
            elif "```" in line:
                recording = True
                contents = [line.strip()]

    return choices


def get_question(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
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
        return ""

    for i, line in enumerate(lines[start_index + 1:]):
        if line == '\n':
            end_index = i + start_index + 1
            break

    skipLength = len("#### Q")
    question_num_digits = len(str(question_number))
    lineText = ''.join(lines[start_index:end_index])
    return "\"" + lineText[skipLength + question_num_digits + 2:].strip() + "\""


def get_answer(filename, question_number):
    with open(filename, 'r',
              encoding='utf-8') as file:  # this line opens the file that is being passed in as the string 'filename' and
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


# TODO: make it so that if a link is found (https:// or http://) then make that entire line that explanation
def get_explanation(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
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
        elif '[Reference]' in line:
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


def get_body(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    question_count = 0
    start_index = None
    end_index = None
    line_one_contents = ""

    for i, line in enumerate(lines):
        if '####' in line:
            if f'Q{question_number}' in line:
                line_one_contents = line
                start_index = i
                break
            else:
                question_count += 1

    if start_index is None:
        print(f'Question {question_number} not found.')
        return

    for i, line in enumerate(lines[start_index + 1:]):
        if line.startswith('- ['):
            end_index = i + start_index + 1
            break

    lineText = ''.join(lines[start_index:end_index])

    question_num_digits = len(str(question_number))
    output = f"{lines[start_index]}"
    output += ''.join(lines[start_index + 1:end_index])
    return output[len(line_one_contents) - 4 + question_num_digits + 2:]


def print_specific_questions_choices(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
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
    recording = False
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
            choices.append(text)

        if recording:
            contents.append(line.strip())
            if "```" in line:
                recording = False
                choices.append('\n'.join(contents))
        elif "```" in line:
            recording = True
            contents = [line.strip()]

    print(f'Question {question_number} choices:' + '\n')
    print('\n'.join(choices))
    return '\n'.join(choices)


def find_amount_of_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
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


def find_md_files(folder):
    md_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files


def question_exists(filename, question_number):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    question_count = 0

    for line in lines:
        if '####' in line:
            question_count += 1
            if f'Q{question_number}' in line:
                return True

    return False


def write_to_json(md_filename):
    print(md_filename)
    output = {"questions": []}
    output_filename = md_filename.split("\\")[-1][:-3]
    amount_of_questions = find_amount_of_questions(md_filename)
    for i in range(1, amount_of_questions):
        if question_exists(md_filename, i):
            choices = get_choices_array(md_filename, i)
            question = get_question(md_filename, i)
            answer = get_answer(md_filename, i)
            reasoning = get_explanation(md_filename, i)
            topic = get_topic(md_filename)
            body = get_body(md_filename, i)

            question_dict = {
                "topic": topic.strip(),
                "id": i,
                "question": question.strip(),
                "body": body.strip(),
                "answer": answer.strip(),
                "choices": choices,
                # "reasoning": reasoning.strip()

            }
            output["questions"].append(question_dict)
        else:
            print("Question " + str(i) + " doesn't exist. Moving onto next question")

    with open("fileOutput/" + output_filename + ".json", "w") as outfile:
        json.dump(output, outfile, indent=4)


# the location of the file
# fileLocation = "res/aws-lambda-quiz.md"
md_files = find_md_files("res")
for md_file in md_files:
    # print("23123")
    write_to_json(md_file)
# write_to_json(fileLocation)
