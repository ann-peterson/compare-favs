# ann_fav = open("ann_fav_foods.txt")
# ann_list = ann_fav.readlines()
# print ann_list


# carly_fav = open("carly_fav_foods.txt")
# carly_list = carly_fav.readlines()
# print carly_list

# def compare_favs(ann_list,carly_list):
#     if ann_list[0] == carly_list[0]:
#         print "Our favorite foods are the same!"
#     else:
#         print "Our favorite foods are different!"

# compare_favs(ann_list,carly_list)

#arly_list = open("carly_fav_foods.txt")


def list_to_file():
    with open("carly_fav_foods.txt", mode = "a") as carly_list:
        carly_list.append("hi")

list_to_file()        