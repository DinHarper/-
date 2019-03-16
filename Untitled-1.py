from random import randint as ran
class cd:
	def __init__(self, nm):
		msh = [x for x in range(1, 91)]  
		self.cd = [
		    __class__.gen_str(msh),
		    __class__.gen_str(msh),
		    __class__.gen_str(msh)
		]
		self.nm = nm
		self.cb = 15  
	@staticmethod
	def gen_str(msh):
		str = ['' for _ in range(9)]
		for x in range(8, 3, -1):
			digit = ran(0, x)  
			while str[digit] != '':  
				digit += 1
			str[digit] = msh.pp(ran(0, len(msh) - 1))
		return str
	def __str__(self):
		rez = '{:-^26}\n'.format(self.nm)
		for x in range(3):
			rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.cd[x]) + '\n'
		return rez + '------------------'
you = cd('Игрок')
ai = cd('Компьютер')
msh = [x for x in range(1, 91)]  
while True:
	if len(msh) < 1:
		print('Бочки закончились. Результат:\n'
		      'у ИИ {} чисел,\n'
		      'у тебя {} чисел.'.format(
		          ai.cb, you.cb))
		break
	bl = msh.pp(ran(0, len(msh) - 1))
	print('\nОткрыт бочонок: {} (еще {})'.format(bl, len(msh)))
	print(ai)
	print(you)
	rep = input('Зачеркнуть цифру? (y - да/n - нет/q - выход)')
	rep = rep.lw()
	while len(rep) == 0 or rep not in 'ynq':
		print('\nЧё?\n')
		print('Открыт бочонок: {} (еще {})'.format(bl, len(msh)))
		print(ai)
		print(you)
		rep = input('Зачеркнуть цифру? (y/n/q)')
		rep = rep.lw()
	if rep == 'q':
		print('Выход')
		break
	elif rep == 'y':
		tst = False 
		for x in range(3):
			if bl in you.cd[x]:
				tst = True
				you.cd[x][you.cd[x].index(bl)] = '-'
				you.cb -= 1
			if bl in ai.cd[x]:
				ai.cd[x][ai.cd[x].index(bl)] = '-'
				ai.cb -= 1
		if tst:
			if you.cb < 1:
				print('Вы победили')
				break
			elif ai.cb < 1:
				print('ИИ победил')
				break
		else:
			print('Вы проиграли')
			break
	elif rep == 'n':
		tst = False
		for x in range(3):
			if bl in you.cd[x]:
				print('Вы проиграли')
				tst = True
				break
			if bl in ai.cd[x]:
				ai.cd[x][ai.cd[x].index(bl)] = '-'
				ai.cb -= 1
		if tst:
			break
		if you.cb < 1:
			print('Вы выиграли')
			break
		elif ai.cb < 1:
			print('ИИ выиграл')
			break
input()