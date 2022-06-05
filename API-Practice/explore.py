from twilio.rest import Client 

ACCOUNT_SID = ""
AUTH_TOKEN = ""
RECIPIENT_NUMBER = ""

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# python is synchronous 

# to get messages
#for msg in client.messages.list(): 
#    print(msg.body)

# to delete messages
#for msg in client.messages.list(): 
#    print(f"Deleting : {msg.body}")
#    msg.delete()

## to send messages 
#msg = client.messages.create(
#    to="RECIPIENT_NUMBER",
#    from_="+19207174246", 
#    body="Hello from Python", 
#    )

print(f"Created a new message: {msg.sid}")

