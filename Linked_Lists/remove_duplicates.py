from base_linked_list import LinkedList

def remove_duplicates(list):
    if list.head is not None:
        current = list.head
        hash_map = {current.value: True}

        while current.next is not None:
            if current.next.value in hash_map:
                current.next = current.next.next
            else:
                hash_map.update({current.next.value: True})
                current = current.next

    return str(list)

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.add_to_tail(12)
    linked_list.add_to_tail(10)
    linked_list.add_to_tail(47)
    linked_list.add_to_tail(31)
    linked_list.add_to_tail(10)
    linked_list.add_to_tail(31)
    linked_list.add_to_tail(42)

    remove_duplicates(linked_list)
  