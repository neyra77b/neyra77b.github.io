import sys
import re
from collections import defaultdict

def preamble():
	p1 = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\
<html xmlns=\http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\
        <head>\
                <title> Micro 4F Semana </title>\
		<link rel=\"stylesheet\" type=\"text/css\" href=\"styleA.css\" />\
		<script type=\"text/javascript\" src=\"collapsible.js\"></script>\
        </head>\
        <body>\
		<center> <h1> Articulos de Fisiopato 2021-2 </h1> </center>"
	announcement = "<div class=\"announcement\"> Sugerencias al link de Whatsapp: </div>"
	p3 = "<div class=\"maincontent\">"
	return p1 + announcement + p3


def fillWeekHdr(i):
	return "<h2> Semana " + str(i) + " </h2>\n"


def fillRow(course, link):	
	tableRowStr = "\t<tr>\n\
	\t<td>" + course + "</td>\n\
 	\t<td>\n\
  \t\t<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"" + link + "\">\n\
  \t\t\tLink\n\
  \t\t</a>\n\
 	\t</td>\n\
 	\t<td>\n\
  \t\t<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"\">\n\
  \t\t\t\n\
  \t\t</a>\n\
 	\t</td>\n\
 	\t<td></td>\n\t</tr>\n"
	return tableRowStr


def main():
	print(sys.argv[1])
	feedFile = open(sys.argv[1], 'r')
	topicStr = feedFile.read()
	feedFile.close()
	#print(topicStr)

	regexStr = r"Semana (\d+).*\nPráctica (\d+): Exposición de (.*)"
	matches = re.findall(regexStr, topicStr)
	#print(matches)

	weekDict = defaultdict(list)
	for match in matches:
		week = match[0]
		session = match[1]
		topics = match[2].split(",")
		topics = [x.strip() for x in topics]
		
		print("Semana: " + week + " Practica: " + session) 
		print("Expos de: ")
		for t in topics:
			print("\t" + t)
			weekDict[week].append(t)
		print()
	print(weekDict)

		
	tableHdrStr = "<table>\n\
	<tr>\n\
	\t<th>Tema</th>\n\
	\t<th>Articulo (Drive)</th>\n\
	\t<th>Articulo Traducido</th>\n\
	\t<th>Bibliografia</th>\n\t</tr>\n"

	# Order the keys of dictionary so we have 1 -> 13
	keyStr = weekDict.keys()
	keyInt = [int(x) for x in keyStr]		
	keyInt = sorted(keyInt)
	
	# Open the drive for links. 
	driveFile = open("driveLinks.txt")
	drivesLinks = driveFile.readlines()
	driveFile.close()
	driveLinks = [x.strip() for x in drivesLinks if x != "\n"]	
	#print(driveLinks)

	# Create the HTML main tables	
	driveCounter = 0
	finalStr = preamble()	
	for i in keyInt:
		finalStr += fillWeekHdr(i) 
		finalStr += tableHdrStr
		for c in weekDict[str(i)]:
			finalStr += fillRow(c, driveLinks[driveCounter]) 	
			driveCounter += 1
		finalStr += "</table>\n" 
	f = open("indexAuto.html", "w")
	f.write(finalStr)

	finalStr += "</div>\n\
	</body>\n\
	</html>"
	

if __name__ == "__main__":
	main()
