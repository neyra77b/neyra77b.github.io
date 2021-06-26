import sys
import re
from collections import defaultdict

EMPTY_LINK = "(empty)"


def preamble():
	p1 = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\n\
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n\
<html xmlns=\http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\n\
        <head>\n\
                <title> Fisiopato Articulos </title>\n\
		<link rel=\"stylesheet\" type=\"text/css\" href=\"styleA.css\" />\n\
		<script type=\"text/javascript\" src=\"collapsible.js\"></script>\n\
        </head>\n\
        <body>\n\
		<center> <h1> Links pa los Portafolios 2021-1 </h1> </center>\n"
	announcement = "\t<div class=\"announcement\"> Whatsapp: \n"
	whatsapp = "\t<span class=\"contact_info\">\n\
		\t\t<a class =\"whatsappinfo\" target=\"_blank\"\n\
		\t\t\trel=\"noopener noreferrer\" href=\"https://wa.me/19098096441\"> Whatsapp </a>\n\
    \t</span>\n\
		\t</div>"
	translated = "\n<span> Se traducio los articulos con: https://www.onlinedoctranslator.com/es/ </span></br>"
	updated = "\n<span> Ultima actualizaci&oacute;n: <span class=\"last_updated\"> \
	Sabado, Junio 26, 2021 </span></span>"
	p3 = "<div class=\"maincontent\">"
	return p1 + announcement + whatsapp + translated + updated + p3

def fillWeekHdr(i):
	return "<h2> Semana " + str(i) + " </h2>\n"


def fillRow(course, link, translatedLink, pdfLink):	
	tableRowStr = "" 
	tableRowStr += "\t<tr>\n\
	\t<td>" + course + "</td>\n\
 	\t<td>\n\
  \t\t<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"" + link + "\">\n\
  \t\t\tArticulo\n\
  \t\t</a>\n\
 	\t</td>\n\
 	\t<td>\n"
	if translatedLink != EMPTY_LINK:
		tableRowStr += "\t\t<a target=\"_blank\" rel=\"noopener noreferrer\" href=" + translatedLink + ">\n\
			\t\t\tTraducido\n"
	tableRowStr += "\t\t</a>\n\
 	\t</td>\n\
 	\t<td>\n"
	if pdfLink != EMPTY_LINK:
		tableRowStr += "\t\t<a target=\"_blank\" rel=\"noopener noreferrer\" href=" + pdfLink + ">\n\
			\t\t\tDiapos de exposicion"
	tableRowStr += "\t\t</a>\n\
	</td>\n\t</tr>\n"
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
	\t<th>PPT de grupo expositor</th>\n"
	#\t<th>Bibliografia de articulo </th>\n\t</tr>\n"

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

	# Open the translated links
	translationsFile = open("translatedLinks.txt")
	translatedLinks = translationsFile.readlines()
	translationsFile.close()
	translatedLinks = [x.strip() for x in translatedLinks if x != "\n"]	

	# Open the Group PDFs
	pdfFile = open("groupPDF.txt")
	pdfLinks = pdfFile.readlines()
	pdfFile.close()
	pdfLinks = [x.strip() for x in pdfLinks if x != "\n"]

	portfolioWeeks = [4, 7, 12, 15]
	portfolioCounter = 0
	shownIndex = 3 #Portfolio that should be open

	# Create the HTML main tables	
	fileCounter = 0
	finalStr = preamble()	

	# Adding in thte buttons for collapsible
	finalStr += "\n<button type=\"button\" class=\"collapsible\"> Portafolio #" + str(portfolioCounter + 1) + "</button>"  
	finalStr += "\n<div class=\"content\">\n"
	for i in keyInt:
		# This creates the table per week
		finalStr += fillWeekHdr(i) 	
		finalStr += tableHdrStr
		for c in weekDict[str(i)]:
			finalStr += fillRow(c, driveLinks[fileCounter], 
					translatedLinks[fileCounter], pdfLinks[fileCounter]) 	
			fileCounter += 1
		finalStr += "</table>\n" 
	
		if i == portfolioWeeks[portfolioCounter]:
			portfolioCounter += 1
			finalStr += "</div>"
			if portfolioCounter < len(portfolioWeeks):
				finalStr += "\n<button type=\"button\" class=\"collapsible\"> Portafolio #" + str(portfolioCounter + 1) + "</button>"  
				if portfolioCounter == shownIndex - 1: 
					finalStr += "\n<div class=\"content\" style=\"display:block\">\n"
				else:	
					finalStr += "\n<div class=\"content\">\n"

	
	f = open("index.html", "w")
	f.write(finalStr)

	finalStr += "</div>\n\
	</body>\n\
	</html>"
	

if __name__ == "__main__":
	main()
