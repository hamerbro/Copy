# Creating the eqivalent of: COPY MENU.TXT MENU.BAK

# First open the files to read(r) and write(w)
inp = open("menu.txt", "r")
outp = open("menu.bak", "w")

# read the file, copying each line to a new file 
for line in inp: 
	outp.write(line)

print "1 file copied..."

# Now close 
inp.close()
outp.close()
