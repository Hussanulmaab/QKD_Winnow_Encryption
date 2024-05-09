from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
import os
from Winnow_1.Winnow_1_Web import Winnow_1_Web
from Performance_Check.Performance_Check import Performance_Check
from Permutation_Winnow.Winnow_Rounds import Winnow_Rounds

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Create a directory to store uploaded files if it doesn't exist
upload_folder = "./Performance_Check"
os.makedirs(upload_folder, exist_ok=True)


@app.get("/")
async def upload_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/upload/")
async def upload_files(request: Request, file1: UploadFile = File(...), file2: UploadFile = File(...), Winnow_Rounds_Number: int = Form(...)):
    file1_content = await file1.read()
    file2_content = await file2.read()

    # Save the uploaded files
    with open(os.path.join(upload_folder, file1.filename), "wb") as f:
        f.write(file1_content)
    with open(os.path.join(upload_folder, file2.filename), "wb") as f:
        f.write(file2_content)

    Winnow_Msg = Winnow_1_Web()
    Winnow_Rounds(Winnow_Rounds_Number)
    results = Performance_Check()

    # return templates.TemplateResponse("Results.html", {"request": request, "filename1": file1.filename, "filename2": file2.filename, "Winnow_Msg": Winnow_Msg, "results": results})
    return templates.TemplateResponse("Results.html", {"request": request, "Winnow_Msg": Winnow_Msg, "results": results})