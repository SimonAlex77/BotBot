FROM python:slim
ENV TOKEN='6597671936:AAH9YT9nMdwWGj8wWUxTu9hwqclnnYzfNog'
COPY . .
RUN pip install -r req.txt
CMD python bot.py