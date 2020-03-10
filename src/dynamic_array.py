class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0  # Count is how much is currently used
        # How much total space is currently allocated wether we are using it or not
        self.capacity = capacity
        self.storage = [None] * self.capacity
