class Product:
    """
    Атрибут name - название продукта (строка).
    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    Атрибут category - категория товара (строка)
    """
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """
        Метод __str__ возвращает строку в формате '<название>, <вес>, <категория>'.
        Все данные в строке разделены запятой с пробелами.
        """
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    """
    Инкапсулированный атрибут __file_name = 'products.txt'
    """
    def __init__(self):
        self.__file_name = 'module_7_1/products.txt'

    def get_products(self):
        """
        Метод get_products(self) считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        """
        self.__file_name = 'module_7_1/products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()

        return products

    def add(self, *products):
        """
        Метод add(self, *products) принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
        """
        for prod in products:
            if prod.name and str(prod.weight) not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(prod.__str__() + '\n')

            else:
                print(f'Продукт {prod.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())