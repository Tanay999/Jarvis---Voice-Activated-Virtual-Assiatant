import google.generativeai as genai

genai.configure(api_key="AIzaSyDFcDwvQuLfEAEUhUi03biWYP-a8XX2zd0")

model = genai.GenerativeModel(model_name="text-bison-001")  # Replace with desired model

# Generate text
response = model.generate_text(prompt="You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please")
print(response.text)
