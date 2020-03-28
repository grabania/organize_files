# def extract_place(filename):
#     first = filename.find("_")
#     partial = filename[first+1:]
#     second = partial.find("_")
#     return partial[:second]


# print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
# print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
# print(extract_place("2018-01_Scottland_11/51/27.jpg"))

import os


def extract_place(filename):
    return filename.split("_")[1]


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


os.chdir("Photos")
orginals = os.listdir()
places = []

for filename in orginals:
    place = extract_place(filename)
    if place not in places:
        places.append(place)


make_place_directories(places)
print(os.listdir())
