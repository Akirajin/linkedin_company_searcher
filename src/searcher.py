from googlesearch import search as gsearch


def google_api(keyword):
    links = []
    for j in gsearch(f'linkedin {keyword}', tld="co.in", num=10, stop=10, pause=2):
        links.append(j)

    if len(links) > 0:
        return links[0]
    else:
        return None
