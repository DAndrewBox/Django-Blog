from django.db import models

class Post(models.Model):
    post_title  = models.CharField(max_length=64)
    post_date   = models.DateTimeField()
    post_image  = models.ImageField(upload_to='media/')
    post_body   = models.TextField()

    def __str__(self):
        return self.post_title

    def get_post_date_pretty(self):
        date = self.post_date.strftime('%B %d') + ", "
        date += self.post_date.strftime('%Y') 

        return date

    def get_post_body_summary(self):
        body_words_split = self.post_body.split(" ")
        body_words = ""

        for i in range(min(len(body_words_split), 25)):
            body_words += body_words_split[i] + " "

        return (body_words + "...")
