# Python - Async Comprehension

## Learning Objectives

---

### ✅ 1. **How to Write an Asynchronous Generator**

An **asynchronous generator** is like a regular generator, but it uses `async def` and `yield` with `await` inside. It allows you to produce values **over time**, especially when dealing with I/O or delays.

#### 🧪 Example:
```python
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(3):
        await asyncio.sleep(1)  # Simulates async work
        yield random.uniform(0, 10)  # Yields a float
```

- `await` makes the generator asynchronous (e.g., waiting on a delay or I/O).
- `yield` sends a value out to the caller.
- You use `AsyncGenerator[value_type, send_type]` for type annotation. The `send_type` is usually `None` unless you’re sending values into the generator (rare).

---

### ✅ 2. **How to Use Async Comprehensions**

An **async comprehension** is like a regular list comprehension, but it works with asynchronous iterators (like an async generator).

#### 🧪 Example:
```python
async def async_comprehension() -> list[float]:
    return [i async for i in async_generator()]
```

This:
- Runs the generator asynchronously.
- Collects all yielded values into a list.
- Returns the list after the generator is exhausted.

✅ It's equivalent to:
```python
result = []
async for i in async_generator():
    result.append(i)
return result
```

---

### ✅ 3. **How to Type-Annotate Async Generators**

#### Basic Syntax:
```python
from typing import AsyncGenerator

async def my_async_gen() -> AsyncGenerator[int, None]:
    yield 1
```

- `AsyncGenerator[YieldType, SendType]`
  - **YieldType** is the type of values yielded.
  - **SendType** is usually `None`.

If your generator doesn’t take sent values (e.g., using `.send()`), you can just use `None` for the second part.

#### Alternative with Python 3.9+:
```python
from collections.abc import AsyncGenerator  # preferred in newer Python

async def gen() -> AsyncGenerator[int, None]:
    yield 42
```

---

### 🔁 Summary

| Concept                | Syntax Example                                      | Notes |
|------------------------|-----------------------------------------------------|-------|
| Async generator        | `async def gen(): yield val`                        | Use `await` inside |
| Async comprehension    | `[x async for x in async_gen()]`                    | Works with `async for` |
| Type annotation        | `AsyncGenerator[float, None]`                       | From `typing` or `collections.abc` |

---

## ✅ Full Example: Async Generator + Async Comprehension + Type Annotations

```python
import asyncio
import random
from typing import AsyncGenerator, List

# 1. Asynchronous generator that yields 10 random float numbers
async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random float numbers between 0 and 10, with a delay."""
    for _ in range(10):
        await asyncio.sleep(1)  # Simulates an async operation (e.g., network, I/O)
        yield random.uniform(0, 10)

# 2. Async comprehension to collect numbers from the async generator
async def async_comprehension() -> List[float]:
    """Collects and returns 10 random numbers from async_generator using async comprehension."""
    return [num async for num in async_generator()]

# 3. Entry point to run the coroutine
async def main() -> None:
    numbers = await async_comprehension()
    print("Collected numbers:", numbers)

# 4. Run the program
if __name__ == "__main__":
    asyncio.run(main())
```

---

### 💡 What You’ll Learn from This:

- `async_generator()` yields values one by one, simulating async work with `await asyncio.sleep(1)`.
- `async_comprehension()` uses an **async comprehension** to consume the async generator and return a list of results.
- `main()` runs the coroutine and prints the final list.
- All functions are **fully type-annotated**.

---

Let's explore how to implement asynchronous generators and async comprehensions in various programming languages, including TypeScript, Rust, Go, Ruby, and C++.

---

## ✅ TypeScript Version

TypeScript, built on JavaScript, supports asynchronous generators and async iteration using `async function*` and `for await...of` loops.

