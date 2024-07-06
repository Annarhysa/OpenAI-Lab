# Resume Parsing using OpenAI's GPT-3.5-turbo and PyMuPDF

This project demonstrates how to extract structured information from resumes using OpenAI's powerful language model, GPT-3.5-turbo, and PyMuPDF for PDF processing.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. Additionally, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory with the following environment variable:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### Running the Script

To parse a resume PDF file:

1. Place your resume PDF file in the `data` directory (create one if it doesn't exist).
2. Update `pdf_path` variable in `main.py` to point to your resume PDF file.
3. Run the script using:

   ```bash
   python main.py
   ```

4. The parsed JSON will be saved in the `output` directory as `resume.json`.

## Features

- **PDF Text Extraction**: Uses PyMuPDF to extract text from resume PDFs.
- **Structured Data Extraction**: Utilizes OpenAI's GPT-3.5-turbo model to extract structured information such as Name, Contact Information, Work Experience, Education, Skills, Certifications, and Projects from resume texts.
- **Output**: Saves the parsed resume data in JSON format for easy integration with other applications.

## Dependencies

- `openai`: Python client library for OpenAI API.
- `fitz`: PyMuPDF library for PDF processing.
- `dotenv`: Library for loading environment variables from `.env` file.