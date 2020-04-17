from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

# Initialize objects
tokenizer = RegexpTokenizer(r'\w+') # expression for extracting all the words
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()

def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    # Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    return cleaned_review

# write one function that accepts input file and returns clean output file of the movie review

def getStemmedDocument(inputfile,outputfile):

	out = open(outputfile,'w',encoding='utf-8')

	with open(inputfile,encoding='utf-8') as f:
		reviews = f.readlines()
	for review in reviews:
		cleaned_review = getStemmedReview(review)
		print((cleaned_review),file=out)
	out.close()

# Read command line arguements
inputfile = sys.argv[1]
outputfile = sys.argv[2]
getStemmedDocument(inputfile,outputfile)