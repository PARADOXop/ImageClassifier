FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .  
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .  

RUN pip install --upgrade pip 

CMD ["streamlit", "run", "app.py"]
