class Phone:
    brand = 'Realme'
    price = 25000
    owner = 'MDSHE'
    features = ['Camera', 'Calling', 'Messaging']

    def call(self):
        print('Calling...Call done')

    def sms(self, number, text):
        text = f'SMS sent to 0{number}, text was {text}'
        return text

my_phn = Phone()
print(my_phn.features)
my_phn.call()
text = my_phn.sms(1763773901, "Trust Allah")
print(text)