# Python Async Functions

## Learning Objectives

1. `async` and `await` syntax
2. How to execute an async program with `asyncio`
3. How to run concurrent coroutines
4. How to create `asyncio` tasks
5. How to use the `random` module

### `Async` and `await` syntax

Let's dive into the concepts of `async` and `await` in Python.

### **1. What is Asynchronous Programming?**

Asynchronous programming allows you to write code that performs non-blocking operations. This means that instead of waiting for a task (like a network request or I/O operation) to finish before moving to the next task, your program can handle multiple tasks concurrently, increasing efficiency.

In traditional synchronous programming, your program will wait (or "block") until an operation (like reading a file or fetching data from a server) is completed before continuing. In asynchronous programming, your program can continue executing other tasks while waiting for operations to complete.

### **2. `async` and `await` Syntax**

Python introduced the `async` and `await` keywords to simplify asynchronous programming and make it more readable.

#### **`async` keyword**

The `async` keyword is used to define an **asynchronous function** (also called a coroutine). This function will return a coroutine object, which is an object that represents the function's execution but hasn't run yet.

Example:

```python
async def my_coroutine():
    print("This is an async function")
```

#### **`await` keyword**

The `await` keyword is used inside an asynchronous function to pause execution and wait for a **task** (usually another coroutine) to finish before continuing. When you `await` a coroutine, Python will run the coroutine and wait for its result, without blocking the entire program.

Example:

```python
import asyncio

async def main():
    await asyncio.sleep(2)  # Pause for 2 seconds without blocking
    print("2 seconds have passed!")

asyncio.run(main())
```

In this example:

- `asyncio.sleep(2)` is a coroutine that makes the program "sleep" for 2 seconds asynchronously (non-blocking).
- The `await` keyword tells the program to pause the `main` function until `asyncio.sleep(2)` completes.

#### **How Does `async` and `await` Work Together?**

- `async` is used to declare a function as asynchronous (i.e., a coroutine).
- `await` is used to pause the execution of the function until the awaited coroutine finishes.

### **3. Example of Asynchronous Code**

Let’s write a simple example that demonstrates asynchronous programming using `async` and `await`. Suppose we need to perform multiple time-consuming tasks, but we don't want to wait for each one to finish before starting the next. We'll simulate this with the `asyncio.sleep()` function:

```python
import asyncio

# Define an asynchronous function
async def task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)  # Simulate a delay (e.g., waiting for data)
    print(f"Task {name} finished after {delay} seconds")

# Define the main coroutine that runs the tasks concurrently
async def main():
    # Create tasks with different delays
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))
    task3 = asyncio.create_task(task("C", 3))
    
    # Wait for all tasks to finish
    await task1
    await task2
    await task3

# Run the main coroutine
asyncio.run(main())
```

### **Explanation of Example:**

- `task()` is an asynchronous function that simulates work by waiting for a delay (`await asyncio.sleep(delay)`).
- In `main()`, we use `asyncio.create_task()` to create multiple tasks that run concurrently. Each task is executed asynchronously.
- When `asyncio.run(main())` is called, the program runs all tasks concurrently, and the output is printed as each task starts and finishes.

### **4. Why Use `async` and `await`?**

The primary benefits of asynchronous programming are:

1. **Concurrency**: You can execute multiple tasks at the same time without blocking each other. This is particularly useful for I/O-bound tasks (e.g., web scraping, database access, file operations).
2. **Efficiency**: Your program can be more efficient in handling tasks that involve waiting (like waiting for a file or a network response), instead of wasting time while waiting.
3. **Readability**: `async` and `await` syntax is more readable than using traditional callback-based approaches (like those used in `asyncio` in earlier versions).

### **5. How Asynchronous Code Works in Practice**

Let's say you're making several web requests. If done synchronously, you'd have to wait for one request to finish before starting the next. Using `asyncio`, you can run all requests concurrently, which would be much faster.

Here’s a quick illustration using `asyncio` for making asynchronous HTTP requests:

```python
import asyncio
import aiohttp  # You need the aiohttp library for async HTTP requests

# Define an async function to make an HTTP request
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# Define a main coroutine that fetches multiple URLs concurrently
async def main():
    urls = [
        "http://example.com",
        "https://example.org",
        "https://example.net"
    ]
    
    # Create a list of tasks
    tasks = [fetch_url(url) for url in urls]
    
    # Run all tasks concurrently and get the results
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(f"Fetched {len(result)} characters")

# Run the main coroutine
asyncio.run(main())
```

In this example:

- `fetch_url()` is an asynchronous function that fetches data from a URL.
- `asyncio.gather(*tasks)` runs all the fetch tasks concurrently.

### **6. Common Mistakes and Things to Remember**

- **No blocking code in async functions**: If you have blocking code (e.g., `time.sleep()`), it will block the entire event loop. Always use asynchronous alternatives, like `asyncio.sleep()`, for non-blocking behavior.
- **`await` must be used inside `async` functions**: You can’t use `await` outside of `async` functions. If you try to, Python will raise a `SyntaxError`.
- **Event loop management**: When you use `asyncio.run()`, it automatically manages the event loop. For more complex cases, you may need to manually manage the event loop.

### **7. Key Functions and Libraries**

- **`asyncio.sleep(seconds)`**: Non-blocking sleep (asynchronous).
- **`asyncio.create_task()`**: Creates a task to run a coroutine.
- **`asyncio.gather()`**: Runs multiple coroutines concurrently and waits for them to finish.
- **`aiohttp`**: A library for making asynchronous HTTP requests.

### Conclusion

The `async` and `await` keywords are powerful tools in Python for writing efficient, non-blocking, concurrent code. By using `async` functions and awaiting tasks, you can handle time-consuming operations (like I/O or network calls) concurrently, without blocking the program's flow.
