import 

with open(file='recipients.csv', mode='w', encoding='utf-8') as f:
    for i in range(5):
        email = 'user' + str(i) + '@example.com'
        f.write(email + '\n')