# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pywikibot.data import api
import pywikibot
site = pywikibot.Site('wikidata','wikidata')

#print(site)
def getItems(site, itemtitle):
    params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
    request = api.Request(site=site,**params)
    return request.submit()

item = pywikibot.ItemPage(site, 'Q154950')

item_2 = getItems(site, "Royal Dutch Shell")
item_dict = item.get()


print(item_dict['aliases']['en'])
#print(item_2)