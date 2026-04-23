{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bd6a9ff4-86db-4892-a7e0-78103e7ea369",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdccdbd2-a7b8-4952-b91e-d8b80d1b50ed",
   "metadata": {},
   "source": [
    "# load model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bfdb4b78-0eb2-4042-912c-24f3c0aa3334",
   "metadata": {},
   "outputs": [
    {
     "ename": "UnpicklingError",
     "evalue": "invalid load key, '\\x07'.",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mUnpicklingError\u001b[39m                           Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m model = \u001b[43mpickle\u001b[49m\u001b[43m.\u001b[49m\u001b[43mload\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mdigit_model.pkl\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mrb\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mUnpicklingError\u001b[39m: invalid load key, '\\x07'."
     ]
    }
   ],
   "source": [
    "model = pickle.load(open(\"digit_model.pkl\", \"rb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98038846-d3c7-453b-b6dc-f60df10d71ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"Digit Recogition App\")\n",
    "\n",
    "st.write(\"Enter pixel value (0-16) separeted by commas:\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dab8f76-82b0-45c1-be03-cb295fc6f075",
   "metadata": {},
   "outputs": [],
   "source": [
    "user_input = st.text_input(\"Example: 0, 0, 5, 13, 9, ....\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35b5a346-751d-430f-8978-ea3a3b220757",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.butto(\"predict\"):\n",
    "    try:\n",
    "        data = np.array([list(map(innt, user_input.spli(\" , \")))])\n",
    "        prediction = model.predict(data)\n",
    "        st.sucess(f\"predicted Digit: {prediction[0]}')\n",
    "    except:\n",
    "        st.error(\"Invalid input format\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c231d67-bbc1-4650-a3a4-5ca022be2664",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4450e7d-912b-4b10-a57a-a05f79c6a70b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
