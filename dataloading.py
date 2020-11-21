'''
placeholder for loading the data from SQL into memory on deployment


'''
import pandas as pd
import urllib.request, json 

def data_downloader(name, url):
    '''
    Pass in a URL and download the dataframe, save to disk
    '''
    # download the json
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode())
    
    # save the json to disk
    filename = f'data/{name}.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
    
    print(f'Saved {name} to Disk')
    
def download_bulk():
    '''
    Script to download all jsons to disk 
    
    TODO: add some kind of loading bar to show percentage of downloaded
    '''
    import dataloading
    import city_of_london_api_endpoints as col
    
    return [dataloading.data_downloader(i, col.EVERYTHING.get(i)) for i in list(col.EVERYTHING.keys())]