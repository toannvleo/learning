# Tuples

- Tuples are an ordered sequence

```
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
```

# Sets

- Sets are type of collection:

  - This means that like lists and tuples you can input different Python types

- Unlike lists and tuples they are unordered:

  - This means sets do not record element position

- Sets only have unique elements:

  - This means there is only one of a particular

## Creating a Set

```
set1 = {"pop", "rock", "country", "rock", "disco", "rock"}

>>> set1: {'country', 'disco', 'pop', 'rock'}
```

- Convert a list to a set

```
album = {"Thriller", 1982, "Thriller", "Michael Jackson"}
album_set = set(album)

>>> album_set: {1982, 'Michael Jackson', 'Thriller'}
```

## Set Operations

- Method `add` and `remove`

```
A = {"Thriller", "Black in Black", "AC/DC"}
A.add("NSYNC")

>>> A: {'AC/DC', 'Black in Black', 'NSYNC', 'Thriller'}


A.remove("NSYNC")

>>> A: {'AC/DC', 'Black in Black', 'Thriller'}
```

- Check if a element in a set

```
A = {"Thriller", "Black in Black", "AC/DC"}
"AC/DC" in A

>>> True
```

- Get the same elements in set1 and set2

```
album_set1 = {"Thriller", "Black in Black", "AC/DC"}
album_set2 = {"Thriller", "Black in Black", "The Dark Side of the Moon"}
album_set3 = album_set1 & album_set2

>>> album_set3: {'Black in Black', 'Thriller'}
```

- Get all elements in both set1 and set2

```
album_set1 = {"Thriller", "Black in Black", "AC/DC"}
album_set2 = {"Thriller", "Black in Black", "The Dark Side of the Moon"}
album_set3 = album_set1.union(album_set2)

>>> album_set3: {'AC/DC', 'Black in Black', 'The Dark Side of the Moon', 'Thriller'}
```

- Check if set3 is subset of set1

```
album_set1 = {"Thriller", "Black in Black", "AC/DC"}
album_set3 = {"Thriller", "Black in Black"}
album_set3.issubset(album_set1)

>>> True
```