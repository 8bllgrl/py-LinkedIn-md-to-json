# LinkedIn Quiz Json Creator

This program is designed to create JSON files that can be used to provide questions and answers for LinkedIn quizzes through a REST API. The goal of this project is to properly and algorithmically convert md files from [Ebazhanov's Linkedin Skill assessments - Answers](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes) into .json format for future use in a REST API.
## Usage

###Input files:
Here is a snippet from [`java-quiz.md`](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/java/java-quiz.md) :
```
#### Q1. Given the string "strawberries" saved in a variable called fruit, what would `fruit.substring(2, 5)` return?

- [ ] rawb
- [x] raw
- [ ] awb
- [ ] traw

**Reasoning:** The substring method is accepting two arguments.

- The first argument being the index to start(includes that char at 2)
- and the second the index of the string to end the substring(excludes the char at 5).
- Strings in Java are like arrays of chars.
- Therefore, the method will return "raw" as those are the chars in indexes 2,3, and 4.
- You can also take the ending index and subtract the beginning index from it, to determine how many chars will be included in the substring (5-2=3).
```

####Output files:
Here's that same example from above, turned into .json formatting through my program:
```
{
            "topic": "Java",
            "id": 1,
            "question": "\"Given the string \"strawberries\" saved in a variable called fruit, what would `fruit.substring(2, 5)` return?\"",
            "body": "",
            "answer": "\"raw\"",
            "choices": [
                "rawb",
                "raw",
                "awb",
                "traw"
            ]
        }
```

## Future plans

Currently, my goal is to add a way for the reasoning to be properly detected and included inside of the .json file.

In the future, the program will include Python testing to ensure that the JSON files are not broken in any way. Additionally, the quiz portion of the program will be implemented to create a complete LinkedIn quiz experience. 
