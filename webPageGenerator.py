import webbrowser

#Opening summer_sale,html, append content
f = open("summer_sale.html", "a")
f.write("Here is the html code!")
f.close()

webbrowser.open('file:///C:/Python_projects/Python_projects/summer_sale.html', new=2)

