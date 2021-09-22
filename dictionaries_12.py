def CountFrequency(my_list):
    freq = {}
    for items in my_list:
        freq[items]= my_list.count(items)
    for key, value in freq.items():
            print("% d : % d"%(key, value))
if __name__=="__main__":
     my_list =[1, 1, 2, 1, 3, 4, 4, 3, 3, 2, 2, 6, 5, 6, 5, 4, 3, 3]
     CountFrequency(my_list)
