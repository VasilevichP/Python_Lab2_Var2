def isAnagram(str1, str2):
    list1 = list(str1)
    list1.sort()
    list2 = list(str2)
    list2.sort()
    return list1 == list2


while True:
    word1 = input("Введите первое слово: ")
    if word1.isalpha():
        break
    else:
        print("Введено небуквенное слово")
while True:
    word2 = input("Введите второе слово: ")
    if word2.isalpha():
        break
    else:
        print("Введено небуквенное слово")
print("Являются ли слова анаграммами? ", isAnagram(word1, word2))
