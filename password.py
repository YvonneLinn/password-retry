password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('帳號已鎖定')
