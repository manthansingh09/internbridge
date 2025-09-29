from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tempfile
import os
from starlette.responses import FileResponse


app = FastAPI()


class LogbookRequest(BaseModel):
student_id: int
intern_data: dict


@app.post('/generate-logbook')
async def generate_logbook(payload: LogbookRequest):
# Minimal example: create a text PDF using reportlab or write a DOCX
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


fd, path = tempfile.mkstemp(suffix='.pdf')
os.close(fd)
c = canvas.Canvas(path, pagesize=A4)
c.setFont('Helvetica', 12)
c.drawString(40, 800, f"Internship Logbook - Student ID: {payload.student_id}")
c.drawString(40, 780, f"Company: {payload.intern_data.get('company')}")
c.drawString(40, 760, f"Role: {payload.intern_data.get('role')}")
c.drawString(40, 740, "--- Activities (sample) ---")
c.drawString(40, 720, str(payload.intern_data.get('activities', [])))
c.showPage()
c.save()


return FileResponse(path, filename=f"logbook_{payload.student_id}.pdf")