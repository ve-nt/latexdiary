import os
from operator import itemgetter

output = open("entries.tex", 'w')
entries = []

for dirname, dirnames, filenames in os.walk('entries'):
    for subdirname in dirnames:
        os.path.join(dirname, subdirname)

    for filename in filenames:
        if filename.endswith('.tex'):  # Only include .tex files
            dsplit = dirname.split('/')   # Split path by directory
            fsplit = filename.split(' - ')  # Split file by date and title

            texfile = {
                        'path': os.path.join(dirname) + "/" + filename[:-4],
                        'title': fsplit[1].split('.')[0],
                        'date': dsplit[1] + "-" + dsplit[2] + "-" + fsplit[0]
                      }
            entries.append(texfile)

sorted_entries = sorted(entries, key=itemgetter('date'))
for e in sorted_entries:
    # Writing the title, hspace and date
    output.write("\\textbf{" + e['title'] + "}  ")
    output.write("\\hspace*{\\fill}  ")
    output.write("\\textbf{" + e['date'] + "}\\\\\n")

    # Writing the input statement
    output.write("\\input{\"" + e['path'] + "\"} \\bigskip\n\n")
