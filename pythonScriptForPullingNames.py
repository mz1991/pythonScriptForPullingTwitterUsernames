# this python script pulls usernames from a .html download of Twitter's
# in-browser account search feature. (But Rachael, you might be wondering, can't
# you just search through the API? Would that I could, canny user, but
# unfortunatnly that's not currently possible.)
#
# Script written by Rachael Tatman, contact rctatman@uw.edu or @rctatman w/ ?

# import the packages we'll need
import re, glob, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-out", "--outputFileName", help="Output filename path")
args = parser.parse_args()

# text that uniquely surrounds usernames as of 12/8/2-16. You can edit
# this for a more general-purpose scrubber.
start = '<span class="visuallyhidden">Unmute @'
end = "</span></span>"

# create an output file to put our usernames in
outputFileName = args.outputFileName
output = open(outputFileName, 'w')

# set directory to the one the file is currently in
os.chdir("./")
# grab all .html files in the directory. For each file, look to see if the start
# text is in each line and, if it is, grab all characters between the start text
# and end text sepecified above.
for file in glob.glob("*.html"):
	with open(file, 'r', encoding="utf8") as f:
		line = f.readline()
		print(line)
		while line:
			if start in line:
				newline = line[line.find(start)+len(start):line.rfind(end)]	
				print(newline)
				output.write(newline + "," + file + "\n")
			line = f.readline()

# print a message to let you know the script is done
print("___________________________________________")
print("All usernames above (and the files they're from) are saved to the output file:")
print(outputFileName)

