


# Zerror

**Zerror** is a package designed to make certain tasks in Python easier by providing powerful decorators and functions for efficient error handling and periodic checks.

## Installation

To install the required modules, run the following commands:

```bash
pip install asyncio
pip install inspect
pip install dis
pip install pyperfmon
```
Usage
Make sure when you are running functions from the functions file, use asyncio.run(function) and define your functions with async def instead of just def.

Example Usage
Here’s an example of how to use the periodic check function:

```python


import asyncio
from zerror import check_function_periodically

async def example_action() -> bool:
    # Simulating delay
    await asyncio.sleep(3)
    return True

async def completion():
    print("Action is done!")

async def combination():
    await check_function_periodically(example_action, completion)

asyncio.run(combination())
```
Checking for Infinite Loops
Example usage for checking for infinite loops:

```python

from zerror import check_infinite_loops
check_infinite_loops(__main__)
```
Decorators
If you’re looking for example usage for decorators, you likely already know how to use them. But if you still need examples, feel free to DM me on Discord at mr.ultra69 (Yes, the name is a bit old, forgive my past self 😅).

That’s it for now! Enjoy making your Python programming easier with Zerror. If you have any questions or need specific versions, don’t hesitate to reach out.

Recommended alias to import as is ze as it can be understood as zerror
