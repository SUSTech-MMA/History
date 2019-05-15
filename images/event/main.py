import os


result = ""
year   = 2014
for file in os.listdir():
    if file.endswith("py"):
        continue
    date  = file[:-4].split("-")
    if str(year) != date[0]:
        year   += 1
        result += "\n\n## %s年\n" % (year)
    title = "### %s年%s月%s日：XXX\n" % \
        (date[0], date[1].lstrip("0"), date[2].lstrip("0"))
    text  = "![](images/event/%s)\n\n" % (file)
    result += title + text
