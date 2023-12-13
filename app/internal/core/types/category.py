from enum import Enum


class ProductCategoryEnum(str, Enum):
    """Категории продуктов

    TECH: Бытовая техника
    BEAUTY: Красота и здоровье
    SMART: Смартфоны и техника
    PC: Пк, ноутбуки и периферия
    """

    TECH = 'tech'
    BEAUTY = 'beauty'
    SMART = 'smart'
    PC = 'pc'
