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



