from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import numpy as np
import cv2

app = FastAPI(title='Prahari Netra Local AI')
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173','http://127.0.0.1:5173'], allow_methods=['*'], allow_headers=['*'])
model = YOLO('yolo11n.pt')
VEHICLES = {'car','truck','bus','motorcycle'}

@app.get('/health')
def health(): return {'status':'ok','model':'yolo11n','classes':['person','car','truck','bus','motorcycle']}

@app.post('/detect')
async def detect(file: UploadFile = File(...)):
    data = await file.read()
    frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
    if frame is None: return {'detections': []}
    result = model.predict(frame, conf=0.35, verbose=False)[0]
    detections=[]
    names=result.names
    for box in result.boxes:
        cls=int(box.cls[0]); name=names[cls];
        if name != 'person' and name not in VEHICLES: continue
        x1,y1,x2,y2=box.xyxy[0].tolist()
        detections.append({'class':'PERSON' if name=='person' else 'VEHICLE','confidence':float(box.conf[0]),'bbox':[x1,y1,x2-x1,y2-y1]})
    return {'detections':detections}
