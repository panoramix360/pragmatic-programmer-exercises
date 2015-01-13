"""
1. Abrir o arquivo e ler para ver se ja existe algum use strict
2. Se ja tiver, pula para o proximo
3. Se nao tiver faz uma copia como backup e escreve o use strict logo apos os primeiros comentarios iniciais
4. Pula para o proximo arquivo
"""
import os
import re

files = os.listdir('.')

def backupFile(file_copy, text):
	if open_file.name.find('.pl~') == -1:
		copy = open(file_copy.name + '~', 'w+')
		copy.write(text)
		copy.close()
	else:
		copy = open(file_copy.name, 'w+')
		copy.write(text)
		copy.close()

for _file in files:
	open_file = open(_file, 'r+')

	text_file = open_file.read()

	if open_file.name.find('.pl') != -1:
		if text_file.find('use strict') != -1:
			continue
		else:
			backupFile(open_file, text_file)

			p = re.compile('\"\"\"$')

			comments = p.search(text_file)

			print comments.end()



	open_file.close()