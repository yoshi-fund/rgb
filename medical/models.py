from django.db import models
from django.utils import timezone
class Medical(models.Model):
    
    CONDITION = (
        (1, '良い'),
        (2, '悪い')
    )
    
    image = models.ImageField('うんちの画像', upload_to='shit', null=True, blank=True)
    r = models.IntegerField('R', null=True, blank=True)
    g = models.IntegerField('G', null=True, blank=True)
    b = models.IntegerField('B', null=True, blank=True)
    condition = models.CharField('コンディション', null=True, blank=True, max_length=100, editable=False)
#    condition = models.IntegerField('コンディション', choices=CONDITION, null=True, blank=True)
    date = models.DateTimeField('投稿日', editable=False, default=timezone.now)
    
    class Meta:
        db_table = 'poop'
    
    def __str__(self):
        return f'ID[{self.id}] --> R : {self.r} | G : {self.g} | B : {self.b}'
# Create your models here.
