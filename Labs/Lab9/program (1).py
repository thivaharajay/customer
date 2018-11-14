import boto3
import json

client = boto3.client('comprehend')

Question = input("You can tell me “who” is going “where” on what “date” to see “what” \n")

response1 = client.detect_entities(
    Text=Question,
    LanguageCode='en'
)

for entities in response1['Entities']:
  print (entities['Type']+':'+entities['Text'])

Comment = input("Enter comment on trip \n")

response2 = client.detect_sentiment(
    Text=Comment,
    LanguageCode='en'
)

print(next(iter(response2.items())))
i = response2['Sentiment']

if i == 'POSITIVE':
	print("That sounds like you had a great time")
elif i == 'NEGATIVE':
	print("I am sorry to hear that")
else:
	print("That sounds interesting")

print("Thank You")
