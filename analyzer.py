from transformers import pipeline

# Load a free text generation model
generator = pipeline("text-generation", model="gpt2")

def analyze(prompt):
    response = generator(prompt, max_length=300, num_return_sequences=1)
    return response[0]['generated_text']
