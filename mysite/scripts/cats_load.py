import csv
# import Cat and Breed model
from cats.models import Cat, Breed

# python manage.py runscript cats_load

def run():
    fhand = open("cats/meow.csv")
    reader = csv.reader(fhand)
    next(reader)

    # Delete old content from db
    Cat.objects.all().delete()
    Breed.objects.all().delete()

    # Name,Breed,Weight
    # Abby,Sphinx,6.4
    # Annie,Burmese,7.6

    for row in reader:
        print(row)
        b, created = Breed.objects.get_or_create(name=row[1])

        c = Cat(nickname=row[0], breed=b, weight=row[2], foods="food")
        c.save()
