from django.db import models

# Create your models here.


class Material(models.Model):
    Name = models.CharField(verbose_name='Название материала', max_length=50, unique=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class TableFurniture(models.Model):
    Name = models.CharField(verbose_name='Название стола', max_length=50)
    Description = models.TextField(verbose_name='Описание', null=True)
    Characteristics = models.TextField(verbose_name='Характеристики')
    Price = models.FloatField(verbose_name='Цена')
    Material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    Height = models.FloatField(verbose_name='Высота', default=0)
    Width = models.FloatField(verbose_name='Ширина', default=0)
    Depth = models.FloatField(verbose_name='Глубина', default=0)
    In_stock = models.BooleanField(verbose_name='В наличии', default=False)
    Image = models.ImageField(verbose_name='Изображение стола', upload_to='TableSite/static/mainsite/img', null=True)

    def __str__(self):
        return f'{self.Name} {self.Width} x {self.Depth} x {self.Height}. Цена: {self.Price}'

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

