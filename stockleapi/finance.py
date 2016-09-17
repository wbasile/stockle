from yahoo_finance import Share

def get_title(title):
    t = Share(title)
    
    return_dic = {}
    
    return_dic["symbol"] = title
    return_dic["price"] = t.get_price()
    return_dic["change"] = t.get_change()
    return_dic["name"] = t.data_set["Name"]
    
    return return_dic
