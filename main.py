"""
HW05 — City Bike Registry (Resizing Chaining Map)
"""

class HashMap:
    """Chaining hash map with auto-resize at load factor > 0.75."""

    def __init__(self, m=4):
        # create m empty buckets and size counter
        self.buckets = [[] for _ in range(m)]
        self.count = 0

    def _hash(self, s):
        """Return simple integer hash for string s."""
        return sum(ord(c) for c in s)

    def _index(self, key, m=None):
        """Return bucket index for key with current or given bucket count."""
        if m is None:
            m = len(self.buckets)
        return self._hash(key) % m

    def __len__(self):
        """Return number of stored pairs."""
        return self.count

    def _resize(self, new_m):
        """Resize to new_m buckets and rehash all pairs."""
        old_items = []
        for bucket in self.buckets:
            for k, v in bucket:
                old_items.append((k, v))
        # reinitialize
        self.buckets = [[] for _ in range(new_m)]
        self.count = 0
        for k, v in old_items:
            self.put(k, v)

    def put(self, key, value):
        """Insert or overwrite. Resize first if load will exceed 0.75."""
        # check if resize needed
        load_factor = (self.count + 1) / len(self.buckets)
        if load_factor > 0.75:
            self._resize(len(self.buckets) * 2)

        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        """Return value for key or None if missing."""
        idx = self._index(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove key if present. Return True if removed else False."""
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

if __name__ == "__main__":
    # Manual test
    m = HashMap()
    m.put("A", "1")
    m.put("B", "2")
    print(len(m), m.get("A"))
    m.delete("A")
    print(len(m), m.get("A"))
