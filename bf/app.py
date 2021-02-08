from fastapi import FastAPI
from pydantic import BaseModel
from brainfu_k_compiler import sourcecode_compiled
from createBrainFuck import Create_Brainfuck_Code
from starlette.requests import Request

app = FastAPI()

class Code(BaseModel):
    """
    Brainfuckコード
    """
    bf : str

class Text(BaseModel):
    """
    Brainfuckコードに変換する英文文字
    """
    text : str

@app.get('/')
async def hello():
    return {"result":"hello"}


@app.post('/bf_compiler')
async def bf_code_compile(code : Code):
    try:
        result = sourcecode_compiled(code.bf)
    except Exception as e:
        print(e)
        result = "error"
    return {"result":result}

@app.post('/text_to_bfcode')
async def text2bf(text : Text):
    try:
        result = Create_Brainfuck_Code(text.text).create()
    except Exception as e:
        print(e)
        result = "error"
    return {"result":result}
