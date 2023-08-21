FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --upgrade tensorflow streamlit
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["streamlit", "run", "app.py"]
