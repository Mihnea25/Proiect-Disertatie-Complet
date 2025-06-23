from transformers import AutoModelForTokenClassification, AutoModel, AutoTokenizer, pipeline
from transformers import pipeline 

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

#functie care genereaza un rezumat
def generate_summary(text, max_length, min_length):
    current_max_length = max_length
    summary_text = ""

    while True:
        summary = summarizer(text, max_length=current_max_length, min_length=min_length, do_sample=False)
        summary_text = summary[0]['summary_text'].strip()

        if summary_text.endswith(('.', '!', '?')) and len(summary_text) >= len(text) * 0.3:
            break

        print(f"Summary incomplete or too short, increasing max_length to {current_max_length + 20}.")
        current_max_length += 20

        if current_max_length > len(text):
            break

    if not summary_text.endswith(('.', '!', '?')):
        summary_text += '.'

    return summary_text