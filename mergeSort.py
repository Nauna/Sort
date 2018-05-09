class MergeSort: 
    def sort(self, unsortedList):
        n_size = len(unsortedList)
        print("Printing Unsorted List being passed in:")
        print(unsortedList)
        if n_size < 2:
            return unsortedList
        else:
            middle_index = int(n_size/2)
           
           # left_list = [unsortedList[i] for i in (middle_index:)]
            left_list = unsortedList[middle_index:]
            right_list = unsortedList[:middle_index] # [unsortedList[i] for i in (:middle_index)]#
           
            if len(left_list)>1:
                sorted_left = MergeSort.sort(self, left_list)
            else:
                sorted_left = left_list
            if len(right_list)>1:
                sorted_right = MergeSort.sort(self, right_list)
            else:
                sorted_right = right_list

            right_size = len(sorted_right)
            left_size = len(sorted_left)
            tot_size = right_size + left_size
            index_L = 0
            index_R = 0
            merged_List = []
            
            for i in range(tot_size):
                if index_L > (left_size-1):
                    merged_List = merged_List + sorted_right[index_R:]
                    return merged_List
                if index_R > (right_size-1):
                    return merged_List + sorted_left[index_L:]
                if sorted_right[index_R] < sorted_left[index_L]:
                    merged_List = merged_List + [sorted_right[index_R]]
                    index_R = index_R + 1
                else:
                    merged_List = merged_List + [sorted_left[index_L]]
                    index_L = index_L + 1
            return merged_List

def main():   
    print(MergeSort.sort(MergeSort, [4,6,8,9,1,10,11]))

main()