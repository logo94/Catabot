import csv
from include.metamodel import get_metatags
from include.tools import headerow, date
import json
from time import sleep

def meta_read_test_csv(filepath):
    try:
        with open(filepath, 'r', encoding='utf8') as file:
            reader = csv.reader(file, delimiter=',')
            print('\n\nEsempio di risultato per link:')
            print('')
            for row in reader:
                try:
                    metadata = get_metatags(row[0], '')
                except:
                    continue
                return print(json.dumps(metadata, indent=4))
    except:
        return print('Impossibile leggere il file selezionato')

def meta_read_save_csv(filepath, csv_style):
    filename = str(filepath).split('/')[-1].split('.')[0]
    with open(filepath, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        with open('metadata/metatags/'+date()+'_'+filename+'_'+csv_style+'_document_metadata.csv', 'w+', encoding='utf8', newline='') as csv_file:
            thewriter = csv.writer(csv_file)
            if csv_style == 'single':
                header = headerow(csv_style) 
            elif csv_style == 'multi':
                header = headerow(csv_style)        
            thewriter.writerow(header)
            
            for row in reader:
                try:
                    metadata = get_metatags(row[0], csv_style)
                except:
                    continue
                thewriter.writerow(metadata)
                sleep(0.1)
        
    return print("File salvato correttamente all'interno della cartella /metadata/metatags/")

