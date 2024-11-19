
# Automating rubric and score generation

The evaluation returns detailed feedback, including points earned, points missed, and comprehensive explanations. The part of code comprises three main components: generating automated structured rubrics, scoring responses based on these rubrics, and genrating an "Scored Rubric" based on student responce in JSON format.
### This code is ready for visualization!



## Code Structure

```.
Project Folder
├── main.py
├── returnRubric.py
├── returnScoredRubric.py
├── rubrics/
│   └── (Generated rubric files are stored here)
└── README.md
```

## Prerequisites

- Python 3.x
- OpenAI API Key
- Required Python packages: ```openai```,  ```json```

## 1) `returnRubric.py`

This module generates a structured rubric from a raw text input provided by the user. The structured rubric is stored as a JSON file in the rubrics folder for subsequent scoring use.

```generate_rubric_json(rubric_text: str) -> dict``` 
- Converts a textual rubric input into a structured JSON      format with categories, criteria, and scoring details.

## 2) `returnScoredRubric.py`

This module uses OpenAI's API to score a student's response against a structured rubric. It provides detailed feedback, including points earned/missed, and comprehensive explanations in the rubric (JSON as well). 

```score_response(rubric_json: dict, student_response: str, assignment_question: str) -> dict``` 
- Scores a given student response using the provided rubric and returns detailed feedback as a JSON object.

## 3) `main.py`

This script serves as the main entry point for generating rubrics and evaluating student responses. It integrates `returnRubric.py` and `returnScoredRubric.py` functionalities to provide a complete workflow from creating a rubric to scoring responses.

- ### Workflow
    #### Generate a Rubric
    Prompts the user to input a rubric text and saves it in structured JSON format under the rubrics directory.

    #### Evaluate Student Response
    Prompts the user for the assignment question (optional) and the student's response. Uses the saved rubric to score the response.

## `rubrics` Folder
This folder stores the generated rubric JSON files. Each rubric is saved as a separate .json file to allow for reuse and modification.





