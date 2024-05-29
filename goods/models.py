from django.db import models


class Categories(models.Model):
    # поле id прописывать не нужно, оно создаётся автоматически
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    # переопределение метода для понятного отображения инфы по новым объектам в бд (для админки)
    def __str__(self) -> str:  # этот метод возвращает инфу по экземпляру класса
        return self.name

    class Meta:     # Ручная корректировка миграции
        db_table: str = 'category'   # имя таблицы
        # имена для админ панели
        verbose_name: str = 'Категорию' # в единственном числе
        verbose_name_plural: str = 'Категории' # во множественном числе


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
    
    def display_id(self) -> str:
        return f'{self.id:05}'

    def sell_price(self) -> int | float:
        if self.discount:
            return round(self.price - self.price*(self.discount/100), 2)
        
        return self.price

    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = 'Продукты'
        ordering = ("id",) # Сортировка выдачи по умолчанию, нужна для пагинации