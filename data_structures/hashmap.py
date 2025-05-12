from typing import Any, Optional

class HashMap:
    def __init__(self, size):
        self.hashmap: list[Optional[tuple[str, Any]]] = [None for _ in range(size)]

    def __key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        self.__resize()
        index = self.__key_to_index(key)
        original_index = index
        first_iteration = True

        it = self.hashmap[index]
        while (it is not None) and (it[0] != key):
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")

            index = (index + 1) % len(self.hashmap)
            first_iteration = False
            it = self.hashmap[index]

        self.hashmap[index] = (key, value)

    def __resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return

        load = self.current_load()

        if load < 0.05:
            return
        
        new_size = len(self.hashmap) * 10
        new_hashmap:  list[Optional[tuple[str, Any]]] = [None for _ in range(new_size)]
        pairs = [pair for pair in self.hashmap if pair is not None]

        for pair in pairs:
            index = self.__key_to_index(pair[0])
            new_hashmap[index] = (pair[0], pair[1]) 
            
        self.hashmap = new_hashmap
        self.size = new_size
            
            
    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
            
        non_empty_list = [pair for pair in self.hashmap if pair is not None]
        filled_buckets = len(non_empty_list)

        return filled_buckets / len(self.hashmap)

    def get(self, key):
        index = self.__key_to_index(key)
        original_index = index
        first_iteration = True

        it = self.hashmap[index]
        while it is not None:
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")

            k = it[0]

            if k == key:
                return it[1]

            index = (index + 1) % len(self.hashmap)
            first_iteration = False
            it = self.hashmap[index]

        raise Exception("sorry, key not found")

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
