user_id = input('输入账户id：')
user_pwd = input('输入用户密码：')
user_name = input('输入用户昵称：')
user = {'u_id': user_id, 'u_pwd': user_pwd, 'u_name': user_name}
user_path = user_id  # 新建文件夹保存信息
file_user = open(user_path, 'w')
file_user.write(str(user))
file_user.close()
