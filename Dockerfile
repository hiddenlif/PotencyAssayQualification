FROM python:3.13-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir --root-user-action=ignore numpy==2.2.6 scipy==1.15.3 \
 && groupadd --gid 1000 assay \
 && useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash assay \
 && install -d -o 1000 -g 1000 /app
COPY --chown=1000:1000 app/ /app/
WORKDIR /app
USER assay
CMD ["sleep", "infinity"]
