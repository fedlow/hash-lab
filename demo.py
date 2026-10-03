from hash_table import HashTable
from string_hash import string_hash
from string_dict import StringDictionary


print("=== 1. HashTable: базовые операции ===")
ht = HashTable(initial_size=5)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("cherry", 300)
print(f"search('apple')  = {ht.search('apple')}")
print(f"search('banana') = {ht.search('banana')}")
print(f"delete('apple')  = {ht.delete('apple')}")
print(f"search('apple')  = {ht.search('apple')}")
print(f"delete('apple')  = {ht.delete('apple')}  (повторно)")
print(f"Состояние: {ht}")

print("\n=== 2. resize: начальный размер 5, добавляем 10 элементов ===")
ht2 = HashTable(initial_size=5)
print(f"До:     size={ht2.size}, count={ht2.count}")
for i in range(10):
    ht2.insert(f"key{i}", i * 10)
    print(f"  + key{i}: size={ht2.size}, count={ht2.count}")
print(f"После:  size={ht2.size}, count={ht2.count}")
print("Содержимое таблицы:")
ht2.display()

print("\n=== 3. Хеш-функция строки ===")
for s in ["", "a", "abc", "Hello", "hello", "world"]:
    print(f"  string_hash({s!r:10}) = {string_hash(s)}")

print("\n=== 4. Словарь на основе хеш-функции ===")
d = StringDictionary(size=10)
for s in ["apple", "banana", "cherry", "date", "elderberry"]:
    d.add(s)

print("Содержимое словаря:")
d.display()

print()
for s in ["apple", "cherry", "not_in_dict"]:
    print(f"  get({s!r:15}) = {d.get(s)}")