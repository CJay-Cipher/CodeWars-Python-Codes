"""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" == domain name = "github"
* url = "http://www.zombie-bites.com"         == domain name = "zombie-bites"
* url = "https://www.cnet.com"                == domain name = cnet"

             more examples
"http://google.com"    == google
"http://google.co.jp"  == google
"www.xakep.ru"         == xakep
"https://youtube.com"  == youtube

"""

def domain_name(url):
    import re
    for word in re.split(r'[/.]', url):
        if word not in ["www", "http:", "https:", "com", ""]:
            return word


# Testing
print(domain_name("http://github.com/carbonfive/raygun") == "github")
print(domain_name("http://www.zombie-bites.com") == "zombie-bites")
print(domain_name("https://www.cnet.com") == "cnet")

print(domain_name("http://google.com") == "google")
print(domain_name("http://google.co.jp") == "google")
print(domain_name("www.xakep.ru") == "xakep")
print(domain_name("https://youtube.com") == "youtube")
