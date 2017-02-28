from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'your-account-sid'
AUTH_TOKEN = 'your-auth-token'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = 'your-number',
    from_ = 'your-twilio-number',
    body = 'Hi',
    )
print message.sid
