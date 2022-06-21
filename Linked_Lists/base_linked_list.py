from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: Node = None


@dataclass
class LinkedList: 
    head: Node = None
    tail: Node = None

    def __str__(self) -> str:
        result = ''
        current = self.head

        while current:
            if current == self.tail:
                result += str(current.value)
            else:
                result += str(current.value) + ' -> '

            current = current.next

        return result

    
    def __len__(self) -> int: 
        current = self.head
        counter = 0 

        while current: 
            counter += 1 
            current = current.next

        return counter
    

    def add_to_head(self, value: Any) -> None:
        new_head = Node(value)
        new_head.next = self.head

        if self.head is None and self.tail is None:
            self.tail = new_head
        self.head = new_head


    def add_to_tail(self, value: Any) -> None:
        new_tail = Node(value)

        if len(self) > 0:
            self.tail.next = new_tail
        else: 
            self.head = new_tail

        self.tail = new_tail

    def remove_head(self) -> Any:
        if len(self) == 0:
            return None

        removed_node = self.head

        if self.head == self.tail:
            self.tail = self.tail.next
        
        self.head = self.head.next

        return removed_node