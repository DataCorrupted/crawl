# Crawl

This is a simple crwal for Zhihao's project. It will auto download csv files for all the housing information from [redfin.com](redfin.com)

## Dependencies

Using Python 3 with the following packages support.

	pip install tqdm
	pip install requests
	pip install random_useragent


## Folders

### csv

All the crawled file goes here. A _.keep_ file is kept to make sure this folder stays alive.

### src 

Source code is put here. In _zipcodes.py_ all the zipcodes that need to be crawled is collected as a list. In case you want to change zipcodes, change this file.

This crawl will stop for 2~4 seconds each time after the connecting is established to _redfin.com_ to prevent been banned.(Got it once, escaped it using this stop timer)

All the files have been tested and it's working.

## Usage

Enter root folder. Issue command:

	python src/craw.py

All the files will be crawed automatically. 

There are 1283 files for now, which would take approx. 3 hrs. Most time is spent sleeping after each connection. 

You can change timer in _craw.py_ so that you can run faster, but be aware the possibility of been banned. It not recommended that you set the timer less than 1 second for each connnection.

## Notice

This util is young and naive. You should not use it as any commerical tools. **DO NOT** count on it to be robust. It works, that's all.

## Contact

Peter Rong / Yuyang Rong

+1 310 307 9952   /   +86 177 2105 4096

PeterRong96@gmail.com   /   rongyy@ShanghaiTech.edu.cn
