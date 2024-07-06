import openai
import json
import fitz  # PyMuPDF
import os

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

from dotenv import load_dotenv  

# Load environment variables from .env file
load_dotenv()
# Access the API key using the variable name defined in the .env file
api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume(resume_text):
    # Create the prompt
    messages = [
        {
            "role": "system",
            "content": "You are an assistant that helps extract structured information from resumes."
        },
        {
            "role": "user",
            "content": f"Given the following resume text, extract the information and format it into a JSON object with the following fields:\n"
                       f"- Name\n"
                       f"- Contact Information\n"
                       f"- Work Experience\n"
                       f"- Education\n"
                       f"- Skills\n"
                       f"- Certifications\n"
                       f"- Projects\n\n"
                       f"Resume:\n{resume_text}\n\nJSON:"
        }
    ]

    # Send the prompt to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000
    )

    # Get the JSON output from the response
    output = response.choices[0].message['content'].strip()

    # Parse the output into a JSON object
    try:
        resume_json = json.loads(output)
    except json.JSONDecodeError:
        resume_json = {"error": "Failed to parse JSON response from OpenAI."}

    return resume_json

def save_json_to_file(json_data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    pdf_path = "./data/Resume.pdf"  
    output_json_path = "output/resume.json"  

    resume_text = extract_text_from_pdf(pdf_path)
    parsed_resume = parse_resume(resume_text)
    
    save_json_to_file(parsed_resume, output_json_path)

    print(f"Parsed resume saved to {output_json_path}")
