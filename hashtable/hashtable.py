class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        # creates a list with the length of the capacity, each item in the list will be None initially and as values are hashed and put into storage the None values will change to
        # linked lists i.e the HashTableEntry
        self.storage = [None] * self.capacity

        # counter to keep track of how many items are actually stored in the hashtable
        self.stored_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # load factor = number of actual stored items / length of storage(capacity)
        slot_nums = self.get_num_slots()
        items = self.stored_items

        load_factor = items / slot_nums

        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # FNV offset basis computed using "chongo <Landon Curt Noll> /\../\" when expressed in ASCII?
        # 64 bit offset basis = 14695981039346656037
        # 64 bit prime = 1099511628211
        # XOR operator in python is ^

        key_utf8 = key.encode()

        # constants
        hash = 14695981039346656037
        FNV_prime = 1099511628211
        
        for byte in key_utf8:
            hash = hash * FNV_prime
            hash = hash ^ byte
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Check the load factor initially and resize the hashtable if necessary
        load_factor = self.get_load_factor()
        print(load_factor)
        if load_factor > 0.7:
            print("growing")
            self.resize(self.capacity * 2)

        storage_index = self.hash_index(key)
        if self.storage[storage_index] is not None:
            current_node = self.storage[storage_index]
            while current_node.key != key:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    current_node.next = HashTableEntry(key, value)
                    self.stored_items += 1

            else:
                current_node.value = value
        else:
            self.storage[storage_index] = HashTableEntry(key, value)
            self.stored_items += 1
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

         # Check the load factor initially and resize the hashtable if necessary
        load_factor = self.get_load_factor()
        print(load_factor)
        # we want to shrink here
        if load_factor < 0.2:
            print("shrinking")
            self.resize(self.capacity // 2)

        storage_index = self.hash_index(key)
        current_node = self.storage[storage_index]

        if current_node is None:
            print("Unable to find the Key in the Hash Table")
        
        if current_node.key == key:
            self.storage[storage_index] = current_node.next
            self.stored_items -= 1
            return
        else:
            prev_node = current_node
            current_node = current_node.next
            
            while current_node is not None:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    self.stored_items -= 1
                    return
                else:
                    prev_node = current_node
                    current_node = current_node.next

            else:
                print("Unable to find the Key in the Hash Table")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        storage_index = self.hash_index(key)
        # print("storage_index", storage_index)
        if self.storage[storage_index] is not None:
            current_node = self.storage[storage_index]
            while current_node.key != key:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    return None
            else:
                return current_node.value
        else:
            return None


    # works for both shrinking or growing
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        old_storage = self.storage.copy()
        
        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        for item in old_storage:
            if item is not None:
                current_node = item
                while current_node is not None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next
                    




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
