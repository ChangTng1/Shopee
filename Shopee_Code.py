print("Hello world")

#Q5
num_user, num_trans = list(map(int, input().split(' ')))

data = []

for i in range(num_user):
    user_data = input().split(' ')
    data.append([user_data[0], int(user_data[1])])
data = dict(data)

for i in range(num_trans):
    trans_data = input().split(' ')
    if data[trans_data[0]]>=int(trans_data[2]):
        data[trans_data[0]]-=int(trans_data[2])
        data[trans_data[1]]+=int(trans_data[2])

data = sorted(data.items(), key=lambda x: x[0],reverse=False)

for row in data:
    print(row[0],row[1])
