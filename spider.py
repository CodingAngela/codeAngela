import requests
from lxml import etree
HEADERS={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0)'
                 ' Gecko/20100101'
                 'Firefox/63.0'
}
BASE_DOMAIN="http://www.dytt8.net"

def get_detail_url(url):
    response=requests.get(url, headers=HEADERS)  # print(response.content.decode('gbk')
    text=response.text.encode("utf-8")  # 拿到数据，，再解码
    html=etree.HTML(text)
    detail_urls=html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls=map(lambda url:BASE_DOMAIN+url,detail_urls)   #构建url
    return detail_urls

def parse_detail_page(url):
    movie={}
    response=requests.get(url, headers=HEADERS)
    text=response.content.decode('gbk')  # text=response.text.encode("utf-8")
    html=etree.HTML(text)
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0] #索引
    movie['title']=title  #电影名称
    Zoome=html.xpath("//div[@id='Zoom']")[0]  # return list
    imgs=Zoome.xpath(".//img/@src")
    # print(cover)
    cover=imgs[0]
    movie['cover']=cover  #电影海报

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos=Zoome.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info=parse_info(info,"◎年　　代")
            # print(info)
            movie['year']=info
        elif info.startswith("◎产　　地"):
            info=parse_info(info,"◎产　　地")
            movie['country']=info
        elif info.startswith("◎类　　别"):
            info=parse_info(info,"◎类　　别")
            movie['category']=info
        elif info.startswith("◎语　　言"):
            info=parse_info(info,"◎语　　言")
            movie['language']=info
        elif info.startswith("◎字　　幕"):
            info=parse_info(info,"◎字　　幕")
            movie['sub_title']=info
        elif info.startswith("◎上映日期"):
            info=parse_info(info,"◎上映日期")
            movie['release_time']=info
        elif info.startswith("◎豆瓣评分"):
            info=parse_info(info,"◎豆瓣评分")
            movie['douban_score']=info
        elif info.startswith("◎片　　长"):
            info=parse_info(info,"◎片　　长")
            movie['length']=info
        elif info.startswith("◎导　　演"):
            info=parse_info(info,"◎导　　演")
            movie['director']=info
        elif info.startswith("◎主　　演"):
            info=parse_info(info,"◎主　　演")
            actors=[info]
            for x in range(index + 1, len(infos)):
                actor=infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors']=actors    #早知道不爬主演了......
        elif info.startswith("◎简　　介"):
            info=parse_info(info,"◎简　　介")
            profiles=[info]
            for x in range(index + 1, len(infos)):
                profile=infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                profiles.append(profile)
                movie['profiles']=profiles
    download_url=html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    # print(download_url)
    movie['download_url']=download_url  #感觉爬这个比较关键
    return movie

movies=[]
def spider():
    base_url='http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1, 2):  # how much page depend on you
        # print(x)
        url=base_url.format(x)
        detail_urls=get_detail_url(url)
        for detail_url in detail_urls:
            # print(detail_url)
            movie=parse_detail_page(detail_url)
            movies.append(movie)

if __name__=='__main__':
    spider()
    with open(r'D:\爬到的movies.txt','a',encoding='utf-8')as f:
        for movie in movies:
            f.write("="*30)
            f.write('\n'*2)
            for (key,value) in movie.items():
                if (key=='actors'):
                    str='actors:{}'
                    f.write(str.format(value))
                    f.write('\n')
                elif (key=='profiles'):
                    str='profiles:{}'
                    f.write(str.format(value))
                    f.write('\n')
                else:
                    f.write(key+":"+value)
                    f.write('\n')
            f.write('\n'*3)requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html=etree.HTML(text)
    title=html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")
    #print(title)
    movie['title'] = title
    Zoome = html.xpath("//div[@id='Zoom']")  # 返回的是列表
    imgs = Zoome.xpath(".//img/@src")
    cover = imgs[0]
    # print(cover)
    movie['cover'] = cover

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    infos = Zoome.xpath(".//text()")
    # print(infos)
    for index, info in enumerate(infos):
        if info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_score'] = info
        if info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            profiles = [info]
            movie['profiles'] = profiles
    return movie

movies=[]
def spider():
     base_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
     for x in range(1,2):  #页数可改动
         # print(x)
         url=base_url.format(x)
         detail_urls=get_detail_url(url)
         for detail_url in detail_urls:
             # print(detail_url)
             movie=parse_detail_page(detail_url)
             movies.append(movie)

if __name__ == '__main__':
    spider()
    with open('movies.txt', 'a', encoding='utf-8') as f:
        for movie in movies:
            f.write("=" * 30)
            f.write('\n' * 2)
            for (key, value) in movie.items():
                if (key =='profiles'):
                    str = 'profiles :{}'
                    f.write(str.format(value))
                    f.write('\n')
            f.write('\n' * 3)
