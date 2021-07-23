# Getting Started

## Packages

-   Every Go program is made up of packages
-   A Go program starts running in the `main` package

```
package main
```

-   There are other packages in Go such as "fmt" that can be imported

```
import "fmt" // => provides input/output functionality
```

-   And you can import more than one package at a time

```
import (
    "fmt"
    "math"
)
```

## Imports

-   Each package has exported names, which you can access after importing them
-   In Go, a name is exported if it begins with a `capital letter`
-   You can access the exported names using the package name, a dot, and the exported name
    -   Exported names sound similar to function methods
-   The output is provided inside the parenthesis enclosed in double quotes or back ticks

```
package main
import "fmt"

func main(){
    fmt.Println("Hello World!")
}
```

-   Similar to other programming languages such as Java or C++ `func main()` is the entry point of the program. It is the function that gets executed when we run the program

```
1. package main
2. import "fmt"

3. func main(){
    4. fmt.Println("Hello World!")
}

1. Defines the main package
2. Imports the "fmt" package used for output
3. Defines the main() function
4. Uses the Println() function of the fmt package to generate the desired output
```

## Comments

-   Comments, both single line and multiple lines, are the same as Javascript:
