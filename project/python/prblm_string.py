def string_man():
    # str1 = "I am a girl"
    # rev_str1 = str1[::-1]
    # print(rev_str1)
    # str2=''
    # for char in str1:
    #     str2 = char + str2
    # print(str2)
    # str1 = "HeLLo"
    # # vowels = ['a', 'e', 'i', 'o', 'u']
    # count = 0
    # for char in str1.lower():
    #     if char in ['a', 'e', 'i', 'o', 'u']:
    #         count+= 1
    # print(count)
    # text = "aabbcdd"
    # str_count = {}
    # for char in text:
    #     str_count[char] = str_count.get(char, 0) + 1
        
    # for key,value in str_count.items():
    #     if value == 1:
    #         print(key)
    #         break
    #anagram
    # a = "Dormitory"
    # b = "Dirty room"
    # a = a.replace(" ", "").lower()
    # b = b.replace(" ", "").lower()
    # counts = {}
    # for char in a:
    #     counts[char] = counts.get(char, 0) + 1
    # for char in b:
    #     if char not in counts:
    #         return False
    #     counts[char] -= 1
    #     if counts[char] == 0:
    #         del counts[char]
    # print(not counts)
    # text = "aaabbc"
    # count = 1
    # result = ""
    # for i in range(1, len(text)):
    #     if text[i] == text[i-1]:
    #         count += 1
    #     else:
    #         result += text[i-1] + str(count)
    #         count = 1
    # result += text[-1] + str(count)
    # print(result)
    # text = "banana"
    # count = set()
    # result = ""
    # for char in text:
    #     if char not in count:
    #         count.add(char)
    #         result += char
    # print(result)
    # text = "A man, a plan, a canal: Panama"
    # for char in text:
    #     if char.isalnum():
    #         cleaned = char.lower()
    # reverse = cleaned[::-1]
    # print(cleaned == reverse)
    # text = "a4k3b2"
    # new_text = ''
    # current = ''
    # for char in text:
    #     if char.isalpha():
    #         new_text += char
    #         current = char
    #     if char.isdigit():
    #         new_text += chr(ord(current) + int(char))
    #         current=""
    # print(new_text)
    # text = "aaaabbbccd"
    # new_text = {}
    # text2 = ""
    # for char in text:
    #     new_text[char] = new_text.get(char, 0) + 1
    # for key,value in new_text.items():
    #     text2 += key + str(value)
    # print(text2)
    # text1 = "abccd"
    # text2 = "cdecd"
    # list1, list2 = list(), list()
    # for char in text1:
    #     list1.append(char)
    # for char in text2:
    #     if char in list1:
    #         list1.remove(char)
    #     else:
    #         list2.append(char)
    # # set3 = (list1 | list2) - (list1 & list2)
    # print(list1,list2)

    

string_man()