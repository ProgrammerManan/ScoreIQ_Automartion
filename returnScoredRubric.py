import openai
import json

# Set the OpenAI API key (ensure to handle the API key securely)
openai.api_key = 'your api key'

def score_response(rubric_json, student_response, assignmentQuestion):
    """
    Evaluates the student's response using the provided rubric.

    Parameters:
    - rubric_json (dict): The structured rubric JSON defining categories, criteria, etc.
    - student_response (str): The student's response to evaluate (e.g., essay, project description).

    Returns:
    - dict: The detailed scored output, indicating points earned, points missed, and feedback.
    """

    # Constructing the prompt for OpenAI to score the response
    prompt = f"""
    Use the following rubric to evaluate the student's response. 
    For each category and criterion, indicate points earned and points missed, provide feedback, 
    and explain why points were awarded or deducted. Summarize the overall performance.

    Rubric (JSON format):
    {json.dumps(rubric_json, indent=4)}
    
    Assignment Question For the (essay, project, etc) [IF APPLICABLE]
    {assignmentQuestion}
    
    Student Response:
    {student_response}

    Return the evaluation in the following JSON structure:

    {{
        "evaluation": {{
            "CategoryName": {{
                "criteria": [
                    {{
                        "description": "Description of the criterion",
                        "max_points": "Maximum points for this criterion",
                        "points_earned": "Points earned based on the response",
                        "points_missed": "Points missed based on the response",
                        "feedback": "Detailed feedback explaining the score"
                    }},
                    {{
                        "description": "Next criterion description",
                        "max_points": "Maximum points for this criterion",
                        "points_earned": "Points earned based on the response",
                        "points_missed": "Points missed based on the response",
                        "feedback": "Detailed feedback explaining the score"
                    }}
                ],
                "total_points_earned": "Total points earned for this category",
                "total_points_possible": "Total possible points for this category",
                "comments": "Overall feedback for this category"
            }},
            "Another Category": {{
                ...
            }}
        }},
        "overall_score": "Total score across all categories",
        "overall_possible_points": "Total possible points",
        "overall_feedback": "General feedback on the response"
    }}
    """

    try:
        # Make the API request to OpenAI's service
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a detailed scoring assistant evaluating student responses using a rubric."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3000,  # Adjust max tokens if needed based on input size
            temperature=0.2  # Low temperature for consistent scoring
        )

        # Extract and parse the response
        generated_text = response['choices'][0]['message']['content'].strip()
        evaluation_json = json.loads(generated_text)
        return evaluation_json

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

        return {"error": "UnexpectedError", "message": str(e)}
