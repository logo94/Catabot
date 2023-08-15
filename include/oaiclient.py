# Importazione librerie
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
from csv import writer
from time import sleep
import json
from include.tools import get_host, random_user, headerow, date
import requests
from bs4 import BeautifulSoup as bs

def oai_count(url):
    try:
        addr = url + '?verb=ListRecords&metadataPrefix=oai_dc'
        page = requests.get(addr, headers=random_user())
        if page.status_code != 200:
            raise Exception()
        soup = bs(page.text, 'xml')
        count = soup.find('resumptionToken')['completeListSize']
        return count
    except:
        return '0'

def oaiReq(url):
    try:
        registry = MetadataRegistry()
        registry.registerReader('oai_dc', oai_dc_reader)
        client = Client(url, registry)
        metadata = client.listRecords(metadataPrefix='oai_dc')
        return metadata
    except:
        raise

def popola(dc_field):
    rowen = []
    row_field = []
    for field in dc_field:
        row_field.append(str(field).replace('\n', '').replace('\t', '').replace('\r', ''))
    if len(row_field) > 0:
        if len(row_field) == 1:
            arrayo = row_field[0]
        elif len(row_field) > 1:
            arrayo = ' § '.join(row_field)
    else: arrayo = ''
    rowen.append(arrayo)
    return rowen

def populate(n, dc_field):
    rowa = []
    if len(dc_field) > 0:
        rowa.append(str(dc_field[0]).replace('\n', '').replace('\t', '').replace('\r', ''))
        for i in range(1, n):
            try:
                rowa.append(str(dc_field[i]).replace('\n', '').replace('\t', '').replace('\r', ''))
            except: rowa.append('')
    else:
        for o in range(n): 
            rowa.append('')   
    return rowa

## TEST
# Manda a schermo un solo record
def test_oai(url):
    try:
        limit = 0
        while limit < 1:
            for record in oaiReq(url):
                element = record[1].getMap()
                json_element = json.dumps(element, indent=4)
                limit += 1
                return json_element
    except:
        return 'Set Dublin Core non disponibile'

# Scrittura file CSV con colonne singole
def csv_aggr_oai(url):
    try:
        domain = get_host(url)[1]
        with open('./metadata/OAI/'+date()+'_'+domain+'_oai_aggr_metadata.csv', 'w+', encoding='UTF-8', newline='') as csv_file:
            thewriter = writer(csv_file)
            header = headerow('single')
            thewriter.writerow(header)

            for record in oaiReq(url):
                row = []
                try:
                    element = record[1].getMap()
                except: continue

                row += popola(element['identifier'])
                row += popola(element['title'])
                row += popola(element['creator'])
                row += popola(element['publisher'])
                row += popola(element['contributor'])
                row += popola(element['date'])
                row += popola(element['type'])
                row += popola(element['format'])
                row += popola(element['source'])
                row += popola(element['language'])
                row += popola(element['relation'])
                row += popola(element['coverage'])
                row += popola(element['rights'])
                row += popola(element['description'])
                row += popola(element['subject'])
                
                thewriter.writerow(row)
                sleep(0.1)

    except:
        return 'Set Dublin Core non disponibile'

    return 'File CSV salvato correttamente all\'interno della cartella metadata/OAI/'

# Scrittura file CSV con colonne multiple
def csv_multi_oai(url):
    try:
        domain = get_host(url)[1]

        with open('./metadata/OAI/'+date()+'_'+domain+'_oai_multi_metadata.csv', 'w+', encoding='utf8', newline='') as csv_file:

            thewriter = writer(csv_file)
            header = headerow('multi')
            thewriter.writerow(header)

            for record in oaiReq(url):
                row = []
                try:
                    element = record[1].getMap()
                except: continue

                row += populate(3, element['identifier'])
                row += populate(3, element['title'])
                row += populate(5, element['creator'])
                row += populate(3, element['publisher'])
                row += populate(3, element['contributor'])
                row += populate(3, element['date'])
                row += populate(3, element['type'])
                row += populate(3, element['format'])
                row += populate(3, element['source'])
                row += populate(3, element['language'])
                row += populate(3, element['relation'])
                row += populate(3, element['coverage'])
                row += populate(3, element['rights'])
                row += populate(3, element['description'])
                row += populate(10, element['subject'])

                print(row)    
                thewriter.writerow(row)
                sleep(0.1)
                       
    except:
        return 'Set Dublin Core non disponibile'

    return 'File CSV salvato correttamente all\'interno della cartella metadati/OAI/'


