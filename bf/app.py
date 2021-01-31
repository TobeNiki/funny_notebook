from fastapi import FastAPI
from pydantic import BaseModel
from brainfu_k_compiler import sourcecode_compiled

from starlette.requests import Request

app = FastAPI()

class Code(BaseModel):
    """
    Brainfuckコード
    """
    bf : str

@app.post('/bf_compiler')
async def bf_code_compile(code : Code):
    result = sourcecode_compiled(code.bf)
    return {"result":result}
