from bs4 import BeautifulSoup as bs
from include.tools import get_html


def get_attr(soup, dc_field, key, arrayo):
    if len(arrayo) > 0:
        for attr in arrayo:
            try:
                dc_field = [dc_field['content'] for dc_field in soup.find_all("meta", attrs={key:attr})]              
            except: continue
            if len(dc_field) > 0:
                dc_field = " § ".join(dc_field)
            else: dc_field = ''    
    else: dc_field = ''
    return dc_field
def get_mutirow(dc_field, n):
    multirow = []
    if dc_field == '':
        for o in range(n):
            multirow.append('')
    elif not ' § ' in dc_field:
        multirow.append(dc_field)
        for y in range(n-1):
            multirow.append('')
    elif ' § ' in dc_field:
        dc_field_row = dc_field.split(' § ')
        multirow.append(dc_field_row[0])
        for i in range(1, n):
            try:
                multirow.append(dc_field_row[i])
            except: multirow.append('')
    return multirow


def get_metatags(doc_url, csv_style):
    
    multirow = []

    title_attrs = ['citation_title', 'DC.Title', 'DC.title', 'dcterms.title', 'DCTERMS.title', 'title']
    title_props = ['og:title']

    creator = ''
    creator_attrs = ['DC.Creator.PersonalName', 'DC.Creator', 'DC.creator', 'dc:creator', 'dcterms.creator', 'DCTERMS.creator', 'DCterms.creator', 'citation_author', 'creator', 'author']
    creator_props = []
    
    publisher = ''
    publisher_attrs = ['DC.Publisher', 'DC.publisher', 'dc:publisher', 'dcterms.publisher', 'DCTERMS.publisher', 'citation_publisher', 'publisher']
    publisher_props = ['article:publisher', 'og:site_name']
    
    contributor = ''
    contributor_attrs = ['DC.Contributor', 'DC.contributor', 'dc:contributor', 'dcterms.contributor', 'DCTERMS.contributor', 'citation_contributor']
    contributor_props = ['article:contributor']

    date = ""
    dc_date_attrs = ['DC.Date.created', 'DC.Date', 'DC.date', 'dcterms.date', 'DCTERMS.date', 'citation_publication_date', 'citation_date', 'date-created']
    dc_date_props = ['article:published_time', 'article:modified_time']

    dc_type = ""
    dc_type_attrs = ['DC.Type', 'DC.type', 'dcterms.type', 'DCTERMS.type', 'DC.Type.articleType']
    dc_type_props = ['og:type']
    
    dc_format = ''

    source = ''
    source_attrs = ['DC.Source', 'DC.source', 'dc.source', 'dc:source']
    source_props = ['og:site_name']
    
    language = ""
    language_attrs = ['DC.Language', 'DC.language', 'dc:language', 'dcterms.language', 'citation_language']
    language_props = ['og:locale']

    relation = ""
    relation_attrs = ['DC.Relation', 'DC.relation', 'dcterms.relation', 'DCTERMS.relation', 'citation_journal_title']
    relation_props = []

    coverage = ''
    coverage_attrs = ['DC.coverage', 'DC.coverage', 'dcterms.coverage', 'DCTERMS.coverage']
    
    rights = ''
    rights_attrs = ['DC.Rights', 'DC.rights', 'dcterms.rights', 'DCTERMS.rights', 'copyright']
    rights_props = []

    description = ""
    description_attrs = ['DC.Description', 'DC.description', 'DC.description', 'dcterms.description', 'DCTERMS.description', 'citation_abstract', 'dcterms.abstract', 'DCTERMS.abstract', 'abstract', 'description']
    description_props = ['og:description']
    
    subject = ""
    subject_attrs = ['DC.Subject', 'DC.subject', 'citation_keywords', 'keywords']
    subject_props = []
            
    try:
        soup = get_html(doc_url)
    except:
        raise Exception()
    # DC:IDENTIFIER
    identifier = [doc_url, '', '']
    multirow += identifier
    # DC:TITLE
    try:
        title = soup.title.text.replace("\r\n", " ").replace("&nbsp;", "").replace('<br>', '').strip()
    except: pass
    if title == '':
        title = get_attr(soup, 'title', 'name', title_attrs)
        if title == '':
            title = get_attr(soup, 'title', 'property', title_props)
    if csv_style == 'multi':
        multirow += get_mutirow(title, 3)
    # DC:CREATOR
    creator = get_attr(soup, 'creator', 'name', creator_attrs)
    if creator == '':
        creator = get_attr(soup, 'creator', 'property', creator_props)  
    if csv_style == 'multi':
        multirow += get_mutirow(creator, 5)
    # DC:PUBLISHER
    publisher = get_attr(soup, 'publisher', 'name', publisher_attrs)
    if publisher == '':
        publisher = get_attr(soup, 'publisher', 'property', publisher_props)
    if csv_style == 'multi':
        multirow += get_mutirow(publisher, 3)
    # DC:CONTRIBUTOR
    contributor = get_attr(soup, 'contributor', 'name', contributor_attrs)
    if contributor == '':
        contributor = get_attr(soup, 'contributor', 'property', contributor_props)
    if csv_style == 'multi':
        multirow += get_mutirow(contributor, 3)
    # DC:DATE
    dc_date = get_attr(soup, 'dc_date', 'name', dc_date_attrs)
    if dc_date == '':
        dc_date = get_attr(soup, 'dc_date', 'property', dc_date_props)
    if csv_style == 'multi':
        multirow += get_mutirow(dc_date, 3)
    # DC:TYPE
    dc_type = get_attr(soup, 'dc_type', 'name', dc_type_attrs)
    if dc_type == '':
        dc_type = get_attr(soup, 'dc_type', 'property', dc_type_props)
    if csv_style == 'multi':
        multirow += get_mutirow(dc_type, 3)
    # DC:FORMAT   
    try:
        dc_format = doc_url.split('/')[-1].split(".")[-1].upper()
    except:
        dc_format = "HTML"
    if csv_style == 'multi':
        multirow += get_mutirow(dc_format, 3)
    # DC:SOURCE
    source = get_attr(soup, 'source', 'name', source_attrs)
    if source == '':
        source = get_attr(soup, 'source', 'property', source_props)
    if csv_style == 'multi':
        multirow += get_mutirow(source, 3)
    # DC:LANGUAGE
    language = get_attr(soup, 'language', 'name', language_attrs)
    if language == '':
        language = get_attr(soup, 'language', 'property', language_props)
    if language == '':
        try:
            language = soup.find("meta", attrs={'http-equiv':'content-language'})['content'].strip()
        except: language = ""  
    if csv_style == 'multi':
        multirow += get_mutirow(language, 3)
    # DC:RELATION
    relation = get_attr(soup, 'relation', 'name', relation_attrs)
    if relation == '':
        relation = get_attr(soup, 'relation', 'property', relation_props)
    if csv_style == 'multi':
        multirow += get_mutirow(relation, 3)
    # DC:COVERAGE
    coverage = get_attr(soup, 'coverage', 'name', coverage_attrs)
    if csv_style == 'multi':
        multirow += get_mutirow(coverage, 3)
    # DC:RIGHTS
    rights = get_attr(soup, 'rights', 'name', rights_attrs)
    if rights == '':
        rights = get_attr(soup, 'rights', 'property', rights_props)
    if csv_style == 'multi':
        multirow += get_mutirow(rights, 3)
    # DC:DESCRIPTION'xml:lang':'it'
    description = get_attr(soup, 'description', 'name', description_attrs)
    if description == '':
        description = get_attr(soup, 'description', 'property', description_props)
    if csv_style == 'multi':
        multirow += get_mutirow(description, 3)
    # DC:SUBJECT'xml:lang':'it'
    subject = get_attr(soup, 'subject', 'name', subject_attrs)
    if subject == '':
        subject = get_attr(soup, 'subject', 'property', subject_props)
    if csv_style == 'multi':
        multirow += get_mutirow(subject, 10)


    if csv_style == '':
        metadata = [
            {'Identifier': doc_url}, 
            {'Title': title.replace(u'\n', u' ').replace(u'\t', u'')},
            {'Creator': creator.replace(u'\xa0', u' ')},
            {'Publisher': publisher}, 
            {'Contributor': contributor},
            {'Date': date}, 
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
        return metadata
    elif csv_style == 'single':
        metadata = [
            doc_url, 
            title.replace(u'\n', u' ').replace(u'\t', u''),
            creator.replace(u'\xa0', u' '),
            publisher, 
            contributor,
            date, 
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
    elif csv_style == 'multi':
        return multirow


