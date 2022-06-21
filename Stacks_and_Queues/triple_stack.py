from typing import List

class TripleStack:
    def __init__(self, list_length: int):
        self.list: List[int] = [0] * list_length
        self.tops: List[int] = [-1, list_length, list_length // 2]
        self.sizes: List[int] = [0] * 3

    def is_mid_stack_even(self):
        return self.sizes[2] % 2 == 0

    def is_stack_empty(self, stack_number: int):
        return self.sizes[stack_number] == 0

    def is_stack_full(self, stack_number: int): 
        if stack_number == 0 and not self.is_mid_stack_even():
            return self.tops[stack_number] == self.tops[2] - self.sizes[2]
        elif stack_number == 1 and self.is_mid_stack_even():
            return self.tops[stack_number] == self.tops[2] + self.sizes[2]

        return (not self.is_mid_stack_even() and self.tops[0] == self.tops[2] - self.sizes[2]) or \
               (self.is_mid_stack_even() and self.tops[1] == self.tops[2] + self.sizes[2])
    
    def pop(self, stack_number: int):
        if self.is_stack_empty(stack_number):
            raise RuntimeError(f'Stack: {stack_number} is empty')

        removed_item: int = self.list[self.tops[stack_number]]

        if stack_number == 0:
            self.tops[stack_number] -= 1
        elif stack_number == 1:
            self.tops[stack_number] += 1
        else: 
            if self.is_mid_stack_even():
                self.tops[stack_number] += (self.sizes[stack_number] - 1)
            else:
                self.tops[stack_number] -= (self.sizes[stack_number] - 1)

        self.sizes[stack_number] -= 1
        
        return removed_item

    def push(self, item: int, stack_number: int):
        if self.is_stack_full(stack_number):
            raise RuntimeError(f'Stack: {stack_number} is full')

        if stack_number == 0:
            self.tops[stack_number] += 1
        elif stack_number == 1:
            self.tops[stack_number] -= 1
        else:
            if self.is_mid_stack_even():
                self.tops[stack_number] += self.sizes[stack_number]
            else:
                self.tops[stack_number] -= self.sizes[stack_number]
        
        self.list[self.tops[stack_number]] = item
        self.sizes[stack_number] += 1

    def __repr__(self):
        return str(self.list)


if __name__ == '__main__':
    stack_array = TripleStack(5)
    stack_array.push(item=1, stack_number=0)
    stack_array.push(item=1, stack_number=1)
    stack_array.push(item=1, stack_number=2)

    print(str(stack_array))