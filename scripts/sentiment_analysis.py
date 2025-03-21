import sys
import json
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('punkt')
    nltk.download('vader_lexicon')
    nltk.download('stopwords')

def analyze_sentiment(text):
    # TextBlob analysis
    blob = TextBlob(text)
    textblob_polarity = blob.sentiment.polarity
    textblob_subjectivity = blob.sentiment.subjectivity
    
    # VADER analysis
    sia = SentimentIntensityAnalyzer()
    vader_scores = sia.polarity_scores(text)
    
    # Tokenization and basic text stats
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in tokens if word.isalnum()]
    meaningful_words = [word for word in words if word not in stop_words]
    
    result = {
        'textblob': {
            'polarity': textblob_polarity,
            'subjectivity': textblob_subjectivity
        },
        'vader': vader_scores,
        'stats': {
            'total_words': len(words),
            'meaningful_words': len(meaningful_words)
        }
    }
    
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'No text provided'}))
        sys.exit(1)
        
    input_text = sys.argv[1]
    analysis_result = analyze_sentiment(input_text)
    print(json.dumps(analysis_result)) 