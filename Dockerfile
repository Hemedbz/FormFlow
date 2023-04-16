FROM python:3.11
COPY FormFlow /etc/FormFlow/FormFlow
COPY formsapp /etc/FormFlow/formsapp
COPY requirements.txt /etc/capsule-backend/
COPY front /etc/FormFlow/front
WORKDIR /etc/FormFlow
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD
