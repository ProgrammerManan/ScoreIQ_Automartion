import json
import openai
# Set the OpenAI API key
openai.api_key = 'your api key'

def generate_rubric_json(rubric_text):
    # OpenAI prompt to structure the rubric
    prompt = f"""
    Convert the following text-based rubric into a well-structured and detailed JSON format that reflects the exact categories, criteria, and point distribution from the original rubric. The rubric should capture every section, subcategory, and points allocation, including all the descriptions and coefficients.

Please be as detailed as possible, and ensure that every element from the rubric is properly included. For example, if there are any subcategories or additional points or specifications in the rubric, include those as well. 

For your output, follow this detailed JSON structure as an example:

EXAMPLE JSON FORMAT:
{{
    "rubric": {{
        "CategoryName": {{
            "total_points": "Total Points",
            "criteria": [
                {{
                    "description": "Description of the criterion",
                    "points": "Points allocated for this criterion",
                    "coefficient": "Coefficient for scoring this criterion",
                    "notes": "Any additional notes or details about this criterion"
                }},
                {{
                    "description": "Next criterion description",
                    "points": "Points allocated for this criterion",
                    "coefficient": "Coefficient for scoring this criterion",
                    "notes": "Any additional notes or details about this criterion"
                }}
            ]
        }},
        "Another Category": {{
            "total_points": "Total Points for this category",
            "criteria": [
                {{
                    "description": "Description of criterion",
                    "points": "Points",
                    "coefficient": "Coefficient",
                    "notes": "Optional notes"
                }}
            ]
        }}
    }}
}}

Note: Please ensure that:
- Every criterion is listed with its corresponding points, coefficient, and description.
- If there are additional notes or special instructions for each criterion, include them.
- Include all categories even if they have only one criterion.
- Preserve any hierarchy or subcategories present in the rubric text.

Rubric:
{rubric_text}

    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a JSON formatter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.2
    )
    try:
        # Extract and parse JSON from the response
        generated_text = response['choices'][0]['message']['content'].strip()
        structured_json = json.loads(generated_text)
        return structured_json
    except (json.JSONDecodeError, IndexError):
        print("Failed to generate a valid JSON structure. Please check the rubric input or the model's response.")
        return None
