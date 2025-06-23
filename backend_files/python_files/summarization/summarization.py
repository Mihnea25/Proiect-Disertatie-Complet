from transformers import AutoModelForTokenClassification, AutoModel, AutoTokenizer, pipeline
from transformers import pipeline 

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

#functie care genereaza un rezumat
def generate_summary(text,max_length,min_length):
  summary = summarizer(text,max_length = max_length,min_length = min_length,do_sample = False)
  summary_text = summary[0]['summary_text']

  while not summary_text.endswith('.') and (len(summary_text)<len(text)*0.4):
    print(f"Summary incomplete, increasing max_length to {max_length + 20}.")
    max_length += 20
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    summary_text = summary[0]['summary_text']

  return summary_text