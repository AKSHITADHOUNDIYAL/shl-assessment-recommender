FROM python:3.10

RUN useradd -m user
USER user

WORKDIR /app

ENV PATH="/home/user/.local/bin:$PATH"

COPY --chown=user . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]