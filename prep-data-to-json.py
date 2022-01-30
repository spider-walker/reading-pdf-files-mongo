import pymongo
import json

with open('./data/output.txt') as f:
    lines = f.readlines()
    counties = dict()
    constituencies = dict()
    wards = dict()
    counties_set = set()
    wards_set = set()
    constituencies_set = set()
    total = 0
    for line in lines:
        data = line.split(',');
        county = data[1].strip()
        constituency = data[5].strip()
        ward = line.split(',')[9].strip()
        voters = int(data[11].strip())

        total += voters;

        if not county in counties_set:
            constituencies = dict()

        if not f'{county},{constituency}' in constituencies_set:
            wards = dict()

        counties_set.add(county)
        constituencies_set.add(f'{county},{constituency}')
        wards_set.add(f'{county},{constituency}')
        county_index = f"000{len(counties_set)}"[-3:]
        constituencies_index = f"000{len(constituencies_set)}"[-3:]
        wards_index = ward.lower().replace(' ', '').replace(' ', '').replace(' ', '').replace(' ', '').replace('\'', '')

        wards.update({
            wards_index: {
                'ward_name': ward.lower().capitalize(),
                'voters_2017': voters
            }
        })

        constituencies.update({
            constituencies_index: {
                'constituency_name': constituency.lower().capitalize(),
                'wards': wards
            }
        })

        counties.update({county_index: {
            'county_name': county.lower().capitalize(),
            'constituencies': constituencies
        }})
    counties.update({'total': total})

    print((json.dumps(counties)))
