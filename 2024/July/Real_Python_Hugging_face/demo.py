# import transformers
# import torch


#pipeline() is high level abstraction which helps use any model in HuggingFace ModelsHub

from transformers import pipeline

model_name="cardiffnlp/twitter-roberta-base-sentiment-latest"
#Pipeline returns callable object
sentiment_classifier=pipeline(model=model_name)

text_input="I dont like you , why you exist in this world"
print(sentiment_classifier(text_input))

