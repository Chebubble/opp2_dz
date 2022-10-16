cook_book = {}

with open('recipes.txt', 'rt', encoding='utf8') as file:
    for l in file:
        cook_name = l.strip()
        cook_ingredients = []
        #прочесть количество:
        amount_count = file.readline()
        #цикл, чтобы узнать точное количество ингредиантов:
        for i in range(int(amount_count)):
            #прочел всю строку:
            amount = file.readline()
            #чтобы отделить от знака |:
            ingredient_name, quantity, measure = amount.strip().split('|')
            cook_ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book.update({cook_name: cook_ingredients})

print(cook_book)
 

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
      if dish in cook_book.keys():
        for ing in cook_book[dish]:
          sum = int(ing['quantity']) * person_count
          shop_list.update({ing['ingredient_name']: {'measure': ing['measure'], 'quantity': sum}})
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ing in cook_book[dish]:
                sum_1 = int(ing['quantity']) * person_count
                shop_list.update({ing['ingredient_name']: {'measure': ing['measure'], 'quantity': sum_1}})
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def number_of_lines(*files):
  lines = {}
  for file in files:
      with open(file, 'rt', encoding='utf8') as f:
        result = f.readlines()
        res = (len(result))
        lines.update({file: res})
  lines_2 = {}
  for i in sorted(lines, key=lines.get):
      lines_2[i] = lines[i]
  return lines_2

def writing_file(*files):
    text_dict = {}
    for i in number_of_lines(*files):
        with open(i, encoding='utf-8') as file_obj:
            f = file_obj.read()
            text_dict.update({i: f})
    for key, value in text_dict.items():
        with open('files/new.txt', 'a', encoding='utf-8') as file:
            file.writelines([f"{key}\n{number_of_lines(*files)[key]}\n{value}\n"])

writing_file('files/1.txt', 'files/2.txt', 'files/3.txt')
