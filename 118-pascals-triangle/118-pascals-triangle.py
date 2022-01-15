class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_of_lists = [[1]]

        def generateNext(list):
            new_list = [1,1]

            for i in range(1, len(list)):
                new_list.insert(i, list[i] + list[i-1])
            return(new_list)


        for i in range(0, numRows - 1):
            list_of_lists.append(generateNext(list_of_lists[i]))

        return(list_of_lists)