#Student Directory Generator Code for Energy@ Conference 2015
#Author: Chinmay Nivargi
#You will need some LaTeX distribution installed to compile the TeX file(s), Python with the necessary packages. Sample Data is provided.

#Scrape Data from survey. The survey was administered using Google forms, which outputs data into a csv, here 'Energy_Student_Directory.csv'
import csv
import urllib

#This section reads the data file, which is a csv generated through Qualtrics. This could be modified for any source. The School and colors are mapped to numbers as below.
datafile = open('Energy_Student_Directory.csv','rU')
reader = csv.reader(datafile)

rownum = 0
name, hometown, school, stanfschool, research, funfact, picture, dept = ([] for i in range(8))
stanf_school = ['Engineering','Earth','Humanities and Sciences','Education','Business','Medicine','Law'] #Check what 7 is?
colors = {1: 'Blue',2:'Green',3:'Red',4:'Yellow',5:'Purple',6:'Purple',7:'Purple'}

#Reading the csv into arrays for the different fields.
for row in reader:
	if rownum>=1:
		name.append(row[12])
		hometown.append(row[13])
		school.append(row[14])
		stanfschool.append(row[15])
		research.append(row[16])
		funfact.append(row[17])
		picture.append(row[18])
		dept.append(row[19])
	rownum+=1


#Beamer Section. This takes the data above and arranges into a beamer presentation. Make sure beamer is installed, the images are in the ./img folder, and there is a ./tex folder
i=1
while i<=len(name)-1:
	print i
	if picture[i] != "":
		urllib.urlretrieve(picture[i], "./img/student"+str(i)+".jpg") #the urllib package retrieves the images from the URL in the csv file, and stores it in img folder as studentx.jpg
		picfile="student"+str(i)+".jpg"
	else:
		picfile="logo.pdf" #default image

#The subsequent code writes a .tex file for each student. These are then combined into a single .tex
#file by generator.tex for final PDF compilation later. Some beamer customizations are also included below (beamer is
#kinda finicky if you want to change how it looks, so proceed with caution if you want to change the look and feel)
	framefile = open("./tex/student"+str(i)+".tex", "w")
	framefile.write("""\setbeamercolor*{title}{fg="""+colors[int(stanfschool[i])]+"""}
		\\setbeamercolor*{structure}{fg="""+colors[int(stanfschool[i])]+"""}

	\\setbeamercolor*{footlinecolor}{fg=white,bg="""+colors[int(stanfschool[i])]+"""}
	\\setbeamertemplate{footline}{""")
	if int(stanfschool[i]) == 1:
		framefile.write("""\\begin{beamercolorbox}[sep=0.5em,wd=\paperwidth,ht=1.35cm,leftskip=0.5cm,rightskip=0.5cm]{footlinecolor}\n""")
 	else:
 		framefile.write("""\\begin{beamercolorbox}[sep=0.68em,wd=\paperwidth,ht=1.35cm,leftskip=0.5cm,rightskip=0.5cm]{footlinecolor}\n""")
 	framefile.write("""\\parbox{\\linewidth}{\\centering """+stanf_school[int(stanfschool[i])-1]+"""}
  	\\end{beamercolorbox}%}
	}

	\\begin{frame}
	\\frametitle{\\textbf{"""+name[i]+"""}}
	\\begin{columns}[T]
	     \\begin{column}{0.4\\textwidth}
	     \\centering
	       \\begin{figure}
	\\includegraphics[width=.9\\textwidth,height=.9\\textwidth,keepaspectratio]{"""+picfile+"""}
	       \\end{figure}
	      """+dept[i]+"""
	     \\end{column}
		\\begin{column}{0.5\\textwidth}
		\\begin{itemize}
		\\setlength\\itemsep{1em}
		\\item """+hometown[i]+". "+school[i]+"""
		\\item """+research[i]+"""
		\\item """+funfact[i]+"""
		\\end{itemize}
		\\end{column}
	\\end{columns}
	\\end{frame}""")
	framefile.close()
	i+=1








