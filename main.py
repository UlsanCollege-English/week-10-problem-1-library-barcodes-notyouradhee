"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    # TODO Step 4: build the data structure (list of lists)
    return [[] for _ in range(m)]

def hash_basic(s):
    """Return a simple integer hash for string s.
    Hint: sum ordinals of characters.
    """
    # TODO Step 5→6: compute a stable integer from s
    total = 0
    for ch in s:
        total += ord(ch)
    return total

def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    # TODO Steps 4–6: compute index, scan bucket, overwrite or append
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            return
    bucket.append([key, value])

def get(t, key):
    """Return value for key or None if not present."""
    # TODO Steps 4–6: compute index, scan bucket, return value or None
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    return None

def has_key(t, key):
    """Return True if key exists in table t; else False."""
    # TODO Steps 4–6: scan the correct bucket
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for pair in bucket:
        if pair[0] == key:
            return True
    return False

def size(t):
    """Return total number of stored pairs across all buckets."""
    # TODO Step 4: count all pairs
    count = 0
    for bucket in t:
        count += len(bucket)
    return count

# if __name__ == "__main__":
#     # Optional manual check (not graded)
#     # TODO Step 7: try a tiny run by yourself
#     pass
