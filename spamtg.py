from telethon.sync import TelegramClient, events

#SERGOPROXY TG:@sergey0804,darksploit:SergoProxy
print("'TG - spam' - скрипт написан SergoProxy, для спама в личных сообщения телеграм. \n Все вопросы и идеи в TG: @sergey0804")
print()
hashtg = input("Введите хэш аккаунта: ")
iptg = int(input("Введите ip приложения: "))
px = int(input("Введите количество сообщений: "))
idp = input("Введите id пользователя: ")
mes = input("Текст сообщения: ")

api_id = iptg
api_hash = hashtg

for i in range(px):
	with TelegramClient('proxy', api_id, api_hash) as client:
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		
#SERGOPROXY TG:@sergey0804,darksploit:SergoProxy
