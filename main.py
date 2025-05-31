from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from resume_parser import extract_text_from_pdf, extract_skills_experience
import shutil
import os

app = FastAPI()

@app.post("/parse-resume/")
async def parse_resume(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Parse resume
        text = extract_text_from_pdf(temp_file_path)
        result = extract_skills_experience(text)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        os.remove(temp_file_path)  # Cleanup

    return result
