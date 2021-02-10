def main():
    outfile=open('abc.txt','w')
    outfile.write('Basak\n')
    outfile.write('Ali\n')
    outfile.write('Ahmet\n')
    outfile.write('Mehmet\n')
    outfile.write('Zel\n')
    outfile.write('Mali\n')
    outfile.close()

main()

name=input('What is the name of the file? ')


infile = open(name, 'r')

for i in range(5):
    print(infile.readline(),end='')

infile.close()
