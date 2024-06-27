# Streamlit Basic Project
This project showcases a Streamlit application demonstrating functionalities like: Word Correction, Object Detection, Chatbot


## Live Demo:

 - Word Correction: https://thuytran-02.streamlit.app/
- Object Detection: https://thuytran-03.streamlit.app/
- Chatbot: https://thuytran-01.streamlit.app/



## Getting Started

This section details how to set up the development environment to run the application.


### Clone the Repository

-  Open your terminal.
- Run the following command to clone the repository

Bash

```
git clone https://github.com/ThuyTran07/Streamlit_Basics.git

```

**Note:** Use the provided command with caution. It will download the entire repository to your local machine.


### Create a Virtual Environment

It's recommended to create a virtual environment to isolate project dependencies. Here's how to do it depending on your operating system:


**Linux/macOS:**

Bash

```
python3 -m venv venv
source venv/bin/activate

```


**Windows:**

Bash

```
python -m venv venv
venv\Scripts\activate

```

**Note:** Use the provided commands with caution. They will create and activate a virtual environment named `venv`.


### Install the Required Dependencies

Once the virtual environment is activated, install the required dependencies listed in the `requirements.txt` file using the following command:

Bash

```
pip install -r requirements.txt

```

**Note:** Use the provided command with caution. It will install all the necessary libraries from the `requirements.txt` file.


## Running the App

Now that the environment is set up, you can start the Streamlit development server.

This project contains multiple Streamlit applications in separate Python files (`es1_levenshtein_distance.py`, `es2_object_detection.py`, and `es3_chatbot.py`). Choose the script corresponding to the application you want to run by replacing the script name in the following command:

Bash

```
streamlit run <script_name.py>  # Replace with your app script name

```


**Example:**

Bash

```
streamlit run es2_object_detection.py  # To run the object detection application

```

**Note:** Use the provided commands with caution. They will launch the corresponding Streamlit application in your web browser.