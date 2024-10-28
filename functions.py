import asyncio as asy 
import dis 
import inspect 
def check_infinite_loops(script ): 
    functions = inspect.getmembers(script, inspect.isfunction)
    for name , function in functions :
        bytecode = dis.Bytecode(function)
        infinite_loop = False 
        break_loop = False 
        for instr in bytecode  : 
            if instr.opname == "SETUP_LOOP" : 
                infinite_loop = True
            if instr.opname == "BREAK_LOOP" :
                break_loop = True 
            
        if infinite_loop and not break_loop : 
            choi = input(f"warning : Function '{function}' has an infinite loop (will use almost 100% CPU and if your computer is weak , it way crash.) do you still want to run it ?")
            if choi == "y" :
                asy.run(function)
            else : 
                print("not --run! ")


async def check_function_periodically(action, function_after_completion):
    """Continuously checks the action and runs the function_after_completion if action is done."""
    while True:
        if await action():
            function_after_completion()
        else:
            await asy.sleep(15)

# im bouta get carpal tunnel syndrome for real dude

def call_error(Error_type : Exception , statement : str) -> None: 
    raise Error_type(statement)

#easier syntax , doesnt scare the newbies with "raise"


