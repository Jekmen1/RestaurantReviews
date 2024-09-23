from django.db import models
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Review(models.Model):
    restaurant_name = models.CharField(max_length=100)
    review_text = models.TextField()
    sentiment_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def analyze_sentiment(self):
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(self.review_text)
        self.sentiment_score = sentiment['compound']
        self.save()

    def __str__(self):
        return self.restaurant_name
