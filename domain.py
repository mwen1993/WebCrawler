from urllib.parse import urlparse


# get only the domain name of a url (example.com)
def get_domain_name(url):
    print(url)
    result = get_sub_domain_name(url).split('.')
    if len(result[-1]) < 3:
        return result[-3] + '.' + result[-2] + '.' + result[-1]
    return result[-2] + '.' + result[-1]


# get sub domain name of a url (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
