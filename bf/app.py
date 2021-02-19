from fastapi import FastAPI, Request
from pydantic import BaseModel
from brainfu_k_compiler import sourcecode_compiled
from createBrainFuck import Create_Brainfuck_Code
from jpn2roma import JPN2Roman
from starlette.requests import Request
import time

app = FastAPI()

jpn2roman = JPN2Roman()

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
        if jpn2roman.check(text.text):
            input_text = jpn2roman.do(text.text)
        else:
            input_text = text.text
        result = Create_Brainfuck_Code().execution(input_text)
    except Exception as e:
        print(e)
        result = "error"
    return {"result":result}

@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response