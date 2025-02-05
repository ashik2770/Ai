from transformers import pipeline

# প্রি-ট্রেইনড মডেল লোড করা (Hugging Face থেকে)
chatbot_pipeline = pipeline('conversational', model='microsoft/DialoGPT-small')

def get_response(user_input):
    response = chatbot_pipeline(user_input)
    return response[0]['generated_text']
