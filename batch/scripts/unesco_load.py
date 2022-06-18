import csv

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, ISO, Site


def run():
    fhand = open("unesco/whc-sites-2018-clean.csv")
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude,
    # area_hectares, category, state, region, iso

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = ISO.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            h = float(row[6])
        except:
            h = None

        site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=row[4], latitude=row[5], area_hectares=h, category=c, state=s, region=r, iso=i)

        site.save()
