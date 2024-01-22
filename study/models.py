from django.db import models

# Create your models here.


class Abstract(models.Model):
    LABEL_CHOICES = [
        ("RCT", "RCT"),
        ("Meta-Analysis", "Meta-Analysis"),
        ("Unknown", "Unknown"),
    ]

    date = models.CharField(max_length=15)
    doi = models.CharField(max_length=50)
    pmid = models.SlugField(unique=True, db_index=True, max_length=8)
    label = models.CharField(max_length=15, choices=LABEL_CHOICES, default="Unknown")
    title = models.TextField()
    authors = models.TextField()
    author_info = models.TextField()
    abstract = models.TextField()
    background = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    conclusions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pmid
