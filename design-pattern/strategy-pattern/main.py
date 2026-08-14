from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        print('Sorting using Bubble Sort')
        # Actual Bubble Sort Logic here

class MergeSortStrategy(SortingStrategy):
    def sort(self, array):
        print('Sorting using Merge Sort')
        # Actual Merge Sort Logic here

class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print('Sorting using Quick Sort')
        # Actual Quick Sort Logic here

class SortingContext:
    def __init__(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def set_sorting_strategy(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def perform_sort(self, array):
        self.sorting_strategy.sort(array)

# Client
array1 = ["cpp","c","java","python3","csharp","html","css","javascript","php","cpp14","cobol","dart","go","julia","kotlin","lisp","matlab","node","objc","perl","r","rust","ruby","scala","swift","solidity","xml"]
sorting_context = SortingContext(BubbleSortStrategy())
sorting_context.perform_sort(array1) # Output: Sorting using Bubble Sort

sorting_context.set_sorting_strategy(MergeSortStrategy())
array2 = ["cpp","c","java","python3","csharp","html","css","javascript","php","cpp14","cobol","dart","go","julia","kotlin","lisp","matlab","node","objc","perl","r","rust","ruby","scala","swift","solidity","xml"]
sorting_context.perform_sort(array2) # Output: Sorting using Merge Sort

sorting_context.set_sorting_strategy(QuickSortStrategy())
array3 = ["cpp","c","java","python3","csharp","html","css","javascript","php","cpp14","cobol","dart","go","julia","kotlin","lisp","matlab","node","objc","perl","r","rust","ruby","scala","swift","solidity","xml"]
sorting_context.perform_sort(array3) # Output: Sorting using Quick Sort