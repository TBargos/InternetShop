from django.db import models


class Categories(models.Model):
    # поле id прописывать не нужно, оно создаётся автоматически
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    # переопределение метода для понятного отображения инфы по новым объектам в бд (для админки)
    def __str__(self) -> str:  # вообще этот метод возвращает инфу по экземпляру класса
        return self.name

    class Meta:     # Ручная корректировка миграции
        db_table = 'category'   # имя таблицы
        # имена для админ панели
        verbose_name = 'Категорию' # в единственном числеч
        verbose_name_plural = 'Категории' # во множественном числе


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'