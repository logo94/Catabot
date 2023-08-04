import csv
from include.tools import get_host, get_html, normalize_url, date
from datetime import datetime
## TEST ##

# Single page
def test_surl_link(url, crawl_range):
    if not 'http' in url:
        return 'URL non valido'
    if url[-1] != '/':
        url = url + '/'
    host = get_host(url)[0]
    domain = get_host(url)[1]
    try:
        soup = get_html(url)
    except:
        raise
    link_list = []
    for a_tag in soup.find_all("a"):
        try:
            link = normalize_url(host, a_tag['href'])
        except: continue
        if crawl_range == 'all':
            
            link_list.append(link)
        elif crawl_range == 'internal':
            if domain in link:
                
                link_list.append(link)
    return link_list

def fastest_surl_links(url, crawl_range):
    row = []
    domain = get_host(url)[1]
    links = test_surl_link(url, crawl_range)
    for i in range(3):
        if crawl_range == 'all':
            print(links[i])
            row.append(links[i])
        elif crawl_range == 'internal':
            if domain in links[i]:
                print(links[i])
                row.append(links[i])
        try:
            links_list = test_surl_link(links[i], crawl_range)
        except: continue
        for link in links_list:
            if not link in row:
                if crawl_range == 'all':
                    print(link)
                    row.append(link)
                elif crawl_range == 'internal':
                    if domain in link:
                        print(link)
                        row.append(link)
    return row


def test_surl_links(url, crawl_range):
    row = []
    domain = get_host(url)[1]
    for element in test_surl_link(url, crawl_range):
        if crawl_range == 'all':

            row.append(element)
        elif crawl_range == 'internal':
            if domain in element:

                row.append(element)
        try:
            links_list = test_surl_link(element, crawl_range)
        except: continue
        for link in links_list:
            if not link in row:
                if crawl_range == 'all':

                    row.append(link)
                elif crawl_range == 'internal':
                    if domain in link:

                        row.append(link)
    return row

# URL progressivo
def test_progress_link(url_pre, p_from, p_to, url_post, crawl_range):
    row = []
    for i in range(int(p_from), int(p_to)+1):
        url = url_pre + str(i) + url_post
        for link in test_surl_link(url, crawl_range):
            if not link in row:
                row.append(link)
    return row

def fastest_progress_links(url_pre, p_from, p_to, url_post, crawl_range):
    row = []
    for i in range(int(p_from), int(p_from)+1):
        url = url_pre + str(i) + url_post
        for link in test_surl_links(url, crawl_range):
            if not link in row:
                print(link)
                row.append(link)
    return row

def test_progress_links(url_pre, p_from, p_to, url_post, crawl_range):
    row = []
    for i in range(int(p_from), int(p_to)+1):
        url = url_pre + str(i) + url_post
        for link in test_surl_links(url, crawl_range):
            if not link in row:
                row.append(link)     
    return row
        


## CSV

# Single page
def link_surl_csv(url, crawl_cover, crawl_range):
    domain = get_host(url)[1]
    if crawl_cover == 'one_page':
        link_list = test_surl_link(url, crawl_range)
    elif crawl_cover == 'deep':
        link_list = test_surl_links(url, crawl_range)
    with open('./metadata/links/'+date()+'_'+domain+'_onepage_links.csv', 'w+', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        for link in link_list:
            row = []
            row.append(link)
            writer.writerow(row)
    return 'File CSV salvato correttamente all\'interno della cartella metadata/Links/'

# URL progressivo
def link_progress_csv(url_pre, p_from, p_to, url_post, crawl_cover, crawl_range):
    domain = get_host(url_pre)[1]
    if crawl_cover == 'one_page':
        link_list = test_progress_link(url_pre, p_from, p_to, url_post, crawl_range)
    elif crawl_cover == 'deep':
        link_list = test_progress_links(url_pre, p_from, p_to, url_post, crawl_range)
    with open('./metadata/links/'+date()+'_'+domain+'_urlprogress_links.csv', 'w+', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        for link in link_list:
            row = []
            row.append(link)
            writer.writerow(row)
    return 'File CSV salvato correttamente all\'interno della cartella metadata/Links/'
