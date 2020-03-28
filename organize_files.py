# def extract_place(filename):
#     first = filename.find("_")
#     partial = filename[first+1:]
#     second = partial.find("_")
#     return partial[:second]


# print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
# print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
# print(extract_place("2018-01_Scottland_11/51/27.jpg"))

import os


def make_place_directories(places):  # Here's the function definition
    for place in places:
        os.mkdir(place)


def extract_place(filename):
    return filename.split('_')[1]

# First, extract place names.


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
    # Second, make place directories.
    make_place_directories(places)


# Third, move files to directories.
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


organize_photos("Photos")
