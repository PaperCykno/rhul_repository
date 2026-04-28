FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -m ctf
WORKDIR /home/ctf

COPY chall .
COPY flag.txt .

RUN chown root:root /home/ctf/flag.txt && \
    chmod 444 /home/ctf/flag.txt && \
    chmod 555 /home/ctf/chall

USER ctf

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/home/ctf/chall"]
