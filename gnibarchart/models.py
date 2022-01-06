from django.db import models
# from django.db import connections

class IndicatorData(models.Model):
    YEAR_CHOICES = (
        ('YR2000', '2000'),
        ('YR2002', '2002'),
        ('YR2004', '2004'),
        ('YR2006', '2006'),
        ('YR2008', '2008'),
        ('YR2010', '2010'),
        ('YR2012', '2012'),
        ('YR2014', '2014'),
        ('YR2016', '2016'),
        ('YR2018', '2018'),
      )
    
    INDIC_CHOICES = (
    ('SP.DYN.TFRT.IN','Total Fertility Rate'),
    )
    year = models.CharField(max_length=50, choices = YEAR_CHOICES)
    indicator = models.CharField(max_length=50, choices = INDIC_CHOICES)
  
    #     return f'{self.indicator}'