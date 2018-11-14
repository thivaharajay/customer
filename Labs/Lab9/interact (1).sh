#interacting with chatbot
aws lex-runtime post-text \
	--region us-east-1 \
	--bot-name PrabhanjanOrderFlowersBot \
	--bot-alias "\$LATEST" \
	--user-id UserOne \
	--input-text "I would like to order flowers"

aws lex-runtime post-text \
	--region us-east-1 \
	--bot-name PrabhanjanOrderFlowersBot \
	--bot-alias "\$LATEST" \
	--user-id UserOne \
	--input-text "lilies"

aws lex-runtime post-text \
	--region us-east-1 \
	--bot-name PrabhanjanOrderFlowersBot \
	--bot-alias "\$LATEST" \
	--user-id UserOne \
	--input-text "monday"

aws lex-runtime post-text  \
	--region us-east-1 \
	--bot-name PrabhanjanOrderFlowersBot \
	--bot-alias "\$LATEST" \
	--user-id UserOne \
	--input-text "3:00 p.m."

aws lex-runtime post-text  \
	--region us-east-1 \
	--bot-name PrabhanjanOrderFlowersBot \
	--bot-alias "\$LATEST" \
	--user-id UserOne \
	--input-text "yes"

