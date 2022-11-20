FROM python:3-slim

RUN useradd -ms /bin/bash debian
RUN pip install --no-cache-dir flask gunicorn
WORKDIR /home/debian/web
ADD web.py run.sh /home/debian/web/
RUN chown -R debian:debian /home/debian/web
USER debian
EXPOSE 8000
CMD /bin/bash run.sh