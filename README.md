# OpenAI
Jumpstart your OpenAI API development with Docker!

Join the beta: [OpenAI API Waitlist](https://share.hsforms.com/1Lfc7WtPLRk2ppXhPjcYY-A4sk30)

This is designed to be a quick and dirty jumpstart to building an OpenAI Python app using Streamlit.

# Requirements
- Docker Compose

- OpenAI beta key (see above)

- Must have your API key assigned to $OPENAI_API_KEY environmental variable:
```bash
      export OPENAI_API_KEY=<insert-key-here>
```


# Usage
Use the 3 line ./RunCommand.sh script (or your own) to spin up the container.
:
```bash
      ./RunCommand.sh
```

Navigate to localhost:8501 in your favorite browser and screw around!

# Future additions (pulls welcome!):
- Reverse proxy (NGINX/Apache) for easy web-hosting

- Alternative use case examples, completion (done!), Q&A, Chatbot, etc.

- Prettier interface