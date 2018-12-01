import csv
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
csv.field_size_limit(sys.maxsize)
analyzer = SentimentIntensityAnalyzer()
data_path = "scraping/output_clean.csv"
years_scores = {2009: 0, 2010: 0, 2011:0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0}
years_freq = {2009: 0, 2010: 0, 2011:0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0}
idx = 0
score_idx = {}
f = open("output_scored.csv", 'w')
with open(data_path) as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		link = row[2]
		year = link.split('/')
		if len(year) > 3: 
			year = int(year[3])
		else:
			idx += 1
			continue
		# type_a = row[0]
		# if type_a != "editorials":
		# 	continue
		text = row[3]
		vs = analyzer.polarity_scores(text)
		years_scores[year] = vs['compound'] + years_scores.get(year)
		years_freq[year] = 1 + years_freq.get(year)
		exists = score_idx.get(vs['compound'], [])
		exists.append(idx)
		score_idx[vs['compound']] = exists
		f.write(str(idx)+','+row[0] +','+row[1]+','+row[2]+','+row[3]+','+str(vs['compound']) + '\n')
		idx += 1
		print(idx)
f.close()
for year, freq in years_freq.items():
	print(year, freq, years_scores[year])
	score = years_scores[year]/freq
	years_scores[year] = score

print(years_scores)


'''
OUTPUT:
2009 252 104.95949999999995
2010 369 228.95990000000012
2011 376 171.4242999999997
2012 396 179.424
2013 362 192.2844000000001
2014 337 161.29200000000006
2015 301 111.65760000000003
2016 294 198.50719999999998
2017 255 158.76030000000003
2018 238 157.69630000000006
{2009: 0.41650595238095217, 
2010: 0.6204875338753391, 
2011: 0.4559156914893609, 
2012: 0.4530909090909091, 
2013: 0.5311723756906079, 
2014: 0.47861127596439185, 
2015: 0.37095548172757487, 
2016: 0.6751945578231292, 
2017: 0.622589411764706, 
2018: 0.6625894957983196}
'''




