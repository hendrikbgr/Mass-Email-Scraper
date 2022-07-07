email_list = []
with open('emails.txt') as my_file:
    for line in my_file:
        line = line.replace("\n","")
        email_list.append(line)

proxy_list = []
with open('proxies.txt') as my_file:
    for line in my_file:
        line = line.replace("\n","")
        proxy_list.append(line)

keyword_list = []
with open('keywords.txt') as my_file:
    for line in my_file:
        line = line.replace("\n","")
        keyword_list.append(line)

site_list = []
with open('sites.txt') as my_file:
    for line in my_file:
        line = line.replace("\n","")
        site_list.append(line)