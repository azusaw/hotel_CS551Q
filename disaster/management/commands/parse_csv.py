import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from disaster.models import Disaster, Continent, Region, Type


def convert_blank(value):
    return None if value == '' else value


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # Delete data from tables to avoid duplicate values when the file is rerun
        Disaster.objects.all().delete()
        Continent.objects.all().delete()
        Region.objects.all().delete()
        Type.objects.all().delete()
        print("table dropped successfully")

        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(str(base_dir) + '/data/1970-2021_DISASTERS.csv', newline='', encoding='latin-1') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)

            disasters = []
            continents = set()
            regions = set()
            types = set()

            for row in reader:
                continent = row[11]
                region = row[10]
                type = row[5]

                # Add data to the relevant collection
                continents.add(Continent(id=continent))
                regions.add(Region(id=region, continent_id=continent))
                types.add(Type(id=type))

                # Creating Disaster model objects
                disaster = Disaster(
                    disasterNo=(row[0]),
                    year=row[1],
                    seq=row[2],
                    group=row[3],
                    subgroup=row[4],
                    type_id=type,
                    subtype=row[6],
                    eventName=row[7],
                    country=row[8],
                    iso=row[9],
                    region_id=region,
                    continent_id=continent,
                    location=row[12],
                    startYear=convert_blank(row[13]),
                    startMonth=convert_blank(row[14]),
                    startDay=convert_blank(row[15]),
                    endYear=convert_blank(row[16]),
                    endMonth=convert_blank(row[17]),
                    endDay=convert_blank(row[18]),
                    totalDeaths=convert_blank(row[19]),
                    injured=convert_blank(row[20]),
                    affected=convert_blank(row[21]),
                    homeless=convert_blank(row[22]),
                    totalAffected=convert_blank(row[23]),
                    damageCost=convert_blank(row[24]),
                )
                disasters.append(disaster)

            # Import data using the bulk_create() method
            Continent.objects.bulk_create(continents)
            Region.objects.bulk_create(regions)
            Type.objects.bulk_create(types)
            Disaster.objects.bulk_create(disasters)

            print("data parsed successfully")
