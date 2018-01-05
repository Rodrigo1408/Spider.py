from urllib.parse import urlparse


# Obter o nome do domínio (exemplo.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Obter o nome do subdomínio (nome.exemplo.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
