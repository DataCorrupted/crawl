# Made by Peter Rong
# PeterRong96@gmail.com

# In case this code don't work, do the following in your terminal:
#
#   pip install tqdm
#   pip install requests
#   pip install random_useragent
#

from zipcodes import l
import time
import requests
from tqdm import tqdm
from random_useragent.random_useragent import Randomize
import random

r_agent = Randomize()
prefix = "https://www.redfin.com"

for zipcode in tqdm(sorted(l)):
	# Setup agent and timer for each iteration
    zipcode_str = str(zipcode).zfill(5)
    ua = r_agent.random_agent('desktop','windows')

    # Get webpage
    address = prefix + "/zipcode/" + zipcode_str
    res = requests.get(address, headers={'User-Agent': ua}).content
    time.sleep(1 + random.uniform(1, 3))

    # Parse webpage and get csv address
    webpage = str(res)
    end = webpage.find('" class="downloadLink"')
    begin = webpage.find('/stingray/api/gis-csv?')
    csv_address = prefix + webpage[begin: end]
    csv_address = csv_address.replace('\n', '').replace('&amp', '').replace(';', '&')

    # Download csv
    res = requests.get(csv_address, headers={'User-Agent': ua}).content
    time.sleep(3 + random.uniform(1, 3))

    # Output to file
    csv_name = 'a' + zipcode_str + '.csv'
    with open('csv/' + csv_name, 'wb') as f:
        f.write(res)