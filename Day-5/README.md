# Day 6 - Variables and Data Types

## What is a variable?

Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

```r
a = 1
b = True
c = "Vaibhav"
d = None
```

These are four variables of different data types.

<h2>What is a Data Type?</h2>-
 <p>Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. </p>
In python, we can print the type of any operator using type function:

```r
a = 1
print(type(a))
b = "1"
print(type(b))
```

By default, python provides the following built-in data types:

<h2>1. Numeric data: int, float, complex</h2>

<h2>2. Text data: str</h2>
str: "Hello World!!!", "Python Programming"

<h2>3. Boolean data:</h2>
Boolean data consists of values True or False.

## 4. Sequenced data: list, tuple

### list:

A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

```r
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

### Tuple:

A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

```r
tuple1 = (("parrot", "sparrow"), ("Lion" "Tiger"))
print(tuple1)
```

### 5. Mapped data: dict

A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

```r
{'name': 'Vaibhav', 'age': 20, 'canVote': True}
```
