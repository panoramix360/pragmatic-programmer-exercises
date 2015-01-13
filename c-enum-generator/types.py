"""
	Cria tipos em C automaticamente a partir de um arquivo
"""
# ask for the name of the file to copy to
filename = raw_input('Enter the name of the file in this directory: ')

# open the file only to read the variables
type_file = open(filename, 'r')

# read the lines
content = type_file.readlines()

# take the name of the enum
name = content[0].strip('\n')

# create the two files for the C compiler
name_h = open(name + '.h', 'wb')
name_c = open(name + '.c', 'wb')

# inserts the first lines
name_h.write('typedef enum {\n')
name_c.write('const char* ' + name.upper() + '_names[] = {\n')

# inserts the states
for i in range(1, len(content)):
	name_h.write('\t' + content[i].strip('\n') + ',\n')
	name_c.write('\t"' + content[i].strip('\n') + '",\n')

# inserts the last lines of the file
name_h.write('} ' + name.upper() + ';')
name_c.write('};')

type_file.close()
name_h.close()
name_c.close()