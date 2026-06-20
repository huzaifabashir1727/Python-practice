# marks_dictionary_1 = {"Huzaifa" : 22 , "Bilal" : 18 , "Ali" : 17 , "Ahmed" : 24}
marks_dictionary_1 = {
    "Huzaifa": {"marks": 22},
    "Bilal": {"marks": 18},
    "Ali": {"marks": 17},
    "Ahmed": {"marks": 24}
}

# marks_dictionary_2 = {"Mehmood" : 10 , "Atif" : 20 , "Asheel" : 15 , "Talha" : 22}
marks_dictionary_2 = {
    "Mehmood": {"marks": 10},
    "Atif": {"marks": 21},
    "Asheel": {"marks": 15},
    "Talha": {"marks": 22}
}

# dictionary_1 = {}
# dictionary_2 = {}

# passed = {}
# failed = {}

# Example 1
# for k in marks_dictionary_1 :
#     marks_dictionary_1[k] = marks_dictionary_1[k] + 5
# print(marks_dictionary_1)
# dictionary_1 = {k : v["marks"] + 4 for k,v in marks_dictionary_1.items()}
# print(dictionary_1)

# Example 2
# for k in marks_dictionary_2 :
#     marks_dictionary_2[k] = marks_dictionary_2[k] + 2
# print(marks_dictionary_2)
# dictionary_2 = {k : v["marks"] + 4 for k,v in marks_dictionary_2.items()}
# print(dictionary_2)

# Example 3
# for k,v in marks_dictionary_1.items() :
#     if (v["marks"] < 20) :
#         v["Grade"] = "B"
#     else :
#         v["Grade"] = "A"
# print(marks_dictionary_1)
# passed = {k : v for k,v in marks_dictionary_1.items() if(v["marks"] > 20)}
# print(passed)

# Example 4
# for k,v in marks_dictionary_1.items() :
#     if (v["marks"] < 20) :
#         passed[k] = v["marks"]
#     else :
#         failed[k] = v["marks"]
        
# print(passed)
# print(failed)

# Example 5
# for k,v in marks_dictionary_1.items() :
#     if (v["marks"] < 20) :
#         v["Grade"] = "P"
#         passed[k] = v["marks"]
#     else :
#         v["Grade"] = "F"
#         failed[k] = v["marks"]
        
# print(passed)
# print(failed)

# passed = {k : {"marks" : v["marks"] , "Grade" : "P" } for k,v in marks_dictionary_1.items() if(v["marks"] > 20)}
# print(passed)



print(marks_dictionary_1.get("Huzaifa" , None))