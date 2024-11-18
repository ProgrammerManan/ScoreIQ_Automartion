import os
import json
from datetime import datetime
from returnRubric import generate_rubric_json
from returnScoredRubric import score_response

def askRubric():
    """
    Prompts the user to input rubric text, saves the structured rubric as a .json file
    in the 'rubrics' folder with a unique filename, and returns the file path.
    """
    os.makedirs('rubrics', exist_ok=True)  # Ensure 'rubrics' folder exists
    rubric_text = input("Paste the rubric text here: ").strip()
    structured_rubric = generate_rubric_json(rubric_text)

    if structured_rubric:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"rubrics/rubric_{timestamp}.json"
        with open(output_file, 'w') as file:
            json.dump(structured_rubric, file, indent=4)
        print(f"Structured rubric saved to {output_file}")
        return output_file  # Return the filename
    else:
        print("Could not generate a structured rubric. Please try again.")
        return None

def askResponse():
    """
    Prompts the user to select an existing rubric and input the assignment question (optional) and response.
    Calls the scoring function using the selected rubric file.
    """
    # List available rubrics
    rubrics_folder = 'rubrics'
    rubric_files = [f for f in os.listdir(rubrics_folder) if f.endswith('.json')]

    if not rubric_files:
        print("No rubrics found. Please create a rubric first.")
        return

    print("Available Rubrics:")
    for idx, rubric_file in enumerate(rubric_files):
        print(f"{idx + 1}: {rubric_file}")

    try:
        selection = int(input("Select the rubric to use by entering its number: ")) - 1
        if selection < 0 or selection >= len(rubric_files):
            raise ValueError("Invalid selection.")
    except ValueError:
        print("Invalid selection. Please try again.")
        return

    selected_rubric_path = os.path.join(rubrics_folder, rubric_files[selection])
    with open(selected_rubric_path, 'r') as file:
        structured_rubric = json.load(file)

    assignment_question = input("Paste the question for the assignment here [If applicable, otherwise press enter]: ").strip()
    assignment_response = input("Paste the student response for the assignment here: ").strip()

    # Call the scoring function
    scored_output = score_response(structured_rubric, assignment_response, assignment_question)

    # Save the scored output to a new JSON file
    scored_output_file = f"rubrics/scored_rubric_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(scored_output_file, 'w') as file:
        json.dump(scored_output, file, indent=4)
    print(f"Scored evaluation saved to {scored_output_file}")

# Call the main function to begin
# askRubric()
askResponse()
