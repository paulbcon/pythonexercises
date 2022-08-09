# Iterators terminating on the shortest input sequence
# Note to self: Key point -> if any of the iterator are shorter than the rest, the resulting 
# iterator won't break, but will simply stop as soon as the shortest iterator is exhausted

from itertools import compress
data = range(10)
even_selector = [1 , 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)