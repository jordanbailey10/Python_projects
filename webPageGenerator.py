
import webPageGenerator_gui
import webbrowser

#Opening summer_sale,html, append content
f = open("summer_sale.html", "a")
f.write("<html>\n<body>\n<h1>Stay tuned for our amazing summer sale!</h1>\n</html>")
f.close()

webbrowser.open_new_tab("summer_sale.html")
