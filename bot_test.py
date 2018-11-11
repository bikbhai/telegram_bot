import telegram
print("hllo")

TOKEN_ID='713300401:AAFZZ7x3kVFU9wXNnEPgoC26_DKkr6objSU'

def send(msg, chat_id,token_id):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token_id)
	bot.sendMessage(chat_id=chat_id, text=msg)

def main():
	send("hi Prashant",-252323998,TOKEN_ID)

main()