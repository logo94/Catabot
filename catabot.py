from include.links import test_surl_link, test_progress_link, link_surl_csv, fastest_surl_links, link_progress_csv, fastest_progress_links
from include.oaiclient import test_oai, csv_aggr_oai, csv_multi_oai, oai_count
from include.SEO import meta_read_save_csv, meta_read_test_csv
from include.arcapi import archive_api_test, archive_api_csv
from include.HTML import html_test, html_csv
import PySimpleGUI as sg
import os
import webbrowser


def main():

    # Inizializzazione variabili
    directory = os.getcwd() + '/metadata/'
    html_elements = ['', 'a', 'article', 'b', 'button', 'cite', 'code', 'div', 'footer', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'i', 'li', 'label', 'link', 'meta', 'ol', 'option', 'p', 'pre', 'q', 'select', 'small', 'source', 'span', 'strong', 'td', 'time', 'title', 'ul']
    html_selectors = ['', 'id', 'class', 'attrs', 'value']
    link_manuale = 'https://github.com/logo94/Catabot/wiki'

    ### GUI ###
    sg.theme('DarkBlack')

    ## HOMEPAGE ##
    home_text = '''
 _____       _        _           _   
/ ____|     | |      | |         | |  
| |     __ _| |_ __ _| |__   ___ | |_ 
| |    / _` | __/ _` | '_ \ / _ \| __|
| |___| (_| | || (_| | |_) | (_) | |_ 
\_____ \__,_\__ \__,_|_.__/ \___/ \__|
    '''

    desc_text = '''
         Catabot è un software che incorpora diverse 
    modalità di raccolta automatica di metadati descrittivi
              secondo lo standard Dublin Core

       Partendo da un OAI endpoint, un indirizzo URL o una 
      lista di link, Catabot permette di estrarre fino a 15 
            elementi descrittivi ed esportarli in 
                        formato CSV
'''
    homepage_layout = [
        [sg.Text('', pad=(0,15))],
        [sg.Push()],   
        [sg.Push(), sg.Text(home_text, font='Courier 15'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text(desc_text, font='Courier 15'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Per maggiori informazioni consulta la', font='Courier 15'), sg.Text('GUIDA', font='Courier 17', tooltip=link_manuale, enable_events=True, key='home_manuale'), sg.Push()]
    ]

    ## OAI-PMH ##
    oai_frame_layout = [
        [sg.Push()],
        [sg.Push(), sg.Text('Selezionare struttura per eventuali campi multi-valore'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Radio('Multi-colonna', 'OAI_radio', key='OAI_cols', default=True), sg.Radio('Aggrega valori ( § )', 'OAI_radio'), sg.Push()],
        [sg.Push()]
    ]

    oai_title_layout = [
        [sg.Push()],
        [sg.Push(), sg.Text('Estrazione metadati descrittivi tramite OAI-PMH', font='Any 15'), sg.Push()],
        [sg.Push()], 
    ]

    oai_scraper_layout = [
        [sg.Text('', pad=(0,10))],
        [sg.Push()],
        [sg.Push(), sg.Frame('', oai_title_layout, pad=(10,20), font='Any 15'), sg.Push()],
        [sg.Push()],   
        [sg.Push(), sg.Text('Inserire OAI Endpoint senza parametri (?verb=...)', pad=(0,20), font='Any 12'), sg.Push()],
        [sg.Push(), sg.InputText(key='OAI_endpoint', size=(60,15)), sg.Push()], # 1 - Host
        [sg.Push()],
        [sg.Frame('Configurazione foglio CSV', oai_frame_layout, font='Any 13', pad=(0,25))],
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='OAI_start_test', pad=(10,35)), sg.Button('Salva CSV', key='OAI_save_csv', pad=(10,20)), sg.Push()],
        [sg.Push()]
    ]

    ## Links ##
    # SingleURL
    link_title_layout = [
        [sg.Push()],
        [sg.Push(), sg.Text('Estrazione URLs', font='Any 15'), sg.Push()],
        [sg.Push()], 
    ]

    link_type_frame = [
        [sg.Push()],
        [sg.Push(), sg.Radio('Tutti i link', 'LINK_rg_radio', key='LINK_surl_all', default=True), sg.Radio('Solo link interni', 'LINK_rg_radio', key='LINK_surl_internal'), sg.Push()],
        [sg.Push()]]

    link_cover_frame = [
        [sg.Push()],
        [sg.Push(), sg.Radio('Pagina singola', 'LINK_np_radio', key='LINK_single_page', default=True), sg.Radio('Pagina + link II livello', 'LINK_np_radio', key='LINK_page_1'), sg.Push()],
        [sg.Push()]]

    link_surl_frame = [
        [sg.Text('')],
        [sg.Push(), sg.Text('Inserire URL di partenza', pad=(0,5)), sg.Push()],
        [sg.Push(), sg.InputText(key='LINK_surl_host', size=(50,15)), sg.Push()], # 1 - Host
        [sg.Push()],
        [sg.Push(), sg.Frame('Profondità raccolta', link_cover_frame, font='Any 10', pad=(0,5)), sg.Push()],        
        [sg.Push()],
        [sg.Push(), sg.Frame('Ampiezza raccolta', link_type_frame, font='Any 10', pad=(0,5)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='LINK_start_surl_test', pad=(10,15)), sg.Button('Salva CSV', key='LINK_save_surl_csv', pad=(10,15)), sg.Push()],
        [sg.Push()]]
    
    # Progress URL
    link_type_frame_prog = [
        [sg.Push()],
        [sg.Push(), sg.Radio('Tutti i link', 'LINK_prog_rg_radio', key='LINK_progr_all', default=True), sg.Radio('Solo link interni', 'LINK_prog_rg_radio', key='LINK_progr_internal'), sg.Push()],
        [sg.Push()]]

    link_cover_frame_prog = [
        [sg.Push()],
        [sg.Push(), sg.Radio('Pagina singola', 'LINK_prog_np_radio', key='LINK_progress_page', default=True), sg.Radio('Pagina + link II livello', 'LINK_prog_np_radio', key='LINK_progress_page_1'), sg.Push()],
        [sg.Push()]]

    link_multi_col1 = [
        [sg.Push(), sg.Text('Inizio URL'), sg.Push()],
        [sg.Push(), sg.InputText(key='LINK_multi_preurl', size=(25,5)), sg.Push()]]

    link_multi_col2 = [
        [sg.Push(), sg.Text('Da'), sg.Text('A'), sg.Push()],
        [sg.Push(), sg.InputText(key='LINK_multi_from', size=(5,5)), sg.InputText(key='LINK_multi_to', size=(5,5)), sg.Push()]]

    link_multi_col3 = [
        [sg.Push(), sg.Text('Fine URL'), sg.Push()],
        [sg.Push(), sg.InputText(key='LINK_multi_posturl', size=(20,5)), sg.Push()]]

    link_progress_frame = [
        [sg.Push()],
        [sg.Push(), sg.Text('Inserire URL progressivo', pad=(0,5)), sg.Push()],
        [sg.Push(), sg.Column(link_multi_col1), sg.Column(link_multi_col2), sg.Column(link_multi_col3), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Frame('Profondità raccolta', link_cover_frame_prog, font='Any 10', pad=(0,5)), sg.Push()],        
        [sg.Push()],
        [sg.Push(), sg.Frame('Ampiezza raccolta', link_type_frame_prog, font='Any 10', pad=(0,5)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='LINK_start_progress_test', pad=(10,15)), sg.Button('Salva CSV', key='LINK_save_progress_csv', pad=(10,15)), sg.Push()],
        [sg.Push()]]

    # LINK TABGROUP
    links_scraper_layout = [
        [sg.Text('', pad=(0,10))],
        [sg.Push()],
        [sg.Push(), sg.Frame('', link_title_layout, pad=(10,20), font='Any 15'), sg.Push()],
        [sg.Push()],
        # Host    
        [sg.Push(), sg.TabGroup([[
        sg.Tab('Singolo URL', link_surl_frame, element_justification= 'center'),
        sg.Tab('URL progressivo', link_progress_frame),
        ]], tab_location='center', size=(600,350)), sg.Push()]
    ]
    
    ## Metatags ##
    meta_title_layout = [
        [sg.Push()],
        [sg.Push(), sg.Text('Estrazione metatags SEO', font='Any 15'), sg.Push()],
        [sg.Push()], 
    ]
    # CARICA CSV
    meta_csv_frame = [
        [sg.Push()],
        [sg.Push(), sg.Text('Selezionare struttura per eventuali campi multi-valore'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Radio('Multi-colonna', 'META_csv_radio', key='META_csv_cols', default=True), sg.Radio('Aggrega valori ( § )', 'META_csv_radio'), sg.Push()],
        [sg.Push()]
    ]

    meta_readcsv_frame = [
        [sg.Push(), sg.Text(''), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Ottieni lista di link da foglio CSV'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.FileBrowse('Carica CSV', initial_folder=directory, key='META_load_file', pad=(0, 10), target='-DIR-'), sg.Push()],
        [sg.In(key='-DIR-', visible=False)],
        [sg.Push(), sg.Frame('Configurazione foglio CSV', meta_csv_frame, font='Any 10', pad=(0,10)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='META_csv_test',  pad=(10,15)), sg.Button('Salva CSV', key='META_csv_save_csv',  pad=(10,15)), sg.Push()],
        [sg.Push()],
    ]

    # METATAGS API
    meta_api_frame = [
        [sg.Push()],
        [sg.Push(), sg.Radio('Multi-colonna', 'META_api_radio', key='META_api_cols', default=True), sg.Radio('Aggrega valori ( § )', 'META_api_radio'), sg.Push()],
        [sg.Push()],
    ]

    meta_readapi_frame = [
        [sg.Push(), sg.Text(''), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Inserire Crawl ID'), sg.Push()],
        [sg.Push(), sg.InputText(key='META_api_host', size=(20,0)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Inserire API Token'), sg.Push()],
        [sg.Push(), sg.InputText(key='META_api_token', size=(40,0)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Frame('Configurazione foglio CSV', meta_api_frame, font='Any 10', pad=(0,15)), sg.Push()],        
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='META_api_test',  pad=(10,10)), sg.Button('Salva CSV', key='META_api_save_csv',  pad=(10,10)), sg.Push()],
        [sg.Push()]
    ]

    # METATAGS TABGROUP
    metatags_scraper_layout = [
        [sg.Text('', pad=(0,10))],
        [sg.Push()],
        [sg.Push(), sg.Frame('', meta_title_layout, pad=(10,20), font='Any 15'), sg.Push()],
        [sg.Push()],
        # Host    
        [sg.Push(), sg.TabGroup([[
        sg.Tab('Carica CSV', meta_readcsv_frame),
        sg.Tab('Archive-it API', meta_readapi_frame,)
        ]], tab_location='center', size=(600,350)), sg.Push()]
    ]
    
    # HTML
    html_col1 = [
        [sg.Push(), sg.Text('Elemento DC'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Title'), sg.Push()],
        [sg.Push(), sg.Text('Creator'), sg.Push()],
        [sg.Push(), sg.Text('Publisher'), sg.Push()],
        [sg.Push(), sg.Text('Contributor'), sg.Push()],
        [sg.Push(), sg.Text('Date'), sg.Push()],
        [sg.Push(), sg.Text('Type'), sg.Push()],
        [sg.Push(), sg.Text('Format'), sg.Push()],
        [sg.Push(), sg.Text('Source'), sg.Push()],
        [sg.Push(), sg.Text('Language'), sg.Push()],
        [sg.Push(), sg.Text('Relation'), sg.Push()],
        [sg.Push(), sg.Text('Coverage'), sg.Push()],
        [sg.Push(), sg.Text('Rights'), sg.Push()],
        [sg.Push(), sg.Text('Description'), sg.Push()],
        [sg.Push(), sg.Text('Subject'), sg.Push()]
    ]

    html_col2 = [
        [sg.Push(), sg.Text('Element HTML'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_title', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_creator', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_pub', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_contr', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_date', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_type', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_format', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_source', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_lang', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_relation', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_cover', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_rights', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_desc', size=(7,7)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_elements, key='HTML_element_sbj', size=(7,7)), sg.Push()]
    ]

    html_col3 = [
        [sg.Push(), sg.Text('Selettore'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_title', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_creator', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_pub', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_contr', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_date', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_type', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_format', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_source', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_lang', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_relation', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_cover', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_rights', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_desc', size=(7,0)), sg.Push()],
        [sg.Push(), sg.Combo(values=html_selectors, key='HTML_selector_sbj', size=(7,0)), sg.Push()]
    ]

    html_col4 = [
        [sg.Push(), sg.Text('Valore'), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_title', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_creator', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_pub', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_contr', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_date', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_type', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_format', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_source', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_lang', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_relation', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_cover', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_rights', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_desc', size=(25, 0)), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_value_sbj', size=(25, 0)), sg.Push()],
    ]

    html_option_col = [
        [sg.Push(), sg.Column(html_col1), sg.Column(html_col2), sg.Column(html_col3), sg.Column(html_col4), sg.Push()]
    ]
    
    # Test
    html_test_frame = [
        [sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Inserire URL pagina di prova'), sg.Push()],
        [sg.Push(), sg.InputText(key='HTML_test_url', size=(70,5)), sg.Push()],
        [sg.Push()]
    ]

    # CSV
    html_csv_frame = [
        [sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Text('Selezionare file CSV'), sg.Push()],
        [sg.Push(), sg.FileBrowse('Carica CSV', initial_folder=directory, key='HTML_load_file', pad=(0, 10), target='DIR'), sg.Push()],
        [sg.In(key='DIR', visible=False)],
        [sg.Push()]
    ]

    # HTML TABGROUP
    html_scraper_layout = [
        [sg.Text('')],
        [sg.Push(), sg.TabGroup([[
        sg.Tab('Test', html_test_frame, element_justification= 'center'),
        sg.Tab('Carica CSV', html_csv_frame),
        ]], tab_location='center', size=(750,100)), sg.Push()],  
        [sg.Push()],
        [sg.Push(), sg.Column(html_option_col, scrollable=True, vertical_scroll_only=True, size=(700, 300)), sg.Push()],
        [sg.Push()],
        [sg.Push(), sg.Button('Test', key='HTML_test',  pad=(10,10)), sg.Button('Salva CSV', key='HTML_save_csv',  pad=(10,10)), sg.Push()],
        [sg.Push()]      
    ]    

    ###################################### Menu ################################################
    link_manuale = 'https://github.com/logo94/Catabot/wiki'
    tabgrp = [
        [sg.Push(), sg.Text('Guida', tooltip=link_manuale, enable_events=True, key='link_manuale')],
        [sg.Push(), sg.TabGroup([[
            sg.Tab('Homepage', homepage_layout, element_justification= 'center'),
            sg.Tab('OAI-PMH', oai_scraper_layout, element_justification= 'center'),
            sg.Tab('Links', links_scraper_layout),
            sg.Tab('Metatags', metatags_scraper_layout),
            sg.Tab('HTML', html_scraper_layout,)
        ]], tab_location='center', size=(750,540)), sg.Push(),],
        # Finestra di test
        [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0,0))],
        [sg.Push(), sg.Output(size=(120,15), key='output'), sg.Push()],
        [sg.Push()]
        ]  
        
    # Creazione finestra
    window = sg.Window('CataBot', tabgrp, resizable=True, finalize=True, size=(850,900), font='Any 12')    
    window['-EXPAND-'].expand(True, True, True)


    ###################################### Scripts ##############################################
    while True:
    
        event, values = window.read() 

        # Chiusura finestra
        if event in (sg.WIN_CLOSED, 'Exit'):
            break  

        # Manuale
        if event in ['link_manuale', 'home_manuale']:
            webbrowser.open(link_manuale)

        ## OAI
        # Test
        if event == 'OAI_start_test':
            window['output'].update('Operazione in corso...')
            window.perform_long_operation(lambda : test_oai(values['OAI_endpoint']), 'OAI_test_done')
        if event == 'OAI_test_done':
            window['output'].update('Sono stati trovati ' + str(oai_count(values['OAI_endpoint'])) + ' record\n\nEsempio di record:\n\n' + values['OAI_test_done'] + '\n\nINFO: eventuali errori di codifica verranno corretti automaticamente durante la scrittura del foglio CSV')        
        # CSV
        if event == 'OAI_save_csv':
            window['output'].update('Le tempistiche per il termine del processo possono dipendere da fattori come la velocità della connessione, la grandezza del sito e prestazioni del web server che le ospita \n\nOperazione in corso...')
            if values['OAI_cols'] == True:
                window.perform_long_operation(lambda : csv_multi_oai(values['OAI_endpoint']), 'OAI_csv_done')
            elif values['OAI_cols'] == False:
                window.perform_long_operation(lambda : csv_aggr_oai(values['OAI_endpoint']), 'OAI_csv_done')
        if event == 'OAI_csv_done':
            window['output'].update(values['OAI_csv_done']) 
        

        ## LINK
        # Test
        # Single page
        if event == 'LINK_start_surl_test':
            window['output'].update('')
            if values['LINK_surl_host']:
                url = values['LINK_surl_host']
                if values['LINK_surl_all'] == True:
                    link_range = 'all'
                elif values['LINK_surl_internal'] == True:
                    link_range = 'internal'
                if values['LINK_single_page'] == True:
                    print(test_surl_link(url, link_range))
                elif values['LINK_page_1'] == True:
                    fastest_surl_links(url, link_range)
        # URL progressivo
        if event == 'LINK_start_progress_test':
            window['output'].update('')
            if values['LINK_progr_all'] == True:
                link_range = 'all'
            elif values['LINK_progr_internal'] == True:
                link_range = 'internal'
            if values['LINK_progress_page'] == True:
                print(test_progress_link(values['LINK_multi_preurl'], values['LINK_multi_from'], values['LINK_multi_to'], values['LINK_multi_posturl'], link_range))
            elif values['LINK_progress_page_1'] == True:
                fastest_progress_links(values['LINK_multi_preurl'], values['LINK_multi_from'], values['LINK_multi_to'], values['LINK_multi_posturl'], link_range)
        # CSV
        if event == 'LINK_save_surl_csv':
            window['output'].update('Operazione in corso...')
            if values['LINK_surl_all'] == True:
                link_csv_range = 'all'
            elif values['LINK_surl_internal'] == True:
                link_csv_range = 'internal'
            if values['LINK_single_page'] == True:
                link_cover = 'one_page'
            elif values['LINK_page_1'] == True:
                link_cover = 'deep'
            window.perform_long_operation(lambda : link_surl_csv(values['LINK_surl_host'], link_cover, link_csv_range), 'LINK_surl_csv_done') 
        if event == 'LINK_surl_csv_done':
            window['output'].update(values['LINK_surl_csv_done']) 

        if event == 'LINK_save_progress_csv':
            window['output'].update('Operazione in corso...')
            if values['LINK_progr_all'] == True:
                link_p_csv_range = 'all'
            elif values['LINK_progr_internal'] == True:
                link_p_csv_range = 'internal'
            if values['LINK_progress_page'] == True:
                link_p_cover = 'one_page'
            elif values['LINK_progress_page_1'] == True:
                link_p_cover = 'deep'
            window.perform_long_operation(lambda : link_progress_csv(values['LINK_multi_preurl'], values['LINK_multi_from'], values['LINK_multi_to'], values['LINK_multi_posturl'], link_p_cover, link_p_csv_range), 'LINK_progr_csv_done') 
        if event == 'LINK_progr_csv_done':
            window['output'].update(values['LINK_progr_csv_done'])   

        ### METATAGS ###

        ## READ CSV ##
        # Test
        if event == 'META_csv_test':
            window['output'].update('Aperture del file CSV in corso...')
            meta_read_test_csv(values['META_load_file'])
        if event == 'META_csv_save_csv':
            if values['META_csv_cols'] == True:
                meta_readcsv_style = 'multi'
            if values['META_csv_cols'] == False:
                meta_readcsv_style = 'single'
            window['output'].update('Lettura del file in corso...')
            window.perform_long_operation(lambda : meta_read_save_csv(values['META_load_file'], meta_readcsv_style), 'META_csv_test_obj')
        if event == 'META_csv_test_obj':
            window['output'].update(values['META_csv_test_obj'])
        ## API ##
        # Test
        if event == 'META_api_test':
            window['output'].update('Interrogazione API in corso...')
            window.perform_long_operation(lambda : archive_api_test(values['META_api_host'], values['META_api_token']), 'META_api_test_obj')
        if event == 'META_api_test_obj':
            window['output'].update(values['META_api_test_obj'])
        # CSV
        if event == 'META_api_save_csv':
            if values['META_api_cols'] == True:
                meta_api_style = 'multi'
            if values['META_api_cols'] == False:
                meta_api_style = 'single'
            window['output'].update('Interrogazione API in corso...')
            window.perform_long_operation(lambda : archive_api_csv(values['META_api_host'], values['META_api_token'], meta_api_style), 'META_api_write_csv')
        if event == 'META_api_write_csv':
            window['output'].update(values['META_api_write_csv'])

        ### HTML ###
        # Test
        if event == 'HTML_test':
            window['output'].update('Esempio di risultato:\n\n')
            html_test(values['HTML_test_url'], 'test',
                      values['HTML_element_title'], values['HTML_selector_title'], values['HTML_value_title'],
                      values['HTML_element_creator'], values['HTML_selector_creator'], values['HTML_value_creator'],
                      values['HTML_element_pub'], values['HTML_selector_pub'], values['HTML_value_pub'],
                      values['HTML_element_contr'], values['HTML_selector_contr'], values['HTML_value_contr'],
                      values['HTML_element_date'], values['HTML_selector_date'], values['HTML_value_date'],
                      values['HTML_element_type'], values['HTML_selector_type'], values['HTML_value_type'],
                      values['HTML_element_format'], values['HTML_selector_format'], values['HTML_value_format'],
                      values['HTML_element_source'], values['HTML_selector_source'], values['HTML_value_source'],
                      values['HTML_element_lang'], values['HTML_selector_lang'], values['HTML_value_lang'],
                      values['HTML_element_relation'], values['HTML_selector_relation'], values['HTML_value_relation'],
                      values['HTML_element_cover'], values['HTML_selector_cover'], values['HTML_value_cover'],
                      values['HTML_element_rights'], values['HTML_selector_rights'], values['HTML_value_rights'],
                      values['HTML_element_desc'], values['HTML_selector_desc'], values['HTML_value_desc'],
                      values['HTML_element_sbj'], values['HTML_selector_sbj'], values['HTML_value_sbj'],
                      )
        if event == 'HTML_save_csv':
            window['output'].update('Operazione in corso...')
            window.perform_long_operation(lambda: html_csv(values['HTML_load_file'], 'csv',
                      values['HTML_element_title'], values['HTML_selector_title'], values['HTML_value_title'],
                      values['HTML_element_creator'], values['HTML_selector_creator'], values['HTML_value_creator'],
                      values['HTML_element_pub'], values['HTML_selector_pub'], values['HTML_value_pub'],
                      values['HTML_element_contr'], values['HTML_selector_contr'], values['HTML_value_contr'],
                      values['HTML_element_date'], values['HTML_selector_date'], values['HTML_value_date'],
                      values['HTML_element_type'], values['HTML_selector_type'], values['HTML_value_type'],
                      values['HTML_element_format'], values['HTML_selector_format'], values['HTML_value_format'],
                      values['HTML_element_source'], values['HTML_selector_source'], values['HTML_value_source'],
                      values['HTML_element_lang'], values['HTML_selector_lang'], values['HTML_value_lang'],
                      values['HTML_element_relation'], values['HTML_selector_relation'], values['HTML_value_relation'],
                      values['HTML_element_cover'], values['HTML_selector_cover'], values['HTML_value_cover'],
                      values['HTML_element_rights'], values['HTML_selector_rights'], values['HTML_value_rights'],
                      values['HTML_element_desc'], values['HTML_selector_desc'], values['HTML_value_desc'],
                      values['HTML_element_sbj'], values['HTML_selector_sbj'], values['HTML_value_sbj'],
                      ), 'HTML_csv_saved')
        if event == 'HTML_csv_saved':
            window['output'].update(values['HTML_csv_saved'])
            
    window.close()

if __name__ == '__main__':
    main()
