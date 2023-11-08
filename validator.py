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

def max_char(value: int) -> object:
    """Determina o tamanho máximo da str de entrada de uma função."""
    def execute(func: object) -> object:
        @wraps(func)
        def call(*args) -> object:
            try:
                
                if not isinstance(value, int) or isinstance(value, bool):
                    raise TypeError(1)
                
                if not isinstance(args[1], str):
                    raise TypeError(2)

                if len(args[1]) > value:
                    raise ValueError
                
                return func(*args)
        
            except TypeError as e:
                if e.args[0] == 1:
                    throw_error(f'A função {func.__name__}() está utilizando o decorator @max_len e informando um tipo diferente de int(): {type(value)}')
                if e.args[0] == 2:
                    throw_error(f'Não é possível atribuir {type(args[1])} para {func.__name__}()')

            except ValueError:
                throw_error(f'A função {func.__name__}() suporta até {value} caracteres, e você está informando {len(args[1])}.')
            
            return
        return call
    return execute 
