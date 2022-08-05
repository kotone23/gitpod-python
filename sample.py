max = 4
with open(file='recipients.csv', mode='w', encoding='utf-8') as f:
    for i in range(max+1):
        email = 'user' + str(i) + '@example.com'
        f.write(email)
        if not i == max:
            f.write(',')