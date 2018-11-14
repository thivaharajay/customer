#creating slot type
aws lex-models put-slot-type \
    --region us-east-1 \
    --name PrabhanjanFlowerTypes \
    --cli-input-json file://FlowerTypes.json


#creating intent
aws lex-models put-intent \
   --region us-east-1 \
   --name PrabhanjanOrderFlowers \
   --cli-input-json file://OrderFlowers.json

#creating bot

aws lex-models put-bot \
    --region us-east-1 \
    --name PrabhanjanOrderFlowersBot \
    --cli-input-json file://OrderFlowersBot.json
