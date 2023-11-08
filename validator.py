from functools import wraps
from colorama import Fore
import  logging
import traceback

def throw_error(msg):
    stack_error = traceback.format_stack()
    stack_error.pop(-1)
    stack_error.pop(-1)
    Fore.RED
    for err in stack_error:
        logging.error(Fore.RED + err + Fore.RESET)
    logging.error(Fore.RED + ' ' + msg + Fore.RESET)

def text(max: int = 255, min: int = 0) -> object:
    """Determina o tamanho máximo e mínimo da str de entrada de uma função."""
    def execute(func: object) -> object:
        @wraps(func)
        def call(*args) -> object:
            try:
                
                param = args[0] if func.__name__ == func.__qualname__ else args[1]

                if (not isinstance(max, int) or isinstance(max, bool)) or (not isinstance(min, int) or isinstance(min, bool)):
                    raise TypeError(1)
                
                if not isinstance(param, str):
                    raise TypeError(2)

                if len(param) > max:
                    raise ValueError(1)
                
                if len(param) < min:
                    raise ValueError(2)
                
                return func(*args)
        
            except TypeError as e:
                if e.args[0] == 1:
                    throw_error(f'A função {func.__name__}() está utilizando o decorator @text e informando um tipo diferente de int():\nmax: {type(max)} min: {type(min)}')
                if e.args[0] == 2:
                    throw_error(f'Não é possível atribuir {type(param)} para {func.__name__}()')

            except ValueError as e:
                if e.args[0] == 1:
                    throw_error(f'A função {func.__name__}() suporta no máximo {max} caracteres, e você está informando {len(param)}.')
                if e.args[0] == 2:
                    throw_error(f'A função {func.__name__}() suporta no minimo {min} caracteres, e você está informando {len(param)}.')
            
            return
        return call
    return execute 
