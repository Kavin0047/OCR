import os
import google.generativeai as genai
from PIL import Image
import pytesseract

# Set up the API key for Google's Generative AI
os.environ['GOOGLE_API_KEY'] = 'YOUR-API-KEY'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def load_image_from_path(image_path):
    # Load the image from the local file system
    return Image.open("IMAGE-PATH")

def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)
    return text

def generate_response_from_text(text, prompt):
    # Set up the Gemini model (no leading/trailing spaces)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Combine the prompt with the extracted text
    full_prompt = f"{prompt} Extracted text: {text}"
    
    # Generate content using the model
    response = model.generate_content([full_prompt])
    
    return response.text

# Provide the path to the image file
image_path = 'path/to/your/image.jpeg'
image = load_image_from_path(image_path)

# Extract text using OCR
extracted_text = extract_text_from_image(image)

# Define the prompt
prompt = "YOUR PROMPT"

# Process the text and get results from the generative model
result = generate_response_from_text(extracted_text, prompt)
print("\nExtracted Information:")
print(result)
