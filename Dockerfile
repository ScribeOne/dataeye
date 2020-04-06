# Pull python 3.8 from alpine base image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV TEST="testfest" 

# Create working directory
RUN mkdir /code
WORKDIR /code

# Copy python requirements
COPY requirements.txt /code/

# Install necessary packages 
# to build project dependencies
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    # install python requirements
    && pip install --no-cache-dir  -r requirements.txt \
    # find packages that are no longer needed
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    # remove packages
    && apk del .build-deps

# Copy files to the workdir
COPY . /code/

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
