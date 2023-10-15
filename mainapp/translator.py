from transformers import MarianMTModel, MarianTokenizer

# Load the English to Hindi translation model
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translator(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Translate the input text to Hindi
    translated = model.generate(**inputs)

    # Decode the translated text
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

    return translated_text[0]

# input_text = "My life was very easy in India."
#
# # Tokenize the input text
# inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#
# # Translate the input text to Hindi
# translated = model.generate(**inputs)
#
# # Decode the translated text
# translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

# print("Input Text (English):", input_text)
# print("Translated Text (Hindi):", translated_text[0])