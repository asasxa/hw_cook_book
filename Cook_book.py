class Ingredient:
    def __init__(self, name, quantity, measure):
        self.ingredient_name = name
        self.quantity = quantity
        self.measure = measure


def read_recipes_from_file(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            ingredients_number = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_number):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient = Ingredient(
                    name=ingredient_name.strip(),
                    quantity=float(quantity.strip()),  # Приведение к числу с плавающей точкой
                    measure=measure.strip()
                )
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


def main():
    file_path = 'recipes.txt'
    cook_book = read_recipes_from_file(file_path)

    for dish, ingredients in cook_book.items():
        print(dish)
        for item in ingredients:
            print(f"  ingredient_name: {item.ingredient_name}, quantity: {item.quantity}, measure: {item.measure}")
        print()


if __name__ == "__main__":
    main()

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            name = ingredient.ingredient_name
            if name not in shop_list:
                shop_list[name] = {'measure': ingredient.measure, 'quantity': ingredient.quantity * person_count}
            else:
                shop_list[name]['quantity'] += ingredient.quantity * person_count
    return shop_list

file_path = 'recipes.txt'
cook_book = read_recipes_from_file(file_path)

dishes = ['Запеченный картофель', 'Омлет', 'Салат "Цезарь"', 'Запеченный картофель']
person_count = 8
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)