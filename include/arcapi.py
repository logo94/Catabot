import requests
from csv import writer
from bs4 import BeautifulSoup as bs
from time import sleep
from include.metamodel import get_metatags
from include.tools import headerow
import json
from datetime import date

def apiReq(crawl_ID, api_key):
    url = "https://partner.archive-it.org/api/reports/crawled-detail/" + crawl_ID + "?format=csv&mimetype=text/html"
    payload={}
    api_headers = {
        'Authorization': api_key
    }
    api_res = requests.request("GET", url, headers=api_headers, data=payload)
    api_data = bs(api_res.text, 'html.parser')
    return api_data

def archive_api_test(crawl_ID, apiKey):
    api_key = apiKey
    try:
        rows = apiReq(crawl_ID, api_key).text.split('\n')
    except:
        return print('Errore di connessione')
    print('\nSono stati trovati '+ str(len(rows))+ ' link')
    print('')
    print('Esempio di risultato per link:')
    print('')
    for i in range(1, len(rows)):
        try:
            doc_url = rows[i].split(',')[0]
            doc_source = rows[i].split(',')[3].replace('\n', "").strip()
            is_duplicate = rows[i].split(',')[2]
        except:
            continue
        if (is_duplicate == '0' and doc_source in doc_url):
            try:
                metadata = get_metatags(doc_url, '')
            except:
                continue
            return print(json.dumps(metadata, indent=4))
            

def archive_api_csv(crawl_ID, apiKey, csv_style):
    
    with open('metadata/metatags/'+date.today().strftime("%d%m%y")+'_'+crawl_ID + '_'+csv_style+'_document_metadata.csv', 'w+', encoding='utf8', newline='') as csv_file:
        
        api_key = apiKey
        
        thewriter = writer(csv_file)
        if csv_style == 'single':
            header = headerow(csv_style) 
        elif csv_style == 'multi':
            header = headerow(csv_style)        
        thewriter.writerow(header)
        
        try:
            rows = apiReq(crawl_ID, api_key).text.split('\n')
        except:
            print('Errore di connessione')
        print('\nScaricamento di '+ str(len(rows))+ ' link in corso\n\nAttendere...')
        for i in range(1, len(rows)):
                    
            try:
                doc_url = rows[i].split(',')[0]
                doc_source = rows[i].split(',')[3].replace('\n', "").strip()
                is_duplicate = rows[i].split(',')[2]
            except:
                continue
            if (is_duplicate == '0' and doc_source in doc_url):
                try:
                    metadata = get_metatags(doc_url, csv_style)
                except:
                    continue
                thewriter.writerow(metadata)
                sleep(0.1)
               

    return print("File salvato correttamente all'interno della cartella /metadata/metatags/")
