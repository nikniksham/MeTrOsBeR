from urllib.request import urlopen

link = "https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva/universalnye-chistyashchie-sredstva/domestos-hvoya-15l"
openedpage = urlopen(link)
content = openedpage.read()
code = content.decode("utf-8")
# title = code.find("<title>")
# title_start = title + len("<title>")
# title_end = code.find("</title>")
# full_title = code[title_start:title_end]
print(code)