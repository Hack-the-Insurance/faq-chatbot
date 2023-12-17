# Sigortam Cepte FAQ Chatbot

This application was developed as part of the Anadolu Sigorta Hackathon. It's a Natural language processing based chatbot designed to answer questions on customers' minds. You send your question and the chatbot returns you the appropriate answer from the FAQ section.

## Technologies Used

- [Rasa](https://rasa.com/docs/rasa/) - Rasa version: 3.6.15
- [Requests](https://requests.readthedocs.io/en/latest/user/quickstart.html) - Requests version: 2.31.0
- [Streamlit](https://docs.streamlit.io/library/get-started) - Streamlit: 1.29.0

---

## Requirements

### Environment

Ensure that your Python version is set to `3.10.12`:

```bash
python --version
```

- Setting up Virtualenv:

```bash
pip install virtualenv
```
- Creating a Virtual Environment:
```bash
virtualenv venv
```
- Activating the Virtual Environment:
```bash
source venv/bin/activate
```
- Installing the necessary libraries:
```bash
pip install -r requirements.txt
```
- Set up your .env file:

```bash
cd <project-directory>
```

### Run
- rasa connection
```bash
rasa shell
```
- Launch the Streamlit app in another terminal
```bash
streamlit run app.py
```
---


https://github.com/Hack-the-Insurance/faq-chatbot/assets/88631980/01214525-edce-499b-b8c1-2978d64c2e3f




