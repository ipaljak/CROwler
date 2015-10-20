# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class Comment(Item):
    
    # user specific fields 
    user        = Field() 
    user_rating = Field()
    post_count  = Field()
    
    # post specific fields 
    text        = Field() 
    thumbs      = Field() # [up, down] 
    quotes_user = Field() 
    quoted_text = Field()
