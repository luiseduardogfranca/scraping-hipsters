# from database import Database
import requests 
import json
import re 

class ResquestsHipsters: 
    def get_podcasts_by_page(self, req, number_page):

        def exists_tag(arr_options, get_text):
            def _(tag):
                if get_text('a', tag)[0] in arr_options:
                    return True 
                else:
                    return False
            return _
        
        get_text_tag = lambda tag, html: re.findall('<{}.*>(.+)</{}>'.format(tag, tag), html)
        get_links = lambda tag, html: re.findall('<{}.*>.*</{}>'.format(tag, tag), html)
        
        page_html = req.get('https://hipsters.tech/page/{}'.format(number_page)).text
        title_podcasts = get_text_tag('option', page_html)

        podcasts = set(filter(exists_tag(arr_options=title_podcasts, get_text=get_text_tag), get_links('a', page_html)))

        return list(podcasts) 

     
    def mount_dictionary(self, arr_tag):
        get_text_tag = lambda tag, html: re.findall('<{}.*>(.+)</{}>'.format(tag, tag), html)
        get_url_tag = lambda tag, html: re.findall('<{} href="(.+)">.+</{}>'.format(tag, tag), html)

        dic = {}

        for index in range(len(arr_tag)):
            title = ''.join(get_text_tag('a', arr_tag[index]))
            url = ''.join(get_url_tag('a', arr_tag[index]))

            dic[index] = {'title':title, 'url-page':url}
        
        return dic

    def get_src_podcast(self, url_page):
    
        link_pod = lambda tag, html: re.findall('<\s*{} href="([^\s]*)" [^>]*>Baixar</\s*{}>'.format(tag, tag), html)

        html = requests.get(url).text 
        return link_pod('a', html)
    
    def get_amount_page(self, req, url_home):
        page_html = req.get('https://hipsters.tech/').text
        number_page = lambda html: max([int(value) for value in re.findall('page/(.)', html) if value.isdigit()])
        return number_page(page_html)


r = ResquestsHipsters()
# dic_podcasts = r.mount_dictionary(r.get_podcasts_by_page(requests, 2    ))

# for podcast in dic_podcasts:
#     url = dic_podcasts.get(podcast).get('url-page') 
#     dic_podcasts[podcast]['src'] = r.get_src_podcast(url)


# with open('podcasts-page2.json', 'w') as fp:
#     json.dump(dic_podcasts, fp, indent=4)
print(r.get_amount_page(requests, 'https://hipsters.tech/'))