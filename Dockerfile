FROM python
COPY . /python
WORKDIR /python
RUN javac Main.python
