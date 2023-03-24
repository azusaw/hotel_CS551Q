import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from disaster.models import Disaster, Continent, Region, Type, disaster_subgroup

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # 从表中删除数据，这样，如果我们重新运行文件，就不会重复数值了
        Disaster.objects.all().delete()
        print("table dropped successfully")

    base_dir = Path(__file__).resolve().parent.parent.parent.parent

    with open(str(base_dir) + '/data/_bk/1970-2021_DISASTERS.csv', newline='', ) as f:

        reader = csv.reader(f, delimiter=",")
        next(reader)

        disasters = []
        continents = set()
        regions = set()
        types = set()
        subgroups = set()

        for row in reader:
            continent = row[11]
            region = row[10]
            type = row[5]
            subgroup = row[4]

            # 添加数据到相关的集合
            continents.add(Continent(id=continent))
            regions.add(Region(id=region, continent_id=continent))
            types.add(Type(id=type))
            subgroups.add(disaster_subgroup(id=subgroup))

            # 创建 Disaster 模型对象
            disaster = Disaster(
                disasterNo=(row[0]),
                year=row[1],
                seq=row[2],
                group=row[3],
                subgroup_id=subgroup,
                type_id=type,
                subtype=row[6],
                eventName=row[7],
                country=row[8],
                iso=row[9],
                region_id=region,
                continent_id=continent,
                location=row[12],
                startYear=row[13],
                startMonth=row[14],
                startDay=row[15],
                endYear=row[16],
                endMonth=row[17],
                endDay=row[18],
                totalDeaths=row[19],
                injured=row[20],
                affected=row[21],
                homeless=row[22],
                totalAffected=row[23],
                damageCost=row[24]
            )

            disasters.append(disaster)

        # 使用 bulk_create() 方法导入数据
        Continent.objects.bulk_create(continents)
        Region.objects.bulk_create(regions)
        Type.objects.bulk_create(types)
        disaster_subgroup.objects.bulk_create(subgroups)
        Disaster.objects.bulk_create(disasters)