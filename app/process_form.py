import re
from docx import Document
import os
import requests


def docx_replace_regex(doc_obj, regex , replace):

    #regex = "/^" + regex + "$/"
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            counter = 0
            for i in range(len(inline)):

                counter=counter+1
                #print inline[i].text
                if regex.search(inline[i].text):
                    #print "found: ",regex,replace,inline[i].text 
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text
                    #print replace, regex, inline[i].text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex , replace)

def email(filename):

	print requests.post("https://api.mailgun.net/v3/sandbox6e7ba6f1a09e44c09e8db03258ead03c.mailgun.org",  
                    auth=("api", "key-d793da1727b1604ab6fa7ae8272d8360"),
                    files=[("attachment", open(filename))],
                    data={"from": "do-not-reply <postmaster@sandbox6e7ba6f1a09e44c09e8db03258ead03c.mailgun.org>",
                          "to": "kresna.jenie@gmail.com",
                          "cc": "",
                          "subject": "Hello",
                          "text": "Testing some Mailgun awesomness with attachment!",
                          "html": "<html>HTML version of the body</html>"})

def process_data(request):

	APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
	APP_STATIC = os.path.join(APP_ROOT, 'static')
	filename = os.path.join(APP_STATIC, "kader.docx")
	doc = Document(filename)

	for v in request.form:
		#v2 = "/^" +v + "$/"
		if v == 'tulang':
			print request.form[v]
		v2 = v
		regex1 = re.compile(v2)
		replace1 = request.form[v]
		print v, request.form[v]
		docx_replace_regex(doc, regex1 , replace1)

	filename = "result1.docx"
	fileoutput = os.path.join(APP_STATIC, filename)
	doc.save(fileoutput)
	#email(filename)




