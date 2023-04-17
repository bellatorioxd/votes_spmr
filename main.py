
list_of_candidates_start=["a", "b", "c", "d"]
main_arr=[
    ["", 2, 5, 5, 7],
    [3, "a", "b", "c", "d"],
    [2, "b", "d", "a", "a"],
    [1, "c", "c", "d", "c"],
    [0, "d", "a", "b", "b"]]

all_cand = 19

def vidnosna_bilshist(array):
    points = array[1][0]
    list_of_candidates=array[1][1:]
    res={}
    for element in list_of_candidates_start:
        res[element] = 0
        i=0
        for elem in list_of_candidates:
                if elem == element:
                    res[element]+=array[0][i+1]
                i+=1
    winner_value=max(res.values())
    winner = list(res.keys())[list(res.values()).index(winner_value)]
    return res, winner

def kondorse(array):
    kondorse_dict={}
    new_array=[]
    columns=[]
    for elem in array:
        new_array.append(elem[1:])
    for i in range(0, len(new_array[0])):
        one_col=[]
        for elem in new_array:
            one_col.append(elem[i])
        columns.append(one_col)
    for element in list_of_candidates_start:
        kondorse_dict[element] = []
    def compare_two( elem_1,elem_2):
        res_1_more_2 = 0
        res_2_more_1 = 0
        for col in columns:
            if col.index(elem_1) < col.index(elem_2):
                res_1_more_2 += col[0]
            elif col.index(elem_1) > col.index(elem_2):
                res_2_more_1 +=col[0]
        return res_1_more_2
    for elem in list_of_candidates_start:
        combinations_lst = [(elem, item) for item in list_of_candidates_start]
        for pair in combinations_lst:
            kondorse_dict[elem].append(compare_two(pair[0], pair[1]))
    for value in kondorse_dict.values():
        if all(num > all_cand/2 or num==0 for num in value):
            winner = list(kondorse_dict.keys())[list(kondorse_dict.values()).index(value)]
    return kondorse_dict, winner


def deborda(array):
    res_deborda ={}
    for element in list_of_candidates_start:
        res_deborda[element] = 0
        for row in array[1:]:
            sum=0
            indexes_list = [index for index in range(len(row)) if row[index] == element]
            for pos in indexes_list:
                sum+=row[0]*array[0][pos]
            res_deborda[element]+=sum
    winner_value = max(res_deborda.values())
    winner =  list(res_deborda.keys())[list(res_deborda.values()).index(winner_value)]
    return res_deborda, winner

def koplend(array):
    res = kondorse(array)[0]
    kollend_arr ={}
    for element in list_of_candidates_start:
        kollend_arr[element] = 0
        for value in res[element]:
            if value>0:
                if value > all_cand/2:
                    kollend_arr[element] += 1
                elif value < all_cand / 2:
                    kollend_arr[element] -= 1
    winner_value = max(kollend_arr.values())
    winner = list(kollend_arr.keys())[list(kollend_arr.values()).index(winner_value)]
    return kollend_arr, winner

def simmpson(array):
    res = kondorse(array)[0]
    simps_dict={}
    for element in list_of_candidates_start:
        simps_dict[element] = 0
        for key in res.keys():
            if key == element:
                min_num = min(num for num in res[key] if num != 0)
                simps_dict[element] =min_num
    winner_value = max(simps_dict.values())
    winner = list(simps_dict.keys())[list(simps_dict.values()).index(winner_value)]
    return simps_dict, winner



print("Переможець за критерієм відносної більшості:", vidnosna_bilshist(main_arr))
print("Переможець критерієм Кондорсе: ", kondorse(main_arr))
print("Переможець критерієм Де Борда: ", deborda(main_arr))
print("Переможець критерієм Копленда: ", koplend(main_arr))
print("Переможець критерієм Сіпмсона: ", simmpson(main_arr))









