from yahoo_finance import Share
import json
import os

def get_title(title, cache=True):
    return_dic = {}
    
    # if cache == True, try to open the cached file
    if cache:
        cached_filename = 'cache/finance_{0}.json'.format(title)
        
        if os.path.exists(cached_filename):
            with open(cached_filename) as f:
                items = json.loads(f.read())
            return items
        
            
    # if cache == False, or the cached file does not exist, call the API
    try:
        
        t = Share(title)
    
        return_dic["symbol"] = title
        return_dic["price"] = t.get_price()
        return_dic["change"] = t.get_change()
        return_dic["name"] = t.data_set["Name"]
    
    except:
        return_dic["symbol"] = title
        return_dic["price"] = 0
        return_dic["change"] = 0
        return_dic["name"] = title
    
    
    # if cache == True but we are down here, it means that the cached file does not exist, so create it
    if cache:
        with open(cached_filename, 'w') as f:
            json.dump(return_dic, f)
            
    
    return return_dic
    
