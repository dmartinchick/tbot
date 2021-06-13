from utils.db_api.sqlighter import SQL



rq = SQL.get_users()
print (rq)
li_users = []
for i in rq:
    li_users.append(i[0])
    print(i)
print(li_users)
#466138751
if 466138751 in li_users:
    print('yes')
else:
    print("no")
