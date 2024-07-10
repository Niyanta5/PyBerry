class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key  # Key stored in the node
        self.value = value  # Value associated with the key
        self.next = None  # Pointer to the next node in case of collisions


class HashTable:
    def __init__(self, capacity=10, load_factor=0.75):
        self.capacity = capacity  # Initial capacity of the hash table
        self.load_factor = load_factor  # Threshold at which to resize the hash table
        self.size = 0  # Number of elements currently stored
        self.buckets = [
            None
        ] * capacity  # Array to hold linked lists of key-value pairs

    def hash_function(self, key):
        """Hash function to determine index in the hash table."""

        return hash(key) % self.capacity

    def put(self, key, value):
        """Inserts a key-value pair into the hash table."""
        index = self.hash_function(key)  # Compute the bucket index

        if self.buckets[index] is None:
            # If bucket is empty, create a new ListNode and store it
            self.buckets[index] = ListNode(key, value)
            self.size += 1
        else:
            # If bucket is not empty, traverse the linked list
            current = self.buckets[index]

            while current:
                if current.key == key:
                    # If key exists, update the value and return
                    current.value = value

                    return

                if current.next is None:
                    break
                current = current.next
            # Add new ListNode at the end of the linked list
            current.next = ListNode(key, value)
            self.size += 1

        # Check if the load factor threshold is exceeded, resize if necessary

        if self.size >= self.load_factor * self.capacity:
            self._resize()

    def get(self, key):
        """Retrieves the value associated with the given key."""
        index = self.hash_function(key)  # Compute the bucket index
        current = self.buckets[index]  # Start at the head of the linked list

        while current:
            if current.key == key:
                return current.value  # Return value if key is found
            current = current.next  # Move to the next node in the linked list

        return None  # Return None if key is not found

    def remove(self, key):
        """Removes a key-value pair from the hash table."""
        index = self.hash_function(key)  # Compute the bucket index
        current = self.buckets[index]  # Start at the head of the linked list
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # Skip the current node
                else:
                    self.buckets[
                        index
                    ] = current.next  # Update head if removing the first node
                self.size -= 1  # Decrease size counter

                return True  # Return True if key is found and removed
            prev = current
            current = current.next  # Move to the next node in the linked list

        return False  # Return False if key is not found

    def _resize(self):
        """Resizes the hash table when the load factor exceeds the threshold."""
        new_capacity = self.capacity * 2  # Double the capacity
        new_buckets = [
            None
        ] * new_capacity  # Create new bucket list with increased capacity

        for bucket in self.buckets:
            current = bucket

            while current:
                new_index = hash(current.key) % new_capacity  # Compute new bucket index

                if new_buckets[new_index] is None:
                    new_buckets[new_index] = ListNode(
                        current.key, current.value
                    )  # Create new ListNode
                else:
                    new_current = new_buckets[new_index]

                    while new_current.next:
                        new_current = new_current.next
                    new_current.next = ListNode(
                        current.key, current.value
                    )  # Append new ListNode at end
                current = current.next  # Move to the next node in the current bucket

        self.capacity = new_capacity  # Update hash table capacity
        self.buckets = new_buckets  # Update hash table buckets with new buckets


# Example usage:
hash_table = HashTable()

# Inserting elements
hash_table.put("key1", "value1")
hash_table.put("key2", "value2")
hash_table.put("key3", "value3")

# Retrieving elements
print(hash_table.get("key2"))  # Output: value2

# Removing elements
hash_table.remove("key1")
print(hash_table.get("key1"))  # Output: None, as key1 is removed
