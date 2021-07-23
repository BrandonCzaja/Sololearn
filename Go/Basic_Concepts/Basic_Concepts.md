# Basic Concepts

## Variables

-   Variables are declared using the `var` keyword
-   The following code declares a variable named i of the type int

```
    Syntax: <keyword <variable_name<> <type>
```

```
    var i int
```

-   We can assign a variable a value and the output it

```
    var i int = 8
    fmt.Println(i)
```

-   You can declare multiple variables on one line and assign values to them
    -   In the below code, the value for `i` is 42

```
    var i, j int = 8, 42
```

-   The variable type is only required if you don't assign a value to it.

```
    var i, j int = 8 42

    OR

    var i, j = 8, 42
```

-   Example of how multiple variables get assigned a value at once

```
    var x, y, z = 4, 3, 6
    x === 4
    y === 3
    z === 6
```

-   Go also supports short cut variable declaration using `:=`

```
    i := 8


    x, y := 10, 5
    x == 10
    y === 5
```

## Data Types

-   Common data types Go supports

    -   int - Integer
    -   float32 - `A single-precision` floating point value
    -   float64 - `A double-precision` floating point value
    -   string - A text value
    -   bool - Boolean true or false

    -   The difference between `float32` and `float64` is the precision. Float64 represents the number with higher accuracy, but takes up more space in memory

-   Examples of some data types in code:

```
    var x int = 42
    x := 42

    var y float32 = 1.36
    var y = 1.36

    var name string = "James"
    var name = "James"

    var online bool = true
    var online = true
```

-   Just like in Javascript, variables can be declared with `zero value`
    -   0 for numeric types
    -   false for boolean types
    -   "" for strings

## Constants

-   Just like in Javascript, variables can change their value during a program

```
    x := 42
    x = 8
```

-   To declare a constant variable, use the `const` keyword

```
    const name = "Brandon"
```

-   Remember, constants `CANNOT` be declared using the `:=` syntax