```typescript
// 1. Async generator that yields 10 random numbers with delay
async function* asyncGenerator(): AsyncGenerator<number> {
  for (let i = 0; i < 10; i++) {
    await new Promise(resolve => setTimeout(resolve, 1000)); // 1 second delay
    yield Math.random() * 10; // float between 0 and 10
  }
}

// 2. Async function that uses async iteration to collect values
async function asyncComprehension(): Promise<number[]> {
  const result: number[] = [];
  for await (const num of asyncGenerator()) {
    result.push(num);
  }
  return result;
}

// 3. Run the async function
asyncComprehension().then(numbers => {
  console.log("Collected numbers:", numbers);
});
```

---

## ✅ Rust Version

Rust supports asynchronous generators through external crates like `async-gen` and `genawaiter`. Here's an example using `async-gen`:

```rust
use async_gen::gen;
use async_gen::GeneratorState;
use tokio::main;

#[main]
async fn main() {
    let g = gen! {
        yield 42;
        return "42"
    };
    let mut g = pin!(g);
    assert_eq!(g.resume().await, GeneratorState::Yielded(42));
    assert_eq!(g.resume().await, GeneratorState::Complete("42"));
}
```

This example demonstrates creating an asynchronous generator that yields a value and then returns a result.

---

## ✅ Go Version

Go does not natively support asynchronous generators. However, you can simulate similar behavior using goroutines and channels:

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Async generator using goroutines and channels
func asyncGenerator(ch chan<- float64) {
	defer close(ch)
	for i := 0; i < 10; i++ {
		time.Sleep(1 * time.Second) // Simulate delay
		ch <- rand.Float64() * 10  // Send random number to channel
	}
}

func asyncComprehension() []float64 {
	ch := make(chan float64)
	go asyncGenerator(ch)

	var result []float64
	for num := range ch {
		result = append(result, num)
	}
	return result
}

func main() {
	numbers := asyncComprehension()
	fmt.Println("Collected numbers:", numbers)
}
```

This Go program uses a goroutine to simulate asynchronous behavior and channels to collect the generated numbers.

---

## ✅ Ruby Version

Ruby supports asynchronous programming with `async` and `await` using the `async` gem. Here's how you can implement an asynchronous generator:

```ruby
require 'async'
require 'async/queue'

# Async generator that yields 10 random numbers with delay
async def async_generator
  10.times do
    await Async::Task.current.sleep(1) # Simulate delay
    yield rand * 10 # Yield random number
  end
end

# Async function that collects values from the generator
async def async_comprehension
  result = []
  await async_generator do |num|
    result << num
  end
  result
end

# Run the async function
Async do
  numbers = await async_comprehension
  puts "Collected numbers: #{numbers}"
end
```

This Ruby script uses the `async` gem to handle asynchronous operations and collect the generated numbers.

---

## ✅ C++ Version

C++23 introduces `std::generator` to support asynchronous generators. Here's an example:

```cpp
#include <iostream>
#include <coroutine>
#include <generator>
#include <thread>
#include <chrono>

std::generator<double> async_generator() {
    for (int i = 0; i < 10; ++i) {
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Simulate delay
        co_yield static_cast<double>(rand()) / RAND_MAX * 10; // Yield random number
    }
}

int main() {
    for (auto num : async_generator()) {
        std::cout << num << std::endl;
    }
    return 0;
}
```

This C++ program uses `std::generator` to create an asynchronous generator that yields random numbers with a delay.

---

### 🧠 Summary

| Language | Async Generator Syntax | Async Comprehension Syntax |
|----------|------------------------|----------------------------|
| TypeScript | `async function*` | `for await...of` loop |
| Rust | `async-gen` crate | `gen!` macro |
| Go | Goroutines & Channels | `for` loop with channel |
| Ruby | `async` gem | `await` with block |
| C++ | `std::generator` | Range-based `for` loop |

Each language has its own approach to asynchronous programming, but the core concepts remain consistent: asynchronous generators allow for lazy evaluation and non-blocking operations, while async comprehensions provide a concise way to collect values from these generators.

If you need further assistance with any of these implementations or have questions about other languages, feel free to ask!
