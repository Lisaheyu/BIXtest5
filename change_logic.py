def read_users_from_file():
    users = []
    f = "user.csv"
    s = f.read().split("\n")
    for i in s:
        user = {}
        user['name'] = i.split(',')[0]
        user['gender'] = i.split(',')[1]
        user['birthdate'] = i.split(',')[2]
        users.append(user)
    return users



def write_to_file(user):
    with open('user.csv','w') as f_w:
        for i in user:
            f_w.write(i + '\n')




def insert_user(user_new):
    users = read_users_from_file()
    if user_new['name'] not in [user['name'] for user in users]:
        users.append(user_new)

    #wirte to file
    write_to_file(users)

def delete_user(user_delete):

    users = read_users_from_file()
    user_list = [user['name'] for user in users]
    if user_delete  in [user['name'] for user in users]:
        users.remove(users[user_list.index(user_delete)])
        # wirte to file
    write_to_file(users)

def change_user(user_change):
    users = read_users_from_file()
    user_list = [user['name'] for user in users]
    user_before_value = users[user_list.index(user_change['name'])]
    if user_change['name'] in [user['name'] for user in users]:
        users.remove(user_before_value)
        users.append(user_change)
    # wirte to file
    write_to_file(users)

def select_user(user_name):
    users = read_users_from_file()
    user_list = [user['name'] for user in users]
    if user_name in [user['name'] for user in users]:
        user_value = users[user_list.index(user_change['name'])]
        return user_value









