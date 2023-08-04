from include.tools import get_html, headerow, get_host, date
from datetime import datetime
import csv
import json
from time import sleep

def html_get_value(soup, element, selector, key):
    if element == '':
        raise Exception()
    elif element == 'meta':
        try:
            field = soup.find(element, attrs=key)['content']
        except: field = ''
    else:
        if selector == '':
            try:
                field = soup.find(element).text
            except: field = ''
        elif selector != '':
            if selector == 'id':
                try:
                    field = soup.find(element, id=key).text
                except: field = ''
            elif selector == 'class':
                try:
                    field = soup.find(element, class_=key).text
                except: field = ''
            elif selector == 'attrs':
                try:
                    field = soup.find(element, attrs=key).text
                except: field = ''
            elif selector == 'value':
                try:
                    field = soup.find(element, value=key).text
                except: field = ''
    return field

    
def html_test(url, process_type,
              title_el, title_sel, title_value,
              creator_el, creator_sel, creator_value,
              publisher_el, publisher_sel, publisher_value,
              contributor_el, contributor_sel, contributor_value,
              date_el, date_sel, date_value,
              type_el, type_sel, type_value,
              format_el, format_sel, format_value,
              source_el, source_sel, source_value,
              language_el, language_sel, language_value,
              relation_el, relation_sel, relation_value,
              coverage_el, coverage_sel, coverage_value,
              rights_el, rights_sel, rights_value,
              description_el, description_sel, description_value,
              subject_el, subject_sel, subject_value
              ):
    try:
        soup = get_html(url)
    except:
        return print('Impossibile connettersi con la pagina selezionata')
    # Identifier
    identifier = url
    # Title
    try:
        title = html_get_value(soup, title_el, title_sel, title_value)
    except: title = ''
    # Creator
    try:
        creator = html_get_value(soup, creator_el, creator_sel, creator_value)
    except: creator = ''
    # Publisher
    try:
        publisher = html_get_value(soup, publisher_el, publisher_sel, publisher_value)
    except: publisher = ''
    # Contributor
    try:
        contributor = html_get_value(soup, contributor_el, contributor_sel, contributor_value)
    except: contributor = ''
    # Date
    try:
        dc_date = html_get_value(soup, date_el, date_sel, date_value)
    except: dc_date = ''
    # Type
    try:
        dc_type = html_get_value(soup, type_el, type_sel, type_value)
    except: dc_type = ''
    # Format
    if format_el == '':
        try:
            dc_format = url.split('/')[-1].split('.')[-1] 
        except:
            dc_format = ''
    else:
        dc_format = html_get_value(soup, format_el, format_sel, format_value)
    # Source
    if source_el == '':
        source = get_host(url)[0]
    else:
        source = html_get_value(soup, source_el, source_sel, source_value)
    # Language
    try:
        language = html_get_value(soup, language_el, language_sel, language_value)
    except: language = ''
    # Relation
    try:
        relation = html_get_value(soup, relation_el, relation_sel, relation_value)
    except: relation = ''
    # coverage
    try:
        coverage = html_get_value(soup, coverage_el, coverage_sel, coverage_value)
    except: coverage = ''
    # rights
    try:
        rights = html_get_value(soup, rights_el, rights_sel, rights_value)
    except: rights = ''
    # description
    try:
        description = html_get_value(soup, description_el, description_sel, description_value)
    except: description = ''
    # subject
    try:
        subject = html_get_value(soup, subject_el, subject_sel, subject_value)
    except: subject = ''
    
    if process_type == 'test':
        metadata = [
            {'Identifier': identifier}, 
            {'Title': title.replace(u'\n', u' ').replace(u'\t', u'')},
            {'Creator': creator.replace(u'\xa0', u' ')},
            {'Publisher': publisher}, 
            {'Contributor': contributor},
            {'Date': dc_date}, 
            {'Type': dc_type},
            {'Format': dc_format},
            {'Source': source},
            {'Language': language},
            {'Relation': relation},
            {'Coverage': coverage},
            {'Rights': rights},
            {'Description': description.replace(u'\n', u' ').replace(u'\t', u' ')},
            {'Subjects': subject}       
        ]
        return print(json.dumps(metadata, indent=4))
    elif process_type == 'csv':
        metadata = [
            identifier, 
            title.replace(u'\n', u' ').replace(u'\t', u''),
            creator.replace(u'\xa0', u' '),
            publisher, 
            contributor,
            dc_date, 
            dc_type,
            dc_format,
            source,
            language,
            relation,
            coverage,
            rights,
            description.replace(u'\n', u' ').replace(u'\t', u' '),
            subject
        ]
        return metadata
    


def html_csv(filepath, process_type,
            title_el, title_sel, title_value,
            creator_el, creator_sel, creator_value,
            publisher_el, publisher_sel, publisher_value,
            contributor_el, contributor_sel, contributor_value,
            date_el, date_sel, date_value,
            type_el, type_sel, type_value,
            format_el, format_sel, format_value,
            source_el, source_sel, source_value,
            language_el, language_sel, language_value,
            relation_el, relation_sel, relation_value,
            coverage_el, coverage_sel, coverage_value,
            rights_el, rights_sel, rights_value,
            description_el, description_sel, description_value,
            subject_el, subject_sel, subject_value):
    filename = str(filepath).split('/')[-1].split('.')[0]
    with open(filepath, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        with open('metadata/HTML/'+date()+'_'+filename+'_document_metadata.csv', 'w+', encoding='utf8', newline='') as csv_file:
            thewriter = csv.writer(csv_file)
            header = headerow('single') 
            thewriter.writerow(header)
            
            for row in reader:
                try:
                    metadata = html_test(row[0], process_type,
                                        title_el, title_sel, title_value,
                                        creator_el, creator_sel, creator_value,
                                        publisher_el, publisher_sel, publisher_value,
                                        contributor_el, contributor_sel, contributor_value,
                                        date_el, date_sel, date_value,
                                        type_el, type_sel, type_value,
                                        format_el, format_sel, format_value,
                                        source_el, source_sel, source_value,
                                        language_el, language_sel, language_value,
                                        relation_el, relation_sel, relation_value,
                                        coverage_el, coverage_sel, coverage_value,
                                        rights_el, rights_sel, rights_value,
                                        description_el, description_sel, description_value,
                                        subject_el, subject_sel, subject_value)
                except:
                    continue
                thewriter.writerow(metadata)
                sleep(0.1)

    return print("File salvato correttamente all'interno della cartella /metadata/HTML/")
