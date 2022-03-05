#
# for / while
#
# 0 10
# 1 9
# 2 8
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
# 8 2
# 1 0

#
# v1 = 0
# v2 = 10
# print(v1, v2)
# while True:
#     v1 = v1 + 1
#     v2 = v2 - 1
#     print(v1, v2)
#
#     if(v1 == 9):
#         break


for indice, valor in enumerate(range(10,1, -1)):
    print(indice, valor)
