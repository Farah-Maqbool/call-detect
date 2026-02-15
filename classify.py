from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = 'unitary/toxic-bert'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def classify_text(text: str) -> str:
    'classify text as yes or no'
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    scores = torch.softmax(outputs.logits, dim=1)
    label = torch.argmax(scores).item()

    if label==1:
        return 'YES'
    return 'NO'